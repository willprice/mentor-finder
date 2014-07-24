from flask import Blueprint, render_template, request, flash
from mentor_finder import controller
from mentor_finder.models.errors import MentorAlreadyExistsError
from mentor_finder.models.forms.mentor_signup import mentor_signup_form_factory

mod = Blueprint('general', __name__)
MentorSignupForm = mentor_signup_form_factory(controller.faculty)



def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u'Error in the %s field - %s' % (
                getattr(form, field).label.text,
                error
                                                  ))
@mod.route('/')
def landing_page():
    return render_template('landing_page.html')


@mod.route('/mentor_signup', methods=('GET', 'POST'))
def mentor_signup(**kwargs):
    form = MentorSignupForm()
    if form.validate_on_submit():
        try:
            controller.add_mentor(request.form)
        except MentorAlreadyExistsError:
            return render_template('mentor_signup.html', form=form,
                                   error=u'Email address already in use')
        else:
            return mentor_listings()
    return render_template('mentor_signup.html', form=form, **kwargs)


@mod.route('/mentor_listings')
def mentor_listings():
    return render_template('mentor_listings.html', mentors=controller.faculty)


@mod.route('/addmentor', methods=['POST'])
def add_mentor():
    try:
        controller.add_mentor(request.form)
    except MentorAlreadyExistsError:
        return mentor_signup(error=u'Email address already in use')
    else:
        return mentor_listings()
