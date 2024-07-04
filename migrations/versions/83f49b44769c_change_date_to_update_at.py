"""change date to update_at

Revision ID: 83f49b44769c
Revises: c78c0a0472fa
Create Date: 2024-07-04 21:49:15.687635

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '83f49b44769c'
down_revision: Union[str, None] = 'c78c0a0472fa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
