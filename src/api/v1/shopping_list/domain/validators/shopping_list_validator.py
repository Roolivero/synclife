from datetime import date

from src.api.v1.shopping_list.domain.errors import ShoppingListValidationTypeError, ShoppingListValidationError

class ShoppingListValidator:
    @staticmethod
    def validate_amount(amount: int) -> int:
        if amount < 1 : 
            raise ShoppingListValidationError(ShoppingListValidationTypeError.INVALID_AMOUNT)
        return amount
    
    @staticmethod
    def validate_product_name(name: str) -> str:
        if not name:
            raise ShoppingListValidationError(ShoppingListValidationTypeError.INVALID_PRODUCT_NAME)
        return name
    
    @staticmethod
    def validate_all(amount: int, product_name: str) -> None:
        ShoppingListValidator.validate_amount(amount)
        ShoppingListValidator.validate_product_name(product_name)