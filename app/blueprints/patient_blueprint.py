from flask import Blueprint, make_response, render_template, redirect, url_for, request
from ..forms import PatientForm
from ..models import Patient
from random import randint
from ..models import db 
patient_blueprint = Blueprint('patient_blueprint', __name__)

@patient_blueprint.route("/")
def index():
    return redirect(url_for('patient_blueprint.patients'))

@patient_blueprint.route("/patients", methods=["GET"])
def patients():
    patients = Patient.query.all()
    return render_template('patients.html', patients = patients)

@patient_blueprint.route("/patients/new", methods=["GET", "POST"])
def form_create_patient():
    if request.method == "POST":
        req = request.form
        print(req)
        new_patient = Patient(firstname = req["firstname"],
                                    lastname = req["lastname"],
                                    date_of_birth = req["dob"],
                                    sex = req["sex"],
                                    image_id = randint(1, 90),
                                    status = "New"
                                    )
        db.session.add(new_patient)
        db.session.commit()
        return redirect(url_for('patient_blueprint.patients'))
    form = PatientForm()
    return render_template('new_patient_form.html', form=form)

@patient_blueprint.route("/patients/:id", methods=["GET"])
def get_patient(id):
    pass

@patient_blueprint.route("/patients/<id>", methods=["GET"])
def delete_patient(id):
    patient = Patient.query.get(id)
    db.session.delete(patient)
    db.session.commit()
    return redirect(url_for('patient_blueprint.patients'))

@patient_blueprint.route("/patients/:id", methods=["PATCH"])
def update_patient(id):
    pass
