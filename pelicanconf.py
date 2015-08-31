#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'André-Patrick Bubel'
SITENAME = "Moredread's blog"
SITEURL = ''

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

STATIC_PATHS = ['images', 'static']

PLUGIN_PATHS = ['plugins']
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'image_process']

IMAGE_PROCESS = {
    'crisp': {'type': 'responsive-image',
              'srcset': [('1x', ["scale_in 800 600 True"]),
                         ('2x', ["scale_in 1600 1200 True"]),
                         ('4x', ["scale_in 3200 2400 True"]),
                         ],
               'default': '1x',
             },
    }

DEFAULT_CATEGORY = "Blog"
DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
