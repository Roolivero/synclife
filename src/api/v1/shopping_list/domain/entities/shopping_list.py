from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.shopping_list.domain.validators.shopping_list_validator import (
    ShoppingListValidator,
)


@dataclass
class ShoppingList:
    id: Uuid
    user_id: Uuid
    amount: int
    product_name: str
    is_deleted: bool
    created_at: datetime
    updated_at: Optional[datetime]

    def __post_init__(self) -> None:
        ShoppingListValidator.validate_all(
            amount=self.amount, product_name=self.product_name
        )

    def __repr__(self) -> str:
        return (
            f"<ShoppingList(id={self.id},"
            f"product_name={self.product_name},"
            f"amount={self.amount})>"
        )

    def __str__(self) -> str:
        return (
            f"ShoppingList(Product name: {self.product_name}, " f"Amount: {self.amount}"
        )
