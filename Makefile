# vim: set noexpandtab:
JS_DIR=mentor_finder/static/js/mentor_finder/


test: python-test js-test

python-test:
	-workon 'mentor_finder'
	nosetests

js-test:
	$(MAKE) -C $(JS_DIR) test


.PHONY: test python-test js-test
