from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import DataRequired


class EventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    date = DateField('Date', validators=[DataRequired()])
    time = TimeField('Time', format='%H:%M', validators=[DataRequired()])  # **{"placeholder": "HH:MM"}
    submit = SubmitField('Create')


