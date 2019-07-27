"""empty message

Revision ID: 563ced4cffe3
Revises: 
Create Date: 2019-07-27 16:02:43.615173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '563ced4cffe3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('site')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('site',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('owner', sa.VARCHAR(), nullable=True),
    sa.Column('online_users', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
