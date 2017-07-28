"""empty message

Revision ID: 355a8f844fb8
Revises: eadf6d98df7c
Create Date: 2017-07-27 06:01:22.980821

"""

# revision identifiers, used by Alembic.
revision = '355a8f844fb8'
down_revision = 'eadf6d98df7c'

from alembic import op
import sqlalchemy as sa
import citext
from sqlalchemy.dialects import postgresql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('art_file', sa.Column('state', postgresql.ENUM('new', 'fetching', 'processing', 'complete', 'error', 'removed', 'disabled', 'specialty_deferred', 'specialty_ready', 'not_set', name='dlstate_enum'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('art_file', 'state')
    # ### end Alembic commands ###