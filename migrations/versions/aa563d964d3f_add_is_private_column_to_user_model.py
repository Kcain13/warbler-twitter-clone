"""Add is_private column to user model

Revision ID: aa563d964d3f
Revises: 
Create Date: 2024-01-02 12:46:01.414804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa563d964d3f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_private', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_private')
    # ### end Alembic commands ###
