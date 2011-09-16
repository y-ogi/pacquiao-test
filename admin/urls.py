# -*- coding: utf-8 -*-
# admin.urls
# 

# Following few lines is an example urlmapping with an older interface.

from kay.routing import (
  ViewGroup, Rule
)
from admin.views import (
    AdminUserCRUDViewGroup,
    AdminMailTemplateCRUDViewGroup,
)

view_groups = [
    ViewGroup(
        Rule('/', endpoint='index', view='admin.views.index'),
    ),
    AdminUserCRUDViewGroup(),
    AdminMailTemplateCRUDViewGroup(),
]

