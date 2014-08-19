class Name(object):
    def __init__(self, first_name, second_name):
        self._first = first_name
        self._second = second_name

    @property
    def first(self):
        return self._first

    @property
    def second(self):
        return self._second

    def __eq__(self, other):
        return self.first == other.first and \
               self.second == other.second

    def __str__(self):
        return self._first + " " + self._second
