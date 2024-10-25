"""first commit

Revision ID: d4970cbbca38
Revises: 43526599626c
Create Date: 2024-10-25 22:25:08.303509

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd4970cbbca38'
down_revision: Union[str, None] = '43526599626c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_role_id_fkey', 'user', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('user_role_id_fkey', 'user', 'role', ['role_id'], ['id'])
    # ### end Alembic commands ###
