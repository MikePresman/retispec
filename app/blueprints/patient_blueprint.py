from flask import Blueprint, make_response, render_template, redirect, url_for

patient_blueprint = Blueprint('patient_blueprint', __name__)

@patient_blueprint.route("/")
def index():
    return redirect(url_for('patient_blueprint.patients'))

@patient_blueprint.route("/patients", methods=["GET"])
def patients():
    return render_template('patients.html')

@patient_blueprint.route("/patients/new", methods=["GET"])
def form_create_patient():
    pass

@patient_blueprint.route("/patients", methods=["POST"])
def create_patient():
    pass

@patient_blueprint.route("/patients/:id", methods=["GET"])
def get_patient(id):
    pass

@patient_blueprint.route("/patients/:id", methods=["PATCH"])
def update_patient(id):
    pass
