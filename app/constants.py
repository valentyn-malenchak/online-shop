"""Module that provides application level constants."""

from enum import Enum


class EnvironmentsEnum(Enum):
    """Application environments enumerate."""

    DEV = "dev"
    PROD = "prod"


class HTTPErrorMessagesEnum(Enum):
    """Contains HTTP error messages."""

    NOT_AUTHORIZED = "Not authorized."
    INCORRECT_CREDENTIALS = "Incorrect username or password."
    EXPIRED_TOKEN = "Token is expired."
    INVALID_CREDENTIALS = "Invalid credentials."
    PERMISSION_DENIED = "Permission denied."
    EMAIL_IS_NOT_VERIFIED = "Email is not verified."
    EMAIL_IS_ALREADY_VERIFIED = "Email is already verified."

    USER_ACCESS_DENIED = "Access denied to another user."
    ROLE_ACCESS_DENIED = "Access denied to use role."
    CLIENT_USER_ACCESS_DENIED = "Access denied to client user."

    ENTITY_IS_NOT_FOUND = "{entity} is not found."
    ENTITY_FIELD_UNIQUENESS = "{entity} with such {field} is already exist."

    PASSWORD_DOES_NOT_MATCH = "The current password does not match."

    INVALID_RESET_PASSWORD_TOKEN = "Invalid or expired reset password token."
    INVALID_EMAIL_VERIFICATION_TOKEN = "Invalid or expired email verification token."

    LEAF_PRODUCT_CATEGORY_REQUIRED = (
        "Invalid category. Operation is allowed only for 'leaf' categories."
    )
    PRODUCT_ACCESS_DENIED = "Access denied to product."
    PRODUCTS_AVAILABLE_FILTER_ACCESS_DENIED = "Access denied to not available products."


# Password policies
PASSWORD_MIN_CHARACTERS_POLICY = 8

# Username policies
USERNAME_MIN_CHARACTERS_POLICY = 8
USERNAME_MAX_CHARACTERS_POLICY = 30
USERNAME_ALLOWED_SPECIAL_CHARACTER = "_-."


class ValidationErrorMessagesEnum(Enum):
    """Contains validation error messages for Pydantic models."""

    INVALID_IDENTIFIER = "Invalid object identifier."
    REQUIRED_FIELD = "Field required."
    INVALID_FIELD_TYPE = "Field should be a valid {type_}."

    # Password policies
    PASSWORD_MIN_LENGTH = "Password must contain at least eight characters."
    PASSWORD_WITHOUT_DIGIT = "Password must contain at least one digit."
    PASSWORD_WITHOUT_LOWERCASE_LETTER = (
        "Password must contain at least one lowercase letter."
    )
    PASSWORD_WITHOUT_UPPERCASE_LETTER = (
        "Password must contain at least one uppercase letter."
    )
    PASSWORD_WITHOUT_SPECIAL_CHARACTER = (
        "Password must contain at least one special character."
    )

    # Username policies
    USERNAME_MIN_LENGTH = "Username must contain at least eight characters."
    USERNAME_MAX_LENGTH = "Username must contain at most thirty characters."
    USERNAME_NOT_ALLOWED_CHARACTERS = (
        "Username must contain only alphanumeric characters, "
        "hyphen, underscore, or dot."
    )


PAGINATION_MAX_PAGE_SIZE = 100


class SortingTypesEnum(Enum):
    """Sorting types enumerate."""

    ASC = "asc"
    DESC = "desc"


class SortingValuesEnum(Enum):
    """Sorting values enum."""

    ASC = 1
    DESC = -1


class ProjectionValuesEnum(Enum):
    """Projection values enumerate."""

    INCLUDE = 1
    EXCLUDE = 0


BACKGROUND_TASK_RETRY_ATTEMPTS = 3
BACKGROUND_TASK_RETRY_WAIT = 5
