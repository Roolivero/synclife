from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.shopping_list.application.update.update_dto import UpdateDto
from src.api.v1.shopping_list.domain.entities.shopping_list import ShoppingList
from src.api.v1.shopping_list.domain.errors import (
    ShoppingListValidationError,
    ShoppingListValidationTypeError,
)
from src.api.v1.shopping_list.domain.repositories.shopping_list_repository import (
    ShoppingListRespository,
)
from src.api.v1.shopping_list.domain.validators.shopping_list_repository_validator import (  # noqa: E501
    ShoppingListRepositoryValidator,
)


class UpdateUseCase:
    def __init__(self, repository: ShoppingListRespository) -> None:
        self.repository = repository

    # Valida si la shopping list existe
    def execute(self, dto: UpdateDto) -> ShoppingList:
        # Valida si la Shopping List existe
        shopping_list = ShoppingListRepositoryValidator.shopping_list_found(
            self.repository.find_by_id(Uuid(dto.shopping_list_id))
        )

        # Actualiza la shoppingList
        shopping_list.product_name = str(dto.product_name)
        shopping_list.amount = int(dto.amount)

        is_updated, updated_item = self.repository.update(shopping_list)

        if not is_updated or updated_item is None:
            raise ShoppingListValidationError(
                ShoppingListValidationTypeError.OPERATION_FAILED
            )

        return updated_item
