"""empty message

Revision ID: 178b8c19804f
Revises: 
Create Date: 2020-12-20 06:09:23.375514

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '178b8c19804f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('communities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('userscount', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('interests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('first_name', sa.String(length=20), nullable=False),
    sa.Column('last_name', sa.String(length=20), nullable=False),
    sa.Column('password', postgresql.BYTEA(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('creator_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['creator_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('friendship',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('requester_id', sa.Integer(), nullable=True),
    sa.Column('target_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.Enum('requested', 'accepted', 'accepted_second_level', 'second_level', name='friendshipstatus'), nullable=True),
    sa.ForeignKeyConstraint(['requester_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['target_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users_interests',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('interests_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['interests_id'], ['interests.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'interests_id')
    )
    op.create_table('event_interests',
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('interests_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.ForeignKeyConstraint(['interests_id'], ['interests.id'], ),
    sa.PrimaryKeyConstraint('event_id', 'interests_id')
    )
    op.create_table('user_friendship',
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('friendship', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['friendship'], ['friendship.id'], ),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user', 'friendship')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_friendship')
    op.drop_table('event_interests')
    op.drop_table('users_interests')
    op.drop_table('friendship')
    op.drop_table('events')
    op.drop_table('user')
    op.drop_table('interests')
    op.drop_table('communities')
    # ### end Alembic commands ###
