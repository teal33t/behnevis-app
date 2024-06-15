"""empty message

Revision ID: 112be7cdca0c
Revises: daa6d71565e1
Create Date: 2024-06-15 13:05:37.257111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '112be7cdca0c'
down_revision = 'daa6d71565e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contents', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_input', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('system_title', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contents', schema=None) as batch_op:
        batch_op.drop_column('system_title')
        batch_op.drop_column('user_input')

    # ### end Alembic commands ###
