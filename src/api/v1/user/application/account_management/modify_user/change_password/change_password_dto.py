from dataclasses import dataclass


@dataclass
class ChangePasswordDto:
    email: str
    new_password: str