__author__ = 'Nick'
from flask_wtf import Form
from wtforms import StringField, TextAreaField, SelectField, DecimalField
from wtforms.validators import DataRequired


class BeerForm(Form):
    name = StringField("name", validators=[DataRequired("Please provide a name for this beer")])
    description = TextAreaField("description")
    brewery = SelectField("brewery", choices=[], coerce=int, validators=[DataRequired('Please provide a brewery')])
    style = SelectField("style", choices=[], coerce=int, validators=[DataRequired('Please provide a beer style')])
    alcohol = DecimalField("alcohol")


class BreweryForm(Form):
    name = StringField("name", validators=[DataRequired("Please provide a name for this brewery")])
    description = TextAreaField("description")
    location = StringField("name", validators=[DataRequired("Please provide a location for this brewery")])
    size = SelectField("size", choices=[], coerce=int, validators=[DataRequired("Please provide the size of this brewery")])


class BrewerySizeForm(Form):
    label = StringField("label", validators=[DataRequired("Please provide a label for this brewery size")])
    description = TextAreaField("description")


class BeerStyleForm(Form):
    label = StringField("label", validators=[DataRequired("Please provide a label for this beer style")])
    description = TextAreaField("description")

