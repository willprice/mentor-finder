# vim: set noexpandtab:
JS_DIR=mentor_finder/static/js/mentor_finder/


test: python-test js-test

python-test: unit-tests functional-tests

unit-tests:
	python manage.py unittest

functional-tests:
	python manage.py functionaltest

js-test:
	$(MAKE) -C $(JS_DIR) test

install_deps:
	pip install -r requirements.txt
	$(MAKE) -C $(JS_DIR) install_dependencies

install_dev_deps: install_deps
	pip install coveralls


.PHONY: test \
	python-test \
	js-test \
	functional-tests \
	unit-tests \
	install_dependencies
