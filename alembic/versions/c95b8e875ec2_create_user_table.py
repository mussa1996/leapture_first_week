"""create user table

Revision ID: c95b8e875ec2
Revises: 
Create Date: 2022-02-16 19:34:13.822218

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c95b8e875ec2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('email', sa.String(50),unique=True), 
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
        
    )

def downgrade():
    pass

