from dataclasses import dataclass
from datetime import date

@dataclass
class CreateDto: 
    user_id: str
    product_name: str
    amount: int