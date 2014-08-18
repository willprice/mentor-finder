# Mentor finder
[Example deploy (heroku)](http://mentor-finder.herokuapp.com/)

[![Stories in Done](https://badge.waffle.io/willprice/mentor-finder.png?label=done&title=Done)](http://waffle.io/willprice/mentor-finder)
[![Stories in Ready](https://badge.waffle.io/willprice/mentor-finder.png?label=ready&title=Ready)](http://waffle.io/willprice/mentor-finder)
[![Travis build status](https://travis-ci.org/willprice/mentor-finder.svg?branch=master)](https://travis-ci.org/willprice/mentor-finder)

A web application designed to connect prospective students to mentors. Mentors post their details for students, students
browse mentors to find one whose interests match theirs and contact them.

## Clone & Run
Requirements: `virtualenv`, `pip`

```
$ git clone http://github.com/willprice/mentor-finder
$ cd mentor-finder

$ virtualenv .virtualenv
$ source .virtualenv/bin/activate
$ pip install -r requirements.txt
```

Now you need to create a python module with the secret keys:
```sh
   # Still inside mentor-finder
$ mkdir mentor_finder/sensitive/
$ touch mentor_finder/sensitive/{__init__,passes}.py
$ cat > mentor_finder/sensitive/passes.py <<EOF
def add_sensitive_information_to_app(app):
    app.config.update(
        SECRET_KEY='super_secret_key',
        MAIL_USERNAME='example@gmail.com',
        MAIL_PASSWORD='example_password'
    )
EOF
```

Now you should be able to run the application with `./manage.py run`

If you'd like to run the tests then a simple `make test` will run the tests
throughout the application :)
