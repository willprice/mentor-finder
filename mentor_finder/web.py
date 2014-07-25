from flask import flash


def flash_errors(form):
    if len(form.errors.items()) > 0:
        flash(u'Sorry, but there are some errors you need to correct before you can submit your registration',
              u'message')
    for field, errors in form.errors.items():
        for error in errors:
            flash(u'%s - %s' % (getattr(form, field).label.text.replace(u'*', u''), error), u'error')
