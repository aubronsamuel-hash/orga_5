from alembic import op
import sqlalchemy as sa

revision = '0001_planning'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'events',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('org_id', sa.Integer, nullable=False),
        sa.Column('project_id', sa.Integer, nullable=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('start_utc', sa.DateTime(timezone=True), nullable=False),
        sa.Column('end_utc', sa.DateTime(timezone=True), nullable=False),
        sa.Column('location', sa.String, nullable=True),
        sa.Column('notes', sa.Text, nullable=True),
        sa.Column('created_at_utc', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at_utc', sa.DateTime(timezone=True), nullable=False),
        sa.Index('ix_events_org_start', 'org_id', 'start_utc')
    )
    op.create_table(
        'assignments',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('event_id', sa.Integer, sa.ForeignKey('events.id'), nullable=False),
        sa.Column('person_id', sa.Integer, nullable=False),
        sa.Column('role', sa.String, nullable=False),
        sa.Column('status', sa.Enum('TENTATIVE','CONFIRMED','CANCELED', name='assignment_status'), nullable=False),
        sa.Column('created_at_utc', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at_utc', sa.DateTime(timezone=True), nullable=False),
        sa.Index('ix_assignments_event_id', 'event_id')
    )

def downgrade():
    op.drop_table('assignments')
    op.drop_table('events')
