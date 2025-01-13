from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from src.api.v1.shopping_list.domain.entities.shopping_list import ShoppingList
from src.api.v1.shared.domain.value_objects import Uuid

class ShoppingListRespository(ABC): 
    @abstractmethod
    def find_all(self) -> List[ShoppingList]:
        pass

    @abstractmethod
    def find_by_id(self, id: Uuid) -> Optional[ShoppingList]:
        pass

    @abstractmethod
    def find_all_by_user_id(
        self, id: Uuid, include_deleted: bool = False
    ) -> List[ShoppingList]:
        pass

    @abstractmethod
    def save(self, product: ShoppingList) -> bool:
        pass

    @abstractmethod
    def delete(self, product: ShoppingList) -> Tuple[bool, Optional[ShoppingList]]:
        pass

    @abstractmethod
    def update(self, product: ShoppingList) -> Tuple[bool, Optional[ShoppingList]]:
        pass
