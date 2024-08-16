"""Module that contains cart domain routers."""

from bson import ObjectId
from fastapi import APIRouter, Depends, Security, status

from app.api.v1.auth.auth import StrictAuthorization
from app.api.v1.constants import ScopesEnum
from app.api.v1.dependencies.cart import (
    CartAccessDependency,
    CartByUserGetDependency,
    CartProductDataCreateDependency,
    CartProductDataDeleteDependency,
    CartProductDataUpdateDependency,
)
from app.api.v1.dependencies.product import ProductByIdGetDependency
from app.api.v1.models.cart import (
    Cart,
    CartProduct,
    CartProductQuantity,
)
from app.api.v1.models.product import Product
from app.api.v1.services.cart import CartService

router = APIRouter(prefix="/carts", tags=["carts"])


@router.get(
    "/me/",
    response_model=Cart,
    status_code=status.HTTP_200_OK,
    dependencies=[
        Security(StrictAuthorization(), scopes=[ScopesEnum.CARTS_GET_CART.name])
    ],
)
async def get_cart(cart: Cart = Depends(CartByUserGetDependency())) -> Cart:
    """API which returns cart of current user.

    Args:
        cart (Cart): Cart object.

    Returns:
        Cart: Cart object.

    """
    return cart


@router.post(
    "/{cart_id}/products/",
    response_model=Cart,
    status_code=status.HTTP_201_CREATED,
    dependencies=[
        Security(StrictAuthorization(), scopes=[ScopesEnum.CARTS_ADD_PRODUCT.name])
    ],
)
async def add_product_to_the_cart(
    cart_product: CartProduct = Depends(CartProductDataCreateDependency()),
    cart: Cart = Depends(CartAccessDependency()),
    cart_service: CartService = Depends(),
) -> Cart:
    """API which adds product to the cart.

    Args:
        cart_product (CartProduct): Cart product data.
        cart (Cart): Cart object.
        cart_service (CartService): Cart service.

    Returns:
        Cart: Cart object.

    """
    return await cart_service.add_product(id_=cart.id, data=cart_product)


@router.patch(
    "/{cart_id}/products/{product_id}/",
    response_model=Cart,
    status_code=status.HTTP_200_OK,
    dependencies=[
        Security(StrictAuthorization(), scopes=[ScopesEnum.CARTS_UPDATE_PRODUCT.name])
    ],
)
async def update_product_in_the_cart(
    cart_product_quantity: CartProductQuantity = Depends(
        CartProductDataUpdateDependency()
    ),
    cart: Cart = Depends(CartAccessDependency()),
    product: Product = Depends(ProductByIdGetDependency()),
    cart_service: CartService = Depends(),
) -> Cart:
    """API which updates product in the cart.

    Args:
        cart_product_quantity (CartProductQuantity): Cart product quantity data.
        cart (Cart): Cart object.
        product (Product): Product object.
        cart_service (CartService): Cart service.

    Returns:
        Cart: Cart object.

    """
    return await cart_service.update_product(
        id_=cart.id,
        product_id=product.id,
        data=cart_product_quantity,
    )


@router.delete(
    "/{cart_id}/products/{product_id}/",
    response_model=Cart,
    status_code=status.HTTP_200_OK,
    dependencies=[
        Security(StrictAuthorization(), scopes=[ScopesEnum.CARTS_DELETE_PRODUCT.name])
    ],
)
async def delete_product_from_the_cart(
    product_id: ObjectId = Depends(CartProductDataDeleteDependency()),
    cart: Cart = Depends(CartAccessDependency()),
    cart_service: CartService = Depends(),
) -> Cart:
    """API which deletes product from the cart.

    Args:
        product_id (ObjectId): BSON object identifier of requested product.
        cart (Cart): Cart object.
        cart_service (CartService): Cart service.

    """
    return await cart_service.delete_product(
        id_=cart.id,
        product_id=product_id,
    )
