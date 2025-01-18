from typing import Optional

from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.shopping_list.domain.entities.shopping_list import ShoppingList
from src.api.v1.shopping_list.domain.errors import (
    ShoppingListValidationError,
    ShoppingListValidationTypeError,
)
from src.api.v1.shopping_list.domain.repositories.shopping_list_repository import (
    ShoppingListRespository,
)


class ShoppingListRepositoryValidator:
    @staticmethod
    def shopping_list_found(
        shopping_list: Optional[ShoppingList],
    ) -> ShoppingList:
        if shopping_list is None:
            raise ShoppingListValidationError(
                ShoppingListValidationTypeError.ITEM_NOT_FOUND
            )
        return shopping_list

    @staticmethod
    def user_owns_inventory(
        repository: ShoppingListRespository,
        user_id: Uuid,
        shopping_list_id: Uuid,
    ) -> None:
        shopping_list = repository.find_by_id(shopping_list_id)
        if shopping_list is None or shopping_list.user_id != user_id:
            raise ShoppingListValidationError(
                ShoppingListValidationTypeError.ITEM_NOT_OWNED
            )
