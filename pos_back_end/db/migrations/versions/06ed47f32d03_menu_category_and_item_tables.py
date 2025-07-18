"""menu category and item tables

Revision ID: 06ed47f32d03
Revises: 705a00882347
Create Date: 2025-07-07 19:41:18.508680
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '06ed47f32d03'
down_revision: Union[str, Sequence[str], None] = '705a00882347'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Upgrade schema."""
    # Batch mode for admins table
    with op.batch_alter_table('admins') as batch_op:
        batch_op.create_unique_constraint('uq_admins_address_id', ['address_id'])
        batch_op.create_foreign_key(
            'fk_admins_address_id',
            'addresses',
            ['address_id'],
            ['id']
        )

    # Batch mode for restaurant table
    with op.batch_alter_table('restaurant') as batch_op:
        batch_op.add_column(sa.Column('address_id', sa.Integer(), nullable=True))
        batch_op.create_unique_constraint('uq_restaurants_address_id', ['address_id'])
        batch_op.create_foreign_key(
            'fk_restaurants_address_id',
            'addresses',
            ['address_id'],
            ['id']
        )

def downgrade() -> None:
    """Downgrade schema."""
    # Batch mode for restaurant table
    with op.batch_alter_table('restaurant') as batch_op:
        batch_op.drop_constraint('fk_restaurants_address_id', type_='foreignkey')
        batch_op.drop_constraint('uq_restaurants_address_id', type_='unique')
        batch_op.drop_column('address_id')

    # Batch mode for admins table
    with op.batch_alter_table('admins') as batch_op:
        batch_op.drop_constraint('fk_admins_address_id', type_='foreignkey')
        batch_op.drop_constraint('uq_admins_address_id', type_='unique')