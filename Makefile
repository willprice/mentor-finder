# vim: set noexpandtab:
JS_DIR=mentor_finder/static/js/mentor_finder/


test: python-test js-test

python-test:
	./manage.py test


js-test:
	$(MAKE) -C $(JS_DIR) test

install_deps:
	pip install -r requirements.txt --download-cache "${HOME}/.pip-cache"
	$(MAKE) -C $(JS_DIR) install_dependencies

install_dev_deps: install_deps
	pip install coveralls


.PHONY: test \
	python-test \
	js-test \
	functional-tests \
	unit-tests \
	install_dependencies
