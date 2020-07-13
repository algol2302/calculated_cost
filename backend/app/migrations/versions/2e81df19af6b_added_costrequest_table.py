"""Added CostRequest table

Revision ID: 2e81df19af6b
Revises: 
Create Date: 2020-07-12 15:33:22.713549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e81df19af6b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('costrequest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('cargo_type', sa.String(), nullable=True),
    sa.Column('declared_value', sa.Float(), nullable=True),
    sa.Column('calculated_value', sa.DECIMAL(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_costrequest_date'), 'costrequest', ['date'], unique=False)
    op.create_index(op.f('ix_costrequest_id'), 'costrequest', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_costrequest_id'), table_name='costrequest')
    op.drop_index(op.f('ix_costrequest_date'), table_name='costrequest')
    op.drop_table('costrequest')
    # ### end Alembic commands ###