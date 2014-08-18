import wtforms_test


class FormTestCase(wtforms_test.FormTestCase):
    def assert_valid(self, data):
        self.form.process(**data)
        self.form.validate()
        for field_name, value in data.iteritems():
            msg = "Field '%s' with value '%s' was valid" % (field_name, value)
            assert field_name not in self.form.errors.keys(), msg

    def assert_invalid(self, data, invalid_field):
        self.form.process(**data)
        self.form.validate()
        msg = "Field '%s' with value '%s' was valid" % (invalid_field, self.form.__dict__[invalid_field].data)
        assert invalid_field in self.form.errors.keys(), msg
