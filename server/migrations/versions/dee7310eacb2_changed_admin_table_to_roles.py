"""changed admin table to roles

Revision ID: dee7310eacb2
Revises: 
Create Date: 2023-11-08 00:22:25.696292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dee7310eacb2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('diseases',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('disease_name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('symptoms', sa.Text(), nullable=True),
    sa.Column('prevention', sa.Text(), nullable=True),
    sa.Column('treatment', sa.Text(), nullable=True),
    sa.Column('num_of_cases', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('diseases', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_diseases_disease_name'), ['disease_name'], unique=False)

    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('coordinates', sa.String(), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('more_details', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('locations', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_locations_name'), ['name'], unique=False)

    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role_given', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('disease_locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.Column('disease_id', sa.Integer(), nullable=True),
    sa.Column('disease', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('cases', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['disease_id'], ['diseases.id'], ),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_users_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_users_username'), ['username'], unique=True)

    op.create_table('donations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('donor_user_id', sa.Integer(), nullable=False),
    sa.Column('recipient_location_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['donor_user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['recipient_location_id'], ['locations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('emergencies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('condition', sa.String(), nullable=True),
    sa.Column('sender_location', sa.String(), nullable=False),
    sa.Column('sender_user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['sender_location'], ['locations.id'], ),
    sa.ForeignKeyConstraint(['sender_user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.Column('review', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    op.drop_table('emergencies')
    op.drop_table('donations')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_username'))
        batch_op.drop_index(batch_op.f('ix_users_email'))

    op.drop_table('users')
    op.drop_table('disease_locations')
    op.drop_table('roles')
    with op.batch_alter_table('locations', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_locations_name'))

    op.drop_table('locations')
    with op.batch_alter_table('diseases', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_diseases_disease_name'))

    op.drop_table('diseases')
    # ### end Alembic commands ###