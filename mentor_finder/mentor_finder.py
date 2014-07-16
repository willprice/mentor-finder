from flask import Flask, render_template, request
from flask import url_for
from models import Mentor
from datetime import date


app = Flask("Mentor finder")

@app.route('/')
def landing_page():
    return render_template('landing_page.html')


@app.route('/mentor_signup')
def mentor_signup():
    return render_template('mentor_signup.html')


@app.route('/mentor_listings')
def mentor_listings():
    return render_template('mentor_listings.html', mentors=mentors)



mentors = []
@app.route('/addmentor', methods=['POST'])
def add_mentor():
    global mentors
    mentor_dict = request.form.to_dict()
    mentor_dict['date_of_birth'] = date(1900,1,1)
    mentors.append(Mentor(mentor_dict))
    return mentor_listings()

def get_mentor(email):
    for mentor in mentors:
        if mentor.email == email:
            return mentor

def serve_static_files():
    url_for('static', filename='css/main.css')
    url_for('static', filename='css/normalize.css')

if __name__ == '__main__':
    app.debug = True
    app.run()

    if app.debug:
        serve_static_files()

