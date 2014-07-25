# vim: set noexpandtab:
JS_DIR=mentor_finder/static/js/mentor_finder/


test: python-test js-test

python-test:
	nosetests

js-test:
	$(MAKE) -C $(JS_DIR) test

install_dependencies:
	pip install -r requirements.txt
	$(MAKE) -C $(JS_DIR) install_dependencies


.PHONY: test python-test js-test install_dependencies
