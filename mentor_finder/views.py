from flask import Blueprint, render_template, request
from mentor_finder import controller

mod = Blueprint('general', __name__)


@mod.route('/')
def landing_page():
    return render_template('landing_page.html')


@mod.route('/mentor_signup')
def mentor_signup():
    return render_template('mentor_signup.html')


@mod.route('/mentor_listings')
def mentor_listings():
    return render_template('mentor_listings.html', mentors=controller.faculty)


@mod.route('/addmentor', methods=['POST'])
def add_mentor():
    controller.add_mentor(request.form)
    return mentor_listings()
