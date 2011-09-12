# -*- coding: utf-8 -*-
# index.urls
# 

from kay.routing import (
    ViewGroup, Rule
)

view_groups = [
    ViewGroup(
        Rule('/', endpoint='index', view='index.views.index'),
        Rule('/generate_users', endpoint='generate_users', view='index.views.generate_users'),
        Rule('/delete_all_users', endpoint='delete_all_users', view='index.views.delete_all_users'),
        Rule('/task/generate_users', endpoint='task_generate_users', view='index.tasks.generate_users'),
        Rule('/task/delete_all_users', endpoint='task_delete_all_users', view='index.tasks.delete_all_users'),
        Rule('/generate_schedules', endpoint='generate_schedules', view='index.views.generate_schedules'),
        Rule('/delete_all_schedules', endpoint='delete_all_schedules', view='index.views.delete_all_schedules'),
        Rule('/task/generate_schedules', endpoint='task_generate_schedules', view='index.tasks.generate_schedules'),
        Rule('/task/delete_all_schedules', endpoint='task_delete_all_schedules', view='index.tasks.delete_all_schedules'),
        Rule('/delete_all_logs', endpoint='delete_all_logs', view='index.views.delete_all_logs'),
        Rule('/task/delete_all_logs', endpoint='task_delete_all_logs', view='index.tasks.delete_all_logs'),
    )
]

