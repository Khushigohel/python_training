from alembic import op

# revision identifiers
revision = "bf3ea2b240cf"
down_revision = "6342e6583201"
branch_labels = None
depends_on = None


def upgrade():
    # Add new enum values
    op.execute("ALTER TYPE task_status ADD VALUE IF NOT EXISTS 'todo'")
    op.execute("ALTER TYPE task_status ADD VALUE IF NOT EXISTS 'processing'")


def downgrade():
    # PostgreSQL DOES NOT support removing enum values safely
    # So we keep downgrade empty on purpose
    pass
