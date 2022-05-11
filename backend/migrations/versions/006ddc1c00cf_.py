"""empty message

Revision ID: 006ddc1c00cf
Revises: 
Create Date: 2022-05-10 23:46:19.554745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '006ddc1c00cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('radtetime', sa.DateTime(), nullable=True),
    sa.Column('dev', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('picture',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('picUrl', sa.String(length=100), nullable=False),
    sa.Column('OCR_txt', sa.String(length=1000), nullable=True),
    sa.Column('author_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('picture')
    op.drop_table('user')
    # ### end Alembic commands ###
