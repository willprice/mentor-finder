from __future__ import print_function
from flask import Blueprint, render_template, request, flash

from mentor_finder.views.forms.mentor_signup import mentor_signup_form_factory




def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u'Error in the %s field - %s' % (getattr(form, field).label.text, error))

class MentorFinderViews(Blueprint):
    def __init__(self, mentor_finder):
        Blueprint.__init__(self, 'MentorFinderViews', __name__)
        self.mentor_finder = mentor_finder
        self.add_url_rules()

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
        MentorSignupForm = mentor_signup_form_factory(self._get_controller().faculty)

        form = MentorSignupForm()

        if request.method == 'POST':
            return self._get_controller() \
                .process_mentor_form(form, request.form,
                                     lambda mentor:
                                     self.mentor_listings(
                                         current=mentor),
                                     lambda : _mentor_signup(form))
        else:
            return _mentor_signup(form)


    def mentor_listings(self, current=None):
        return render_template('mentor_listings.html',
                               mentors=self._get_controller().faculty,
                               current=current)

    def activate_mentor(self, key):
        return self.mentor_listings()

    def _get_controller(self):
        return self.mentor_finder.controller

