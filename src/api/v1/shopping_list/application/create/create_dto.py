from dataclasses import dataclass


@dataclass
class CreateDto:
    user_id: str
    product_name: str
    amount: int
