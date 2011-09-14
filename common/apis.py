# -*- coding: utf-8 -*-
"""
common.apis
"""
from google.appengine.ext import blobstore
from werkzeug import redirect, Response
from kay.utils import url_for

def upload_url(request):
    # アップロード先のURL取得
    upload_url = '"%s"' % (blobstore.create_upload_url(url_for('common/upload')),)
    return Response(upload_url, content_type='application/json', status=200)