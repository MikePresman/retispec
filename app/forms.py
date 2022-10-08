from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

class PatientForm(FlaskForm):
    firstname = StringField('Firstname', validators=[DataRequired()])
    lastname = StringField('Lastname', validators=[DataRequired()])
    dob = StringField('Date of Birth', validators=[DataRequired()])
    sex = StringField('Sex', validators=[DataRequired()])
    submit = SubmitField('Create new Patient')

