from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class MessageText(FlaskForm):
    message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')
