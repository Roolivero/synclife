from dataclasses import dataclass


@dataclass
class UpdateDto:
    shopping_list_id: str
    product_name: str
    amount: int
