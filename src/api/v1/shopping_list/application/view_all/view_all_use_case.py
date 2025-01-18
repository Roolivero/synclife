from typing import List

from src.api.v1.shopping_list.application.view_all.view_all_dto import ViewAllDto
from src.api.v1.shopping_list.domain.entities.shopping_list import ShoppingList
from src.api.v1.shopping_list.domain.repositories.shopping_list_repository import (
    ShoppingListRespository,
)


class ViewAllUseCase:
    def __init__(self, repository: ShoppingListRespository):
        self.repository = repository

    def execute(self, dto: ViewAllDto) -> List[ShoppingList]:
        shopping_list = self.repository.find_all_by_user_id(dto.user_id)

        return shopping_list
