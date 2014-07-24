#!/usr/bin/env python2


from jinja2 import Template, FileSystemLoader, Environment
import glob
import os.path

env = Environment(loader=(FileSystemLoader('../../../../templates')))

for file in glob.glob('../../../../templates/*.html'):
    template_filename = os.path.basename(file)
    template = env.get_template(template_filename)
    with open("sample_pages/" + template_filename, "wb") as file:
        file.write(template.render())
