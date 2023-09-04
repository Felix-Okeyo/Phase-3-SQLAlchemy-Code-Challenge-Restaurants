"""completed part with few methods yet to be completed, refactoring restaurant one to many yet to be done

Revision ID: 6cdb2ecbe48c
Revises: 
Create Date: 2023-09-04 15:47:38.970386

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6cdb2ecbe48c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
