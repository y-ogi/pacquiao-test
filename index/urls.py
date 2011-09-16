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
        Rule('/summary_daily_schedules', endpoint='summary_daily_schedules', view='index.views.summary_daily_schedules'),
        Rule('/task/summary_daily_schedules', endpoint='task_summary_daily_schedules', view='index.tasks.summary_daily_schedules'),
        
        Rule('/file_upload', endpoint='file_upload', view='index.views.file_upload'),
        Rule('/file_upload2', endpoint='file_upload2', view='index.views.file_upload2'),
        
        Rule('/mail_send', endpoint='mail_send', view='index.views.mail_send'),
        
        Rule('/search', endpoint='search', view='index.views.search'),
    )
]

