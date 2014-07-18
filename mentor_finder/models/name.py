class Name(object):
    def __init__(self, first_name, second_name):
        self._first_name = first_name
        self._second_name = second_name

    def __eq__(self, other):
        return self._first_name == other._first_name and \
               self._second_name == other._second_name

    def __str__(self):
        return self._first_name + " " + self._second_name