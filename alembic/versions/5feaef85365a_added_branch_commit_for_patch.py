"""Added branch commit for patch

Revision ID: 5feaef85365a
Revises: c6fab014f70e
Create Date: 2024-08-12 22:03:25.028131

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '5feaef85365a'
down_revision: Union[str, None] = 'c6fab014f70e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project_patches', sa.Column('branch_commit', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project_patches', 'branch_commit')
    # ### end Alembic commands ###
