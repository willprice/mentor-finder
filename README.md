# Mentor finder
[Example deploy (heroku)](http://mentor-finder.herokuapp.com/)

[![Stories in Done](https://badge.waffle.io/willprice/mentor-finder.png?label=done&title=Done)](http://waffle.io/willprice/mentor-finder)
[![Stories in Ready](https://badge.waffle.io/willprice/mentor-finder.png?label=ready&title=Ready)](http://waffle.io/willprice/mentor-finder)
[![Travis build status](https://travis-ci.org/willprice/mentor-finder.svg?branch=master)](https://travis-ci.org/willprice/mentor-finder)
[![Coverage Status](https://img.shields.io/coveralls/willprice/mentor-finder.svg)](https://coveralls.io/r/willprice/mentor-finder?branch=master)
[![Sauce Test Status](https://saucelabs.com/buildstatus/willprice94)](https://saucelabs.com/u/willprice94) [![Greenkeeper badge](https://badges.greenkeeper.io/willprice/mentor-finder.svg)](https://greenkeeper.io/)

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

MentorFinder is configured via environmental variables, 
create a file with these then source them before running
```sh
$ cat > configuration.sh <<EOF
# Export all of these
export APP_URL="http://localhost"
export APP_SECRET_KEY="lkasjasjdfiio234kjh2j2387dy72hg398"
export MAIL_HOST="smtp.gmail.com"
export MAIL_PORT=465
export MAIL_USERNAME="email@gmail.com"
export MAIL_PASSWORD="email_password"
export MAIL_TLS="ssl"
export MAIL_USE="smtp"
EOF
```
An example is provided in `example_env_vars` that you can copy and modify for
 your own use

Now you should be able to run the application with `./manage.py run`

If you'd like to run the tests then a simple `make test` will run the tests
throughout the application :)
