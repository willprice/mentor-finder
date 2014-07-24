# vim: set noexpandtab

TEMPLATES=$(wildcard ../../../../templates/*.html)

test: html_pages
	(cd .. && npm test);

html_pages: ${TEMPLATES}
	./gen_sample_site_pages.py


.PHONY: html_pages test
