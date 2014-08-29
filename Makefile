# vim: set noexpandtab:
JS_DIR=mentor_finder/static/js/mentor_finder/


.PHONY: test
test: python_test

.PHONY: python_test
python_test:
	./manage.py test

.PHONY: install_deps
install_deps:
	pip install -r requirements.txt --download-cache "${HOME}/.pip-cache"

.PHONY: install_dev_deps
install_dev_deps: install_deps
	pip install coveralls

.PHONY: build
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

.PHONY: build_deb
build_deb: build
	fpm -s dir -t deb -n mentor-finder -v 0.1 -d "python" -d "python-dev" -C ./build \
		--prefix /home/mentor_finder mentor_finder

.PHONY: build_rpm
build_rpm: build
	fpm -s dir -t rpm -n mentor-finder -v 0.1 -d "python" -d "python-dev" -C ./build \
		--prefix /home/mentor_finder mentor_finder

.PHONY: build_all
build_all: build_rpm build_deb

.PHONY: clean_build
clean_build:
	-rm -rf ./build
	-rm mentor-finder*.deb
