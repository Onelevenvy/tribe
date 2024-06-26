"""add uploads table

Revision ID: c3dc42618662
Revises: c1acf65d4731
Create Date: 2024-06-19 14:03:47.288367

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = 'c3dc42618662'
down_revision = 'c1acf65d4731'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('upload',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('path', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('memberuploadslink',
    sa.Column('member_id', sa.Integer(), nullable=False),
    sa.Column('upload_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['member_id'], ['member.id'], ),
    sa.ForeignKeyConstraint(['upload_id'], ['upload.id'], ),
    sa.PrimaryKeyConstraint('member_id', 'upload_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('memberuploadslink')
    op.drop_table('upload')
    # ### end Alembic commands ###