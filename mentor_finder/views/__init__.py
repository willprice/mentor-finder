from __future__ import print_function
import sys
from flask import Blueprint, render_template, request, flash

from mentor_finder import controller
from mentor_finder.models.errors import MentorAlreadyExistsError
from mentor_finder.views.forms.mentor_signup import mentor_signup_form_factory


mod = Blueprint('general', __name__)
MentorSignupForm = mentor_signup_form_factory(controller.faculty)



def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u'Error in the %s field - %s' % (getattr(form, field).label.text, error))

@mod.route('/')
def landing_page():
    return render_template('landing_page.html')


@mod.route('/mentor_signup', methods=('GET', 'POST'))
def mentor_signup(**kwargs):
    def _mentor_signup(form):
        return render_template('mentor_signup.html', form=form, **kwargs)

    form = MentorSignupForm()

    if request.method == 'POST':
        print(request.form, file=sys.stderr)
        return controller.process_mentor_form(form, request.form,
                                              lambda mentor: mentor_listings(current=mentor),
                                              lambda : _mentor_signup(form))
    else:
        return _mentor_signup(form)


@mod.route('/mentor_listings')
def mentor_listings(current=None):
    return render_template('mentor_listings.html', mentors=controller.faculty, current=current)
