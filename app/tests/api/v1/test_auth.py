"""Module that contains tests for auth routes."""

from unittest.mock import Mock, patch

import pytest
from fastapi import status
from httpx import AsyncClient
from jose import ExpiredSignatureError

from app.api.v1.auth.jwt import JWT
from app.api.v1.constants import ScopesEnum
from app.constants import AppConstants, HTTPErrorMessagesEnum
from app.services.mongo.constants import MongoCollectionsEnum
from app.tests.api.v1 import BaseAPITest
from app.tests.constants import (
    CUSTOMER_USER,
    DELETED_USER,
    FAKE_USER,
    NOT_VERIFIED_EMAIL_USER,
    TEST_JWT,
    USER_NO_SCOPES,
)


class TestAuth(BaseAPITest):
    """Test class for auth API endpoints in the FastAPI application."""

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "arrange_db", [(MongoCollectionsEnum.USERS,)], indirect=True
    )
    async def test_create_tokens(
        self, test_client: AsyncClient, arrange_db: None
    ) -> None:
        """Test auth token creation."""

        response = await test_client.post(
            f"{AppConstants.API_V1_PREFIX}/auth/tokens/",
            data={
                "username": "john.smith",
                "password": "John1234!",
                "grant_type": "password",
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json().keys() == {
            "access_token",
            "refresh_token",
            "token_type",
        }
        # If scope is not requested returns all permitted
        assert set(JWT.decode_token(response.json()["access_token"]).scopes) == {
            ScopesEnum.AUTH_REFRESH_TOKEN.name,
            ScopesEnum.USERS_GET_ME.name,
            ScopesEnum.USERS_UPDATE_USER.name,
            ScopesEnum.USERS_UPDATE_USER_PASSWORD.name,
            ScopesEnum.USERS_DELETE_USER.name,
            ScopesEnum.ROLES_GET_ROLES.name,
            ScopesEnum.CATEGORIES_GET_CATEGORIES.name,
            ScopesEnum.CATEGORIES_GET_CATEGORY.name,
            ScopesEnum.CATEGORIES_GET_CATEGORY_PARAMETERS.name,
            ScopesEnum.PRODUCTS_GET_PRODUCTS.name,
            ScopesEnum.PRODUCTS_GET_PRODUCT.name,
        }

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "arrange_db", [(MongoCollectionsEnum.USERS,)], indirect=True
    )
    async def test_create_tokens_with_scopes_request(
        self, test_client: AsyncClient, arrange_db: None
    ) -> None:
        """Test auth token creation with scopes request."""

        response = await test_client.post(
            f"{AppConstants.API_V1_PREFIX}/auth/tokens/",
            data={
                "username": "john.smith",
                "password": "John1234!",
                "scope": " ".join(
                    [
                        ScopesEnum.USERS_GET_ME.name,
                        ScopesEnum.AUTH_REFRESH_TOKEN.name,
                    ]
                ),
                "grant_type": "password",
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json().keys() == {
            "access_token",
            "refresh_token",
            "token_type",
        }

        assert JWT.decode_token(response.json()["access_token"]).scopes == [
            ScopesEnum.USERS_GET_ME.name,
            ScopesEnum.AUTH_REFRESH_TOKEN.name,
        ]

    @pytest.mark.asyncio
    async def test_create_tokens_missing_fields(self, test_client: AsyncClient) -> None:
        """Test auth token creation in case username/password is missed."""

        response = await test_client.post(
            f"{AppConstants.API_V1_PREFIX}/auth/tokens/",
            data={"username": "john.smith"},
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert [
            (error["type"], error["loc"], error["msg"])
            for error in response.json()["detail"]
        ] == [
            ("missing", ["body", "grant_type"], "Field required"),
            ("missing", ["body", "password"], "Field required"),
        ]

    @pytest.mark.asyncio
    async def test_create_tokens_user_does_not_exist(
        self, test_client: AsyncClient
    ) -> None:
        """Test auth token creation in case user with such username does not exist."""

        response = await test_client.post(
            f"{AppConstants.API_V1_PREFIX}/auth/tokens/",
            data={
                "username": "joe.smith",
                "password": "john1234",
                "grant_type": "password",
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.json() == {
            "detail": HTTPErrorMessagesEnum.INCORRECT_CREDENTIALS
        }

    @pytest.mark.asyncio
    async def test_create_tokens_invalid_password(
        self, test_client: AsyncClient
    ) -> None:
        """Test auth token creation in case user with such username does not exist."""

        response = await test_client.post(
            f"{AppConstants.API_V1_PREFIX}/auth/tokens/",
            data={
                "username": "john.smith",
                "password": "john1234smith",
                "grant_type": "password",
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.json() == {
            "detail": HTTPErrorMessagesEnum.INCORRECT_CREDENTIALS
        }

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "arrange_db", [(MongoCollectionsEnum.USERS,)], indirect=True
    )
    async def test_create_tokens_deleted_user(
        self, test_client: AsyncClient, arrange_db: None
    ) -> None:
        """Test auth token creation in case user is deleted."""

        response = await test_client.post(
            f"{AppConstants.API_V1_PREFIX}/auth/tokens/",
            data={
                "username": "sheila.fahey",
                "password": "Sheila1234!",
                "grant_type": "password",
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.json() == {
            "detail": HTTPErrorMessagesEnum.INCORRECT_CREDENTIALS
        }

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "arrange_db", [(MongoCollectionsEnum.USERS,)], indirect=True
    )
    async def test_create_tokens_user_email_is_not_verified(
        self, test_client: AsyncClient, arrange_db: None
    ) -> None:
        """Test auth token creation in case user email is not verified."""

        response = await test_client.post(
            f"{AppConstants.API_V1_PREFIX}/auth/tokens/",
            data={
                "username": "lila.legro",
                "password": "Lila1234!",
                "grant_type": "password",
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "arrange_db", [(MongoCollectionsEnum.USERS,)], indirect=True
    )
    async def test_create_tokens_request_not_permitted_scopes(
        self, test_client: AsyncClient, arrange_db: None
    ) -> None:
        """Test auth token creation in case user request not permitted scopes."""

        response = await test_client.post(
            f"{AppConstants.API_V1_PREFIX}/auth/tokens/",
            data={
                "username": "john.smith",
                "password": "John1234!",
                "scope": " ".join(
                    [
                        ScopesEnum.USERS_GET_ME.name,
                        ScopesEnum.HEALTH_GET_HEALTH.name,
                    ]
                ),
                "grant_type": "password",
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert response.json() == {"detail": HTTPErrorMessagesEnum.PERMISSION_DENIED}

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "arrange_db", [(MongoCollectionsEnum.USERS,)], indirect=True
    )
    @patch("jose.jwt.decode", Mock(return_value=CUSTOMER_USER))
    async def test_refresh_access_token(
        self, test_client: AsyncClient, arrange_db: None
    ) -> None:
        """Test refreshing access token."""

        response = await test_client.post(
            f"{AppConstants.API_V1_PREFIX}/auth/access-token/",
            headers={"Authorization": f"Bearer {TEST_JWT}"},
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json().keys() == {"access_token", "token_type"}

    @pytest.mark.asyncio
    async def test_refresh_access_token_invalid_token(
        self, test_client: AsyncClient
    ) -> None:
        """Test refreshing access token in case refresh token is invalid."""

        response = await test_client.post(
            f"{AppConstants.API_V1_PREFIX}/auth/access-token/",
            headers={"Authorization": f"Bearer {TEST_JWT}"},
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.json() == {"detail": HTTPErrorMessagesEnum.INVALID_CREDENTIALS}

    @pytest.mark.asyncio
    @patch("jose.jwt.decode", Mock(side_effect=ExpiredSignatureError()))
    async def test_refresh_access_token_is_expired(
        self, test_client: AsyncClient
    ) -> None:
        """Test refreshing access token in case refresh token is expired."""

        response = await test_client.post(
            f"{AppConstants.API_V1_PREFIX}/auth/access-token/",
            headers={"Authorization": f"Bearer {TEST_JWT}"},
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.json() == {"detail": HTTPErrorMessagesEnum.EXPIRED_TOKEN}

    @pytest.mark.asyncio
    @patch("jose.jwt.decode", Mock(return_value=FAKE_USER))
    async def test_refresh_access_token_user_does_not_exist(
        self, test_client: AsyncClient
    ) -> None:
        """
        Test refreshing access token in case user from refresh token does not exist.
        """

        response = await test_client.post(
            f"{AppConstants.API_V1_PREFIX}/auth/access-token/",
            headers={"Authorization": f"Bearer {TEST_JWT}"},
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.json() == {"detail": HTTPErrorMessagesEnum.NOT_AUTHORIZED}

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "arrange_db", [(MongoCollectionsEnum.USERS,)], indirect=True
    )
    @patch("jose.jwt.decode", Mock(return_value=DELETED_USER))
    async def test_refresh_access_token_deleted_user(
        self, test_client: AsyncClient, arrange_db: None
    ) -> None:
        """Test refreshing access token in case user is deleted."""

        response = await test_client.post(
            f"{AppConstants.API_V1_PREFIX}/auth/access-token/",
            headers={"Authorization": f"Bearer {TEST_JWT}"},
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.json() == {"detail": HTTPErrorMessagesEnum.NOT_AUTHORIZED}

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "arrange_db", [(MongoCollectionsEnum.USERS,)], indirect=True
    )
    @patch("jose.jwt.decode", Mock(return_value=NOT_VERIFIED_EMAIL_USER))
    async def test_refresh_access_token_user_email_is_not_verified(
        self, test_client: AsyncClient, arrange_db: None
    ) -> None:
        """Test refreshing access token in case user email is not verified."""

        response = await test_client.post(
            f"{AppConstants.API_V1_PREFIX}/auth/access-token/",
            headers={"Authorization": f"Bearer {TEST_JWT}"},
        )

        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert response.json() == {
            "detail": HTTPErrorMessagesEnum.EMAIL_IS_NOT_VERIFIED
        }

    @pytest.mark.asyncio
    @patch("jose.jwt.decode", Mock(return_value=USER_NO_SCOPES))
    @pytest.mark.parametrize(
        "arrange_db", [(MongoCollectionsEnum.USERS,)], indirect=True
    )
    async def test_refresh_access_token_no_scope(
        self, test_client: AsyncClient, arrange_db: None
    ) -> None:
        """
        Test refreshing access token in case user does not have appropriate scope.
        """

        response = await test_client.post(
            f"{AppConstants.API_V1_PREFIX}/auth/access-token/",
            headers={"Authorization": f"Bearer {TEST_JWT}"},
        )

        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert response.json() == {"detail": HTTPErrorMessagesEnum.PERMISSION_DENIED}
