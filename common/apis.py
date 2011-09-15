# -*- coding: utf-8 -*-
"""
common.apis
"""
from google.appengine.ext import db
from google.appengine.ext import blobstore
from werkzeug import redirect, Response
from werkzeug.exceptions import BadRequest
from kay.utils import url_for
from common.utils import dict_to_response

def upload_url(request):
    # アップロード先のURL取得
    upload_url = '"%s"' % (blobstore.create_upload_url(url_for('common/upload')),)
    return Response(upload_url, content_type='application/json', status=200)

def mail_info(request, key):
    mail_template = db.get(key)
    dct = dict(name=mail_template.name,
               subject=mail_template.subject,
               body=mail_template.body)
    return dict_to_response(request, dct)