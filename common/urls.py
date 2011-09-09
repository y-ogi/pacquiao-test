# -*- coding: utf-8 -*-
# common.urls
# 

# Following few lines is an example urlmapping with an older interface.
"""
from werkzeug.routing import EndpointPrefix, Rule

def make_rules():
  return [
    EndpointPrefix('common/', [
      Rule('/', endpoint='index'),
    ]),
  ]

all_views = {
  'common/index': 'common.views.index',
}
"""

from kay.routing import (
  ViewGroup, Rule
)

view_groups = [
  ViewGroup(
    Rule('/', endpoint='index', view='common.views.index'),
  )
]

