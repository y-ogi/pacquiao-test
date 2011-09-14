# -*- coding: utf-8 -*-
import string
import random
import datetime
try:
    import simlejson
except ImportError:
    from google.appengine.dist import use_library
    use_library('django', '1.2')
    from django.utils import simplejson
from werkzeug import Response

def generate_string(length=10):
    ret = ''
    for i in range(0, length):
        ret = ret + random.choice(string.lowercase)
    return ret

def dict_to_response(request, dct, *args, **kwargs):
    """
    ディクショナリをJSONに変換して返却を行う
    """
    format = request.values.get('format', 'json')
    if format == 'json':
        dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None
        kwargs.update({'content_type':'text/javascript+json; charset=utf-8'})
        return Response(simplejson.dumps(dct, default=dthandler), *args, **kwargs)
    else:
        return Response(dct, *args, **kwargs)