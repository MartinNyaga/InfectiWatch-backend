"""removed unique constrains

Revision ID: 55e25246e466
Revises: 6ea798192fe1
Create Date: 2023-10-31 20:10:48.216409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55e25246e466'
down_revision = '6ea798192fe1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('locations', schema=None) as batch_op:
        batch_op.drop_index('ix_locations_name')
        batch_op.create_index(batch_op.f('ix_locations_name'), ['name'], unique=False)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('ix_users_username')
        batch_op.create_index(batch_op.f('ix_users_username'), ['username'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_username'))
        batch_op.create_index('ix_users_username', ['username'], unique=False)

    with op.batch_alter_table('locations', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_locations_name'))
        batch_op.create_index('ix_locations_name', ['name'], unique=False)

    # ### end Alembic commands ###
