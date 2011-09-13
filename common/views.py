# -*- coding: utf-8 -*-
"""
common.views
"""
import logging
from google.appengine.ext import blobstore

from kay.handlers import blobstore_handlers

from kay.utils import render_to_response


# Create your views here.

def index(request):
    return render_to_response('common/index.html', {'message': 'Hello'})

class ServeHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, resource):
        import urllib
        resource = str(urllib.unquote(resource))
        blob_info = blobstore.BlobInfo.get(resource)
        return self.send_blob(blob_info, content_type=blob_info.content_type)