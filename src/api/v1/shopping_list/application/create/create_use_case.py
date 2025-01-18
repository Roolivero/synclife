from datetime import datetime

from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.shopping_list.application.create.create_dto import CreateDto
from src.api.v1.shopping_list.domain.entities.shopping_list import ShoppingList
from src.api.v1.shopping_list.domain.repositories.shopping_list_repository import (
    ShoppingListRespository,
)
from src.api.v1.user.domain.repositories import UserRepository
from src.api.v1.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)


class CreateUseCase:
    def __init__(
        self, repository: ShoppingListRespository, user_repository: UserRepository
    ):
        self.repository = repository
        self.user_repository = user_repository

    def execute(self, dto: CreateDto) -> ShoppingList:

        # Valida si el usuario existe
        UserRepositoryValidator.user_found(
            self.user_repository.find_by_id(Uuid(dto.user_id))
        )

        # Crear y guardar el inventario
        shopping_list_item = ShoppingList(
            id=Uuid(),
            user_id=Uuid(dto.user_id),
            product_name=str(dto.product_name),
            amount=int(dto.amount),
            is_deleted=False,
            created_at=datetime.now(),
            updated_at=None,
        )
        self.repository.save(shopping_list_item)
        return shopping_list_item
