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

def ambil_satu(milestone_id):
   
    milestone = Milestone.query.filter(Milestone.milestone_id == milestone_id).one_or_none()
    if milestone is not None:
        milestone_schema = MilestoneSchema()
        data = milestone_schema.dump(milestone)
        return data
    else:
        abort(
            404,
            "Milestone tidak ditemukan dengan Id: {milestone_id}".format(milestone_id=milestone_id),
        )

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
        
def update_data(milestone_id, milestone):
    
    update_milestone = Milestone.query.filter(Milestone.milestone_id == milestone_id).one_or_none()
  
    milestone_title = milestone.get("milestone_title")
    milestone_description = milestone.get("milestone_description")
    milestone_priority = milestone.get("milestone_priority")
    milestone_status = milestone.get("milestone_status")

    existing_milestone = (
        Milestone.query.filter(Milestone.milestone_title == milestone_title).filter(Milestone.milestone_description == milestone_description)
        .one_or_none()
    )
    
    if update_milestone is None:
        abort(
            404,
            "Milestone tidak ditemukan dengan Id: {milestone_id}".format(milestone_id=milestone_id),
        )
   
    elif (
        existing_milestone is not None and existing_milestone.milestone_id != milestone_id
    ):
        abort(
            409,
            "Milestone yang berjudul {milestone_title} dengan deskripsi {milestone_description} datanya ada".format(
                milestone_title=milestone_title, milestone_description=milestone_description
            ),
        )

    else:
        schema = MilestoneSchema()
        update_milestone = Milestone( milestone_title=milestone_title, milestone_description=milestone_description, milestone_priority=milestone_priority, milestone_status=milestone_status, milestone_id=milestone_id)

        db.session.merge(update_milestone)
        db.session.commit()
        data = schema.dump(update_milestone)

        return data, 200


def hapus_data(milestone_id):
   
    milestone = Milestone.query.filter(Milestone.milestone_id == milestone_id).one_or_none()
    
    if milestone is not None:
        db.session.delete(milestone)
        db.session.commit()
        return make_response(
            "Milestone dengan id {milestone_id} sudah dihapus".format(milestone_id=milestone_id), 200
        )

    
    else:
        abort(
            404,
            "Milestone tidak ditemukan dengan Id: {milestone_id}".format(milestone_id=milestone_id),
        )
