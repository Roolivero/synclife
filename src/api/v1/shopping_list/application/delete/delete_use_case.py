from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.shopping_list.application.delete.delete_dto import DeleteDto
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


class DeleteUseCase:
    def __init__(self, repository: ShoppingListRespository):
        self.repository = repository

    def execute(self, dto: DeleteDto) -> ShoppingList:
        # Valida si la Shopping List existe
        shopping_list = ShoppingListRepositoryValidator.shopping_list_found(
            self.repository.find_by_id(Uuid(dto.shopping_list_id))
        )
        # Valida que el usuario es propietario de la shopping list
        ShoppingListRepositoryValidator.user_owns_inventory(
            self.repository, shopping_list.user_id, Uuid(dto.shopping_list_id)
        )
        # Elimina (logicamente) la shopping list
        is_deleted, deleted_item = self.repository.delete(shopping_list)

        if not is_deleted or deleted_item is None:
            raise ShoppingListValidationError(
                ShoppingListValidationTypeError.OPERATION_FAILED
            )

        return deleted_item
