from flask import Flask, render_template, request


app = Flask("Mentor finder")


@app.route('/')
def landing_page():
    return render_template('landing_page.html')


@app.route('/mentor_signup')
def mentor_signup():
    return render_template('mentor_signup.html')


@app.route('/mentor_listings')
def mentor_listings():
    return render_template('mentor_listings.html')


@app.route('/addmentor', methods=['POST'])
def add_mentor():
    print request.form
    return mentor_listings()


if __name__ == '__main__':
    app.debug = True
    app.run()
