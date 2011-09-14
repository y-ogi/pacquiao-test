# -*- coding: utf-8 -*-
"""
common.views
"""
import logging
from google.appengine.ext import blobstore

from kay.handlers import blobstore_handlers

from kay.utils import render_to_response, url_for


# Create your views here.

def index(request):
    return render_to_response('common/index.html', {'message': 'Hello'})

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
        next = self.request.values.get('next', url_for('index/index'))
        """
        # csrfオフの状態でフォームを生成
        form = FileUploadForm()
        form.csrf_protected = False
        next = None
        # Validate
        if form.validate(self.request.values):
            # モデルを非コミットでsave
            model = form.save(commit=False)
            # blobstoreのkeyをcontentに設定
            model.content = blob_info.key()
            model.save()
            # 次のURLを取得
            next = form['next']

        headers = dict(Location=next, blob_key=blob_info.key())
        return Response(None, headers=headers, status=302)    
        """
        headers = dict(Location=next, blob_key=blob_info.key())
        return Response(None, headers=headers, status=302)    