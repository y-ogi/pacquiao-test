# -*- coding: utf-8 -*-
"""
index.tasks
"""
from __future__ import with_statement
from common.models import User, Schedule, Process, Log
from common.utils import generate_string
from datetime import datetime, date, timedelta
from google.appengine.api import files
from google.appengine.ext import db
from werkzeug import Response
from werkzeug.exceptions import BadRequest
import logging
import random

# 実験的BlobStore書き込みようFileAPI


def generate_users(request):
    
    if request.method == 'POST':
        # 量を取得
        quantity = int(request.values.get('quantity', 100))
    
        # 開始
        log = Log()
        log.name = u"generate users:%d" % (quantity,)
        log.started_at = datetime.now()
            
        # ランダムに指定数分先生を作る
        users = []
        for i in range(0, quantity):
            user = User(name=generate_string(20), shift=random.choice([0,1,2,3,4,5,6,7,8,9,10,11,12,13]))
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
    
    
def delete_all_users(request):
    if request.method == 'POST':
        db.delete(User.all())
    return Response(status=200)

def generate_schedules(request):
    if request.method == 'POST':
        
        # 開始
        log = Log()
        log.name = u'generate schedules'
        log.started_at = datetime.now()
        
        # ユーザ全員を取得
        users = User.all().fetch(1000);
        
        # 日付を取得
        today = datetime.today()
        target_day = date(today.year, today.month + 1, 1)
        nn_month = date(today.year, today.month + 2, 1)
        
        # 1日ずつスケジュールを入れる
        schedules = []
        while target_day < nn_month:
            
            # 時間をずらす
            for hour in range(9, 24):
                # 分をずらす
                for minutes in [0, 30]:
                    # ユーザずつ
                    for user in users:
                        # シフト
                        # 0/1: 月曜休みAM/月曜休みPM
                        # 2/3: 火曜休みAM/火曜休みPM
                        weekday = target_day.weekday()
                        if user.shift == weekday * 2 or user.shift == weekday * 2 + 1:
                            continue
                        
                        # AM: 9 - 17
                        # PM: 15 - 23
                        if user.shift % 2 == 0 and hour > 18:
                            continue
                        if user.shift % 2 == 1 and hour < 15:
                            continue
                        
                        # スケジュール入れる
                        target_datetime = datetime(target_day.year, target_day.month, target_day.day, hour, minutes)
                        schedule = Schedule(name=generate_string(20),
                                            user=user,
                                            title=generate_string(100),
                                            schedule_at=target_datetime)
                        # リストに追加
                        schedules.append(schedule)
                        
            
            # 追加
            db.put(schedules)
            schedules = []
            # 1日追加
            target_day = target_day + timedelta(days=1)
        
        
        # 終了
        log.ended_at = datetime.now()
        log.put()
        
        return Response(status=200)

def delete_all_schedules(request):
    if request.method == 'POST':
        #db.delete(Schedule.all())
        while True:
            schedules = Schedule.all().fetch(100)
            if len(schedules) == 0: break
            db.delete(schedules)
    return Response(status=200)

def delete_all_logs(request):
    if request.method == 'POST':
        db.delete(Log.all())
    return Response(status=200)

def summary_daily_schedules(request):
    if request.method == 'POST':
        # プロセス名を取得
        process_name = request.values.get('name')
        process = Process(name=process_name, is_processed=False)
        process.put()
        
        # 対象日を取得
        target_date = request.values.get('date')
        if not target_date:
            raise BadRequest
        # 日付に変換
        date = datetime.strptime(target_date, '%Y%m%d')
        
        # 対象となるスケジュールを取得
        schedules = Schedule.schedules_from_date(date)
        logging.debug(schedules)
        
        # blobに書き込む
        file_name = files.blobstore.create(mime_type='application/octet-stream')
        with files.open(file_name, 'a') as f:
            for schedule in schedules:
                f.write('user:%s date:%s\n' % (schedule.user.name, schedule.schedule_at,))
        files.finalize(file_name)
        
        # blobキーを取得
        blob_key = files.blobstore.get_blob_key(file_name)
        process.content = str(blob_key)
        process.put()
        
    return Response(status=200)
    