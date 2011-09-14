# -*- coding: utf-8 -*-
"""
common.views
"""
import logging
from google.appengine.ext import blobstore
from kay.handlers import blobstore_handlers
from kay.utils import render_to_response, url_for
from werkzeug import redirect, Response
from common.utils import dict_to_response
# Create your views here.

def index(request):
    return render_to_response('common/index.html', {'message': 'Hello'})

def file_info(request, resource):
    blob_info = blobstore.BlobInfo.get(resource)
    dct = [{
            'filename': blob_info.filename, 
            'name': blob_info.filename, 
            'size': blob_info.size, 
            'resource': resource,
            'url': url_for('common/serve', resource=resource),
            },]
    return dict_to_response(request, dct)

class ServeHandler(blobstore_handlers.BlobstoreDownloadHandler):
    
    def get(self, resource):
        import urllib
        resource = str(urllib.unquote(resource))
        blob_info = blobstore.BlobInfo.get(resource)
        return self.send_blob(blob_info, content_type=blob_info.content_type)

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    
    def post(self):
        # ファイル取得
        files = self.get_uploads('files')
        blob_info = files[0]
        next = self.request.values.get('next', url_for('common/file_info', resource=blob_info.key()))
        
        # Entitiyにblob_info.key()を保存する処理を入れる場合は
        # この辺に書くこと。

        headers = dict(Location=next)
        return Response(None, headers=headers, status=302)    
