from src.api.v1.shopping_list.application.delete.delete_dto import DeleteDto
from src.api.v1.shopping_list.domain.entities.shopping_list import ShoppingList
from src.api.v1.shopping_list.domain.errors import (
    ShoppingListError,
    ShoppingListValidationTypeError,
)
from src.api.v1.shopping_list.domain.repositories.shopping_list_repository import ShoppingListRespository
from src.api.v1.shopping_list.domain.validators.shopping_list_repository_validator import (
    InventoryRepositoryValidator,
)
from src.api.v1.shared.domain.value_objects import Uuid


class DeleteItemUseCase:
    def __init__(self, repository: InventoryRepository):
        self.repository = repository

    def execute(self, dto: DeleteItemDTO) -> Inventory:
        # Valida que el inventario existe
        inventory_item = InventoryRepositoryValidator.inventory_found(
            self.repository.find_by_id(Uuid(dto.inventory_id))
        )
        # Valida que el usuario es propietario del inventario
        InventoryRepositoryValidator.user_owns_inventory(
            self.repository, inventory_item.user_id, Uuid(dto.inventory_id)
        )

        # Elimina (logicamente) el inventario
        is_deleted, deleted_item = self.repository.delete(inventory_item)

        if not is_deleted or deleted_item is None:
            raise InventoryItemError(InventoryItemTypeError.OPERATION_FAILED)

        return deleted_item
