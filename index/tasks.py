# -*- coding: utf-8 -*-
"""
index.tasks
"""
import logging
from datetime import datetime

from google.appengine.ext import db

from werkzeug import (
    Response
)
from common.utils import generate_string
from common.models import (
    User, Schedule, Log
)

def generate_user(request):
    
    if request.method == 'POST':
        # 量を取得
        quantity = int(request.values.get('quantity', 100))
    
        # 開始
        log = Log()
        log.started_at = datetime.now()
            
        # ランダムに指定数分先生を作る
        users = []
        for i in range(0, quantity):
            user = User(name=generate_string(20))
            users.append(user)
            # 何件ごとに書き込むか検討
            if i % 20 == 0:
                db.put(users)
                users = []
        if len(users) > 0:
            db.put(users)

        # 終了
        log.ended_at = datetime.now()
        log.put()
        
        return Response(status=200)
    
def generate_schedule(request):
    users = User.all().fetch(100, 0)
    