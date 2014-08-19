from __future__ import print_function
from flask import Blueprint, render_template, request, flash

from mentor_finder.views.forms.mentor_signup import mentor_signup_form_factory


mod = Blueprint('general', __name__)


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
    controller = _get_controller()
    MentorSignupForm = mentor_signup_form_factory(controller.faculty)

    form = MentorSignupForm()

    if request.method == 'POST':
        return controller.process_mentor_form(form, request.form,
                                              lambda mentor: mentor_listings(current=mentor),
                                              lambda : _mentor_signup(form))
    else:
        return _mentor_signup(form)


@mod.route('/mentor_listings')
def mentor_listings(current=None):
    controller = _get_controller()
    return render_template('mentor_listings.html', mentors=controller.faculty, current=current)

@mod.route('/users/activate/<key>')
def activate_mentor(key):
    return mentor_listings()

def _get_controller():
    from mentor_finder import controller
    return controller
