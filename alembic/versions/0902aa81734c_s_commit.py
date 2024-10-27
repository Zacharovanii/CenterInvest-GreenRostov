"""s commit

Revision ID: 0902aa81734c
Revises: 2749e42c1ac3
Create Date: 2024-10-27 09:48:26.231019

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0902aa81734c'
down_revision: Union[str, None] = '2749e42c1ac3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('achievement', sa.Column('description', sa.String(length=320), nullable=False))
    op.create_unique_constraint(None, 'achievement', ['name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'achievement', type_='unique')
    op.drop_column('achievement', 'description')
    # ### end Alembic commands ###