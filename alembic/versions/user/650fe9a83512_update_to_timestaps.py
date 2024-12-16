"""Update to timestaps

Revision ID: 650fe9a83512
Revises: 2e71bd2e425d
Create Date: 2024-11-08 18:26:39.326089

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "650fe9a83512"
down_revision: Union[str, None] = "2e71bd2e425d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users",
        "created_at",
        existing_type=sa.DATE(),
        type_=sa.DateTime(),
        existing_nullable=False,
    )
    op.alter_column(
        "users",
        "updated_at",
        existing_type=sa.DATE(),
        type_=sa.DateTime(),
        existing_nullable=True,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users",
        "updated_at",
        existing_type=sa.DateTime(),
        type_=sa.DATE(),
        existing_nullable=True,
    )
    op.alter_column(
        "users",
        "created_at",
        existing_type=sa.DateTime(),
        type_=sa.DATE(),
        existing_nullable=False,
    )
    # ### end Alembic commands ###
