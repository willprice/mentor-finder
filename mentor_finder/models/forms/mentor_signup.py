import flask_wtf
import wtforms
from wtforms_html5 import DateField, EmailField, URLField
from wtforms import PasswordField, SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired, Regexp, Optional, EqualTo
from mentor_finder.models.county import get_counties
from mentor_finder.models.forms.validators import DuplicateAccount



def mentor_signup_form_factory(faculty, test=False):
    Form = flask_wtf.Form
    if test:
        Form = wtforms.Form

    class MentorSignupForm(Form):
        first_name = StringField(u'First name*',
                                 validators=[DataRequired(),
                                             Regexp(r'^[a-zA-Z]+$', message=u'Must be alphanumeric')])
        last_name = StringField(u'Last name*',
                                validators=[DataRequired()])
        county = SelectField(u'County*',
                             validators=[DataRequired()], choices=get_counties())
        email = EmailField(u'Email address*',
                            validators=[DataRequired(), DuplicateAccount(faculty)])
        password = PasswordField(u'Password*',
                                 validators=[DataRequired(),
                                             EqualTo('password_confirmation',
                                                     message=u'Passwords must match')])
        password_confirmation = PasswordField(u'Password confirmation*',
                                              validators=[DataRequired()])
        date_of_birth = DateField(u'Date of birth*',
                                  validators=[DataRequired()])
        description = TextAreaField(u'Description*',
                                    validators=[DataRequired()])
        keywords = StringField(u'Keywords',
                               validators=[Optional()])
        personal_site = URLField(u'Personal Site',
                                 validators=[Optional()])
        twitter_id = StringField(u'Twitter ID',
                                 validators=[Optional()])
        linkedin = URLField(u'Linkedin URL',
                            validators=[Optional()])
        github_id = StringField(u'Github ID',
                                validators=[Optional()])

    return MentorSignupForm
