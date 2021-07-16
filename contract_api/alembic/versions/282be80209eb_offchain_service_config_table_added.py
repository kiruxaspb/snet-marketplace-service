"""offchain_service_config_table_added

Revision ID: 282be80209eb
Revises: 6947016cfc24
Create Date: 2021-07-16 14:45:26.476557

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '282be80209eb'
down_revision = '6947016cfc24'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('offchain_service_config',
    sa.Column('row_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('org_id', sa.VARCHAR(length=128), nullable=False),
    sa.Column('service_id', sa.VARCHAR(length=128), nullable=False),
    sa.Column('demo_component_required', mysql.TINYINT(display_width=1), server_default='0', nullable=False),
    sa.Column('created_on', mysql.TIMESTAMP(), nullable=False),
    sa.Column('updated_on', mysql.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('row_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('offchain_service_config')
    # ### end Alembic commands ###
