#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Author Name'
AUTHOR_DESC = 'Author description'
SITENAME = u'KalyanChakravarthy.net'
SITEURL = 'http://kalyanchakravarthy.net/blog'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
DEFAULT_PAGINATION = None 

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

OUTPUT_PATH = './relative/output/path'
THEME = 'jekyll'
PATH = 'content'

STATIC_PATHS = ('static',) # (os.walk('content/').next()[1])

TWITTER_URL = 'http://twitter.com/kalyan02'
GITHUB_URL = 'http://github.com/kalyan02'
AUTHOR_EMAIL = 'kalyan@kalyanchakravarthy.net'

# these are static links on the top
LINKS = (
      ('	home', SITEURL),
	  ('photos','http://blog.fuss.in'),
	  ('about','#footer')
	)

PORT = 8000
