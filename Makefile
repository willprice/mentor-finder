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

build: clean_build
	mkdir build
	# Copy source, without tests
	cp -p --recursive mentor_finder build
	rm -rf build/mentor_finder/tests
	cp setup.py requirements.txt build/
	# Add a virtual environment
	virtualenv --python=python2 build/mentor_finder/virtualenv
	# Install the requirements
	./build/mentor_finder/virtualenv/bin/pip install -r ./build/requirements.txt
	# Install the mentor_finder package into the virtualenv
	./build/mentor_finder/virtualenv/bin/python ./build/setup.py install
	# Remove any *.pyc *.pyo files
	find build -iname '*.pyc' -o -iname '*.pyo' -exec rm {} +
	# Build a debian package
	fpm -s dir -t deb -n mentor-finder -v 0.1 -d "python" -d "python-dev" -C ./build \
		--prefix /home/mentor_finder mentor_finder

clean_build:
	-rm -rf ./build
	-rm mentor-finder*.deb

.PHONY: test \
	python-test \
	js-test \
	functional-tests \
	unit-tests \
	install_dependencies \
	build \
	clean_build
