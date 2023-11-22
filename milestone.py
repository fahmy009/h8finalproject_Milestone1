from flask import make_response, abort
from config import db
from models import Milestone, MilestoneSchema


def ambil_data():
    # membuat list dari milstone dan di urutkan berdasarkan prioritasnya
    milestone = Milestone.query.order_by(Milestone.milestone_priority).all()

    # serialisasi data untuk response
    milestone_schema = MilestoneSchema(many=True)
    data = milestone_schema.dump(milestone)
    return data


def tambah_data(milestone):
    milestone_title = milestone.get("milestone_title")
    milestone_description = milestone.get("milestone_description")
    milestone_priority = milestone.get("milestone_priority")
    milestone_status = milestone.get("milestone_status")

    existing_milestone = (
        Milestone.query.filter(Milestone.milestone_title == milestone_title)
        .filter(Milestone.milestone_title == milestone_title)
        .one_or_none()
    )

    if existing_milestone is None:
        schema = MilestoneSchema()
        new_milestone = Milestone(
            milestone_title=milestone_title,
            milestone_description=milestone_description,
            milestone_priority=milestone_priority,
            milestone_status=milestone_status,
        )

        db.session.add(new_milestone)
        db.session.commit()

        data = schema.dump(new_milestone)

        return data, 201

    else:
        abort(
            409,
            "Milestone {milestone_title} {milestone_description} {milestone_priority} {milestone_status}".format(
                milestone_title=milestone_title,
                milestone_description=milestone_description,
                milestone_priority=milestone_priority,
                milestone_status=milestone_status,
            ),
        )
