# -*- coding: utf-8 -*-
# common.urls
# 

# Following few lines is an example urlmapping with an older interface.


from kay.routing import (
  ViewGroup, Rule
)
from views import ServeHandler

view_groups = [
  ViewGroup(
    Rule('/', endpoint='index', view='common.views.index'),
    Rule('/serve/<string:resource>', endpoint='serve', view=ServeHandler()),
  )
]

