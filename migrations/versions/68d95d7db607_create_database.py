"""Create Database

Revision ID: 68d95d7db607
Revises: 
Create Date: 2024-07-03 21:43:59.033377

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '68d95d7db607'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('query',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('article',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('query_id', sa.Integer(), nullable=True),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('date_update', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['query_id'], ['query.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    op.drop_table('article')
    op.drop_table('query')
    # ### end Alembic commands ###
