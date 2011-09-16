'''
Created on 2011/09/16

@author: ogihara
'''

from werkzeug import redirect, Response
from common.models import InvertedNameIndex

def indexing(request):
    if request.method == 'POST':
        key = request.values.get('key')
        InvertedNameIndex.indexing(key)
    return Response(status=200)