#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'André-Patrick Bubel'
SITENAME = "Moredread's blog"
SITEURL = 'http://127.0.0.1:8081'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PATH = 'blog'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

FEED_ALL_ATOM = 'atom.xml'
CATEGORY_FEED_ATOM = '%s.atom.xml'

FEED_ALL_RSS = 'rss.xml'
CATEGORY_FEED_RSS = '%s.rss.xml'

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

SOCIAL = (('feed', 'atom.xml', 'rss'),
          ('twitter', 'http://twitter.com/IndustrialRobot'),
          ('github', 'http://github.com/Moredread'),
         )

DIRECT_TEMPLATES = ['index', 'archives']

STATIC_PATHS = ['images', 'static']

THEME = "themes/pelican-bootstrap3"
BOOTSTRAP_THEME = "yeti"

DISPLAY_ARTICLE_INFO_ON_INDEX = True
#SHARIFF = True
#SHARIFF_SERVICES = ["facebook", "googleplus", "twitter"]
#SHARIFF_TWITTER_VIA = True

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n']
}

PLUGIN_PATHS = ['plugins']
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code',
           #'image_process',
           'tag_cloud',
           'i18n_subsites',
           'photos']

PHOTO_LIBRARY = "galleries"
PHOTO_EXIF_COPYRIGHT = 'CC-BY-NC-SA'
PHOTO_THUMB = PHOTO_ARTICLE = (760, 506, 80)
PHOTO_GALLERY = (4000, 4000, 95)
PHOTO_WATERMARK_TEXT = ""
PHOTO_RESIZE_JOBS = 5

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 20
TAG_CLOUD_SORTING = 'alphabetically'

#FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'
#SLUGIFY_SOURCE = 'basename'

#MENUITEMS = [
#                ("Archives", "archives.html"),
#            ]

DISPLAY_CATEGORIES_ON_MENU = False

YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
TAGS_SAVE_AS = 'tags.html'
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'archives']

#DISPLAY_TAGS_ON_SIDEBAR = False
#DISPLAY_TAGS_INLINE = True
CC_LICENSE = "CC-BY-NC-SA"

# IMAGE_PROCESS = {
#     'crisp': {'type': 'responsive-image',
#               'srcset': [('1x', ["scale_in 800 600 True"]),
#                          ('2x', ["scale_in 1600 1200 True"]),
#                          ('4x', ["scale_in 3200 2400 True"]),
#                          ],
#                'default': '1x',
#              },
#     }

DEFAULT_CATEGORY = "Blog"
DEFAULT_PAGINATION = 20

SUMMARY_MAX_LENGTH = None

#GITHUB_URL = "https://github.com/Moredread"
#TWITTER_USERNAME = "IndustrialRobot"
#DISQUS_SITENAME = "andre-bubel"
#PIWIK_URL = "piwik.nolife.de"
#PIWIK_SITE_ID = "1"

MATHJAX = True
TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Tell Pelican to add files from 'extra' to the output dir
STATIC_PATHS = [
    'extra'
]

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'}
}

CUSTOM_CSS = 'static/css/custom.css'
