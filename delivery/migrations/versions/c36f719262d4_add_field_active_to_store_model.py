"""add field active to Store model

Revision ID: c36f719262d4
Revises: 04712b3313a9
Create Date: 2022-12-29 02:34:02.926494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c36f719262d4'
down_revision = '04712b3313a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('store', schema=None) as batch_op:
        batch_op.add_column(sa.Column('active', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('store', schema=None) as batch_op:
        batch_op.drop_column('active')

    # ### end Alembic commands ###
