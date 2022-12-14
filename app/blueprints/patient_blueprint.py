from flask import Blueprint, make_response, render_template, redirect, url_for, request
from ..forms import PatientForm, UpdatePatientForm
from ..models import Patient
from random import randint
from ..models import db 
patient_blueprint = Blueprint('patient_blueprint', __name__)

new.route("/")
def index():
    return redirect(url_for('patient_blueprint.patients'))

new.route("/patients", methods=["GET"])
def patients():
    patients = Patient.query.all()
    return render_template('patients.html', patients = patients)

new.route("/patients/new", methods=["GET", "POST"])
def form_create_patient():
    if request.method == "POST":
        req = request.form
        new_patient = Patient(firstname = req["firstname"],
                                    lastname = req["lastname"],
                                    date_of_birth = req["date_of_birth"],
                                    sex = req["sex"],
                                    image_id = randint(1, 90),
                                    status = "New")
        db.session.add(new_patient)
        db.session.commit()
        return redirect(url_for('patient_blueprint.patients'))
    form = PatientForm()
    return render_template('new_patient_form.html', form=form)

new.route("/patients/:id", methods=["GET"])
def get_patient(id):
    pass

new.route("/patients/<id>", methods=["GET"])
def delete_patient(id):
    patient = Patient.query.get(id)
    db.session.delete(patient)
    db.session.commit()
    return redirect(url_for('patient_blueprint.patients'))

new.route("/update_patients/<id>", methods=["GET", "POST"])
def update_patient(id):
    patient = Patient.query.get(id)
    if request.method == "POST":
        req = request.form
        print(req)
        patient.firstname = req["firstname"]
        patient.lastname = req["lastname"]
        patient.date_of_birth = req["date_of_birth"]
        patient.sex = req["sex"]
        db.session.commit()
        return redirect(url_for('patient_blueprint.patients'))

    form = UpdatePatientForm(obj=patient)
    return render_template('new_patient_form.html', form=form)
