from datetime import datetime
from config import db, ma


class Milestone(db.Model):
    __tablename__ = "milestone"
    milestone_id = db.Column(db.Integer, primary_key=True)
    milestone_title = db.Column(db.String(32))
    milestone_description = db.Column(db.String(32))
    milestone_priority = db.Column(db.Integer, index=True)
    milestone_status = db.Column(db.String(32))
    milestone_timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class MilestoneSchema(ma.SQLAlchemyAutoSchema):
    class meta:
        model = Milestone
        sqla_session = db.session
