"""empty message

Revision ID: 2afcf55e7188
Revises: dec6e094b69c
Create Date: 2020-03-24 14:34:44.173253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2afcf55e7188'
down_revision = 'dec6e094b69c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('socket_connections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('active', sa.Integer(), nullable=True),
    sa.Column('total', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_socket_connections'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('socket_connections')
    # ### end Alembic commands ###