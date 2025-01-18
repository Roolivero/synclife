class ShoppingListError(Exception):
    def __init__(self, error_message: str):
        super().__init__(f"Error de Shopping List: {error_message}")
