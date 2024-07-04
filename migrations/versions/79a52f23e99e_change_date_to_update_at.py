"""change date to update_at

Revision ID: 79a52f23e99e
Revises: 83f49b44769c
Create Date: 2024-07-04 22:05:14.838432

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '79a52f23e99e'
down_revision: Union[str, None] = '83f49b44769c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('update_at', sa.DateTime(), nullable=True))
    op.drop_column('article', 'date_update')
    op.add_column('query', sa.Column('update_at', sa.DateTime(), nullable=True))
    op.drop_column('query', 'date')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('query', sa.Column('date', sa.DATE(), autoincrement=False, nullable=True))
    op.drop_column('query', 'update_at')
    op.add_column('article', sa.Column('date_update', sa.DATE(), autoincrement=False, nullable=True))
    op.drop_column('article', 'update_at')
    # ### end Alembic commands ###
