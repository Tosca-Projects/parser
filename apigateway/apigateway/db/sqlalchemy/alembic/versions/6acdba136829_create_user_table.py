#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Create user table

Revision ID: 6acdba136829
Revises:
Create Date: 2017-01-22 9:18:09.967362

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '6acdba136829'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.String(255), nullable=False),
        sa.Column('name', sa.String(64), nullable=False, unique=True),
        sa.Column('email', sa.String(255))
    )


def downgrade():
    op.drop_table('user')
