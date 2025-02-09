"""empty message

Revision ID: 24c23c9197c9
Revises: abe0497758b8
Create Date: 2023-01-05 11:25:18.625903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24c23c9197c9'
down_revision = 'abe0497758b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('moon',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('size', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('moon')
    # ### end Alembic commands ###
