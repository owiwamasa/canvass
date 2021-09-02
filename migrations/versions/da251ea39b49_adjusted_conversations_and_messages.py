"""adjusted conversations and messages

Revision ID: da251ea39b49
Revises: 440cd56f9e2d
Create Date: 2021-09-02 11:28:28.101319

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da251ea39b49'
down_revision = '440cd56f9e2d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('conversations', sa.Column('userId', sa.Integer(), nullable=False))
    op.add_column('conversations', sa.Column('artistId', sa.Integer(), nullable=False))
    op.drop_constraint('conversations_userInboxId_fkey', 'conversations', type_='foreignkey')
    op.drop_constraint('conversations_artistInboxId_fkey', 'conversations', type_='foreignkey')
    op.create_foreign_key(None, 'conversations', 'users', ['artistId'], ['id'])
    op.create_foreign_key(None, 'conversations', 'users', ['userId'], ['id'])
    op.drop_column('conversations', 'artistInboxId')
    op.drop_column('conversations', 'userInboxId')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('conversations', sa.Column('userInboxId', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('conversations', sa.Column('artistInboxId', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'conversations', type_='foreignkey')
    op.drop_constraint(None, 'conversations', type_='foreignkey')
    op.create_foreign_key('conversations_artistInboxId_fkey', 'conversations', 'inboxes', ['artistInboxId'], ['id'])
    op.create_foreign_key('conversations_userInboxId_fkey', 'conversations', 'inboxes', ['userInboxId'], ['id'])
    op.drop_column('conversations', 'artistId')
    op.drop_column('conversations', 'userId')
    # ### end Alembic commands ###
