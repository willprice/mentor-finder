from flask import Blueprint, render_template, request, flash
from mentor_finder import controller
from mentor_finder.models.errors import MentorAlreadyExistsError

mod = Blueprint('general', __name__)


@mod.route('/')
def landing_page():
    return render_template('landing_page.html')


@mod.route('/mentor_signup')
def mentor_signup(**kwargs):
    return render_template('mentor_signup.html', **kwargs)


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
