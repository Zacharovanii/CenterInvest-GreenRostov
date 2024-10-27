"""s commit

Revision ID: 2a78626c231e
Revises: 9510ff97921e
Create Date: 2024-10-26 15:47:06.837789

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '2a78626c231e'
down_revision: Union[str, None] = '9510ff97921e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('achivement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=320), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('description', sa.String(length=320), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('performers', sa.ARRAY(sa.Integer()), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role_name', sa.String(length=320), nullable=False),
    sa.Column('events_management', sa.Boolean(), nullable=False),
    sa.Column('events_parttake', sa.Boolean(), nullable=False),
    sa.Column('roles_edit', sa.Boolean(), nullable=False),
    sa.Column('users_block', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('status')
    op.drop_table('task')
    op.add_column('user', sa.Column('phone_number', sa.String(length=20), nullable=False))
    op.add_column('user', sa.Column('name', sa.String(length=320), nullable=False))
    op.add_column('user', sa.Column('lastname', sa.String(length=320), nullable=False))
    op.add_column('user', sa.Column('surname', sa.String(length=320), nullable=True))
    op.add_column('user', sa.Column('level', sa.Integer(), nullable=False))
    op.add_column('user', sa.Column('points', sa.Integer(), nullable=False))
    op.add_column('user', sa.Column('role_id', sa.Integer(), nullable=False))
    op.add_column('user', sa.Column('achievements', sa.ARRAY(sa.Integer()), nullable=True))
    op.add_column('user', sa.Column('events', sa.ARRAY(sa.Integer()), nullable=True))
    op.add_column('user', sa.Column('registered_at', sa.TIMESTAMP(), nullable=False))
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_phone_number'), 'user', ['phone_number'], unique=True)
    op.create_foreign_key(None, 'user', 'role', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_index(op.f('ix_user_phone_number'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_column('user', 'registered_at')
    op.drop_column('user', 'events')
    op.drop_column('user', 'achievements')
    op.drop_column('user', 'role_id')
    op.drop_column('user', 'points')
    op.drop_column('user', 'level')
    op.drop_column('user', 'surname')
    op.drop_column('user', 'lastname')
    op.drop_column('user', 'name')
    op.drop_column('user', 'phone_number')
    op.create_table('task',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('executor_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('performers', postgresql.ARRAY(sa.INTEGER()), autoincrement=False, nullable=False),
    sa.Column('status_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['status_id'], ['status.id'], name='task_status_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='task_pkey')
    )
    op.create_table('status',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('status_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='status_pkey')
    )
    op.drop_table('role')
    op.drop_table('event')
    op.drop_table('achivement')
    # ### end Alembic commands ###
