from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class SearchForm(FlaskForm):
	content = StringField('Search Articles', validators=[Required()])
	submit = SubmitField('Search')