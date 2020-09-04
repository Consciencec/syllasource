#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Consciencec'
SITENAME = 'Sylla Source'
SITESUBTITLE = 'A personal website and blog that no one reads.'
SITEURL = ''

PATH = 'content'
THEME = "../attila"
COLOR_SCHEME_CSS = 'tomorrow_night.css'
HEADER_COVER = 'static/header2.jpg'
SITE_LOGO = 'static/sylla_logo.png'

DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = False
TIMEZONE = 'US/Eastern'
DEFAULT_LANG = 'En'
DEFAULT_PAGINATION = 10

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Un-comment for custom side nav links
"""
MENUITEMS = (
    ('About', '/pages/about.html'),
    ('Blog', '/category/blog.html'),
    ('Email', 'http://www.google.com/recaptcha/mailhide/d?...'),
    ('Vita', '/pdfs/HouserCV.pdf')
)
"""

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# custom variables
PROFILE_HEADING = "What is SyllaSource?"

PROFILE_DESCRIPTION_1 = """Sylla Source is a mysterious website created out of boredom.
This website serves as a creative outlet to showcase ideas, projects and possibly music (pending)"""

PROFILE_DESCRIPTION_2 = "Feel free to checkout the articles below."
SELFIE = 'static/about.gif'
