"""create JeroTest table

Revision ID: dde93c1a0b20
Revises: 
Create Date: 2025-02-17 16:27:57.439921

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dde93c1a0b20'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'jero_test',
        sa.Column('id', sa.Integer, autoincrement= True, primary_key=True),
        sa.Column('questions', sa.String(length=5000), nullable=True),
        sa.Column('responses', sa.String(length=5000), nullable=True),
    )
    pass


def downgrade() -> None:
    pass
