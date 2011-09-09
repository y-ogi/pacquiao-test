# -*- coding: utf-8 -*-
# index.urls
# 

from kay.routing import (
    ViewGroup, Rule
)

view_groups = [
    ViewGroup(
        Rule('/', endpoint='index', view='index.views.index'),
        Rule('/generate_user', endpoint='generate_user', view='index.views.generate_user'),
        Rule('/task/generate_user', endpoint='task_generate_user', view='index.tasks.generate_user'),
    )
]

