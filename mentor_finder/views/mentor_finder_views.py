from flask import Blueprint, render_template, request, session
from mentor_finder.views import mentor_signup_form_factory


class MentorFinderViews(Blueprint):
    def __init__(self, controller, static_files=False):
        Blueprint.__init__(self, 'MentorFinderViews', __name__)
        self.controller = controller
        self.add_url_rules()
        if static_files:
            self.add_static_files()

    def add_static_files(self):
        pass

    def add_url_rules(self):
        self.add_url_rule('/', 'landing_page', self.landing_page)
        self.add_url_rule('/mentor_signup', 'mentor_signup',
                          self.mentor_signup,
                          methods=('GET', 'POST'))
        self.add_url_rule('/mentor_listings', 'mentor_listing', self
                          .mentor_listings)
        self.add_url_rule('/users/activate/<key>', 'activate_mentor',
                          self.activate_mentor)

    def landing_page(self):
        return render_template('landing_page.html')


    def mentor_signup(self, **kwargs):
        def _mentor_signup(form):
            return render_template('mentor_signup.html', form=form, **kwargs)

        MentorSignupForm = mentor_signup_form_factory(
            self.controller.faculty)
        form = MentorSignupForm()

        if request.method == 'POST':
            mentor = self.controller \
                .process_mentor_form(form, request.form,
                                     lambda mentor: self.mentor_listings(
                                         current=mentor
                                     ),
                                     lambda: _mentor_signup(form))
            if mentor:
                session['username'] = mentor.email
                return self.mentor_listings()
            return _mentor_signup(form)

        else:
            return _mentor_signup(form)


    def mentor_listings(self, current=None):
        try:
            current = current or self.controller.faculty.get_mentor(
                session['username']
            )
        except KeyError:
            pass
        return render_template('mentor_listings.html',
                               mentors=self.controller.faculty,
                               current=current)

    def activate_mentor(self, key):
        self.controller.activate_mentor(key)
        return self.mentor_listings()
