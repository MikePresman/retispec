from flask import Blueprint, make_response, render_template, redirect, url_for, request
from ..forms import PatientForm, UpdatePatientForm
from ..models import Patient
from random import randint
from ..models import db 
acquisition_blueprint = Blueprint('acquisition_blueprint', __name__)

@acquisition_blueprint.route("/acquisitions")
def acquisitions():
    pass

