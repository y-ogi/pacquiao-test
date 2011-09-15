# -*- coding: utf-8 -*-
# common.urls
# 

# Following few lines is an example urlmapping with an older interface.
from kay.routing import (
  ViewGroup, Rule
)
from views import ServeHandler, UploadHandler

view_groups = [
    ViewGroup(
        Rule('/', endpoint='index', view='common.views.index'),
        Rule('/file_info/<string:resource>', endpoint='file_info', view='common.views.file_info'),
        Rule('/upload', endpoint='upload', view=UploadHandler()),
        Rule('/upload_url', endpoint='upload_url', view='common.apis.upload_url'),
        Rule('/serve/<string:resource>', endpoint='serve', view=ServeHandler()),
        Rule('/mail_info/<string:key>', endpoint='mail_info', view='common.apis.mail_info'),
    )
]

