"""

Revision ID: 2b03271c952a
Revises: 5d6bad884aef
Create Date: 2024-08-23 21:44:04.900109

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b03271c952a'
down_revision: Union[str, None] = '5d6bad884aef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project_commits', sa.Column('committed_at', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project_commits', 'committed_at')
    # ### end Alembic commands ###
