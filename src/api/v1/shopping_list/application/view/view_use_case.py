from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.shopping_list.application.view.view_dto import ViewDto
from src.api.v1.shopping_list.domain.entities.shopping_list import ShoppingList
from src.api.v1.shopping_list.domain.repositories.shopping_list_repository import (
    ShoppingListRespository,
)
from src.api.v1.shopping_list.domain.validators.shopping_list_repository_validator import (  # noqa: E501
    ShoppingListRepositoryValidator,
)


class ViewUseCase:
    def __init__(self, repository: ShoppingListRespository):
        self.repository = repository

    def execute(self, dto: ViewDto) -> ShoppingList:
        # Valida que la shopping list existe
        shopping_list_id = Uuid(dto.shopping_list_id)
        shopping_list_item = ShoppingListRepositoryValidator.shopping_list_found(
            self.repository.find_by_id(shopping_list_id)
        )
        return shopping_list_item
