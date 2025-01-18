from enum import Enum

from src.api.v1.shopping_list.domain.errors import ShoppingListError


class ShoppingListValidationTypeError(Enum):
    INVALID_PRODUCT_NAME = "El nombre del producto no puede estar vacio."
    INVALID_AMOUNT = "La cantidad del producto debe ser mayor a 0."
    ITEM_NOT_FOUND = "No se encontro el producto"
    ITEM_NOT_OWNED = "Esta shopping list no pertenece al usuario"
    OPERATION_FAILED = "La operación no pudo completarse. Inténtalo nuevamente."


class ShoppingListValidationError(ShoppingListError):
    def __init__(self, error_type: ShoppingListValidationTypeError):
        super().__init__(error_type.value)
