#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'admin'
SITENAME = 'cftutorials.tech'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'https://getpelican.com/'),
)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "nest"

STATIC_PATHS = [
    "images"
]

NEST_HEADER_LOGO = "/images/logo.svg"
NEST_INDEX_HEADER_TITLE = "cftutorials.tech"
NEST_HEADER_IMAGES = []
