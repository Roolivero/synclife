from enum import Enum

from src.api.v1.shopping_list.domain.errors import ShoppingListError

class ShoppingListValidationTypeError(Enum):
    INVALID_PRODUCT_NAME = "El nombre del producto no puede estar vacio."
    INVALID_AMOUNT = "La cantidad del producto debe ser mayor a 0."
    
class ShoppingListValidationError(ShoppingListError):
    def __init__(self, error_type: ShoppingListValidationTypeError):
        super().__init__(error_type.value)