"""Update table_2

Revision ID: a83424a76d74
Revises: 97aade999af0
Create Date: 2024-03-02 18:33:26.802272

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a83424a76d74'
down_revision: Union[str, None] = '97aade999af0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'full_name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'full_name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
