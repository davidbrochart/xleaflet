#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if on_rtd:
    subprocess.call('cd ..; doxygen', shell=True)

import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


def setup(app):
    app.add_javascript("https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js")
    app.add_javascript("https://unpkg.com/@jupyter-widgets/html-manager@*/dist/embed-amd.js")

    app.add_stylesheet("main_stylesheet.css")

extensions = ['breathe']
breathe_projects = { 'xleaflet': '../xml' }
templates_path = ['_templates']
html_static_path = ['_static']
source_suffix = '.rst'
master_doc = 'index'
project = 'xleaflet'
copyright = '2018, Johan Mabille, Sylvain Corlay, Wolf Vollprecht and Martin Renou'
author = 'Johan Mabille, Sylvain Corlay, Wolf Vollprecht and Martin Renou'

html_logo = 'quantstack-white.svg'

exclude_patterns = []
highlight_language = 'c++'
pygments_style = 'sphinx'
todo_include_todos = False
htmlhelp_basename = 'xleafletdoc'
