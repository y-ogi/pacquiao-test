# -*- coding: utf-8 -*-
"""
index.views
"""
from common.models import User, Schedule, Process, Log
from google.appengine.api import taskqueue
from google.appengine.ext import db
from kay.utils import render_to_response, url_for
from werkzeug import redirect, Response
import logging
from werkzeug.exceptions import BadRequest



# Create your views here.

def index(request):
    user_count = User.all().count(999999)
    schedule_count = Schedule.all().count(999999)
    log_count = Log.all().count(999999)
    processes = Process.all().order('-created_at').fetch(1)
    process = processes[0] if len(processes) > 0 else None
    return render_to_response('index/index.html', {
        'user_count': user_count,
        'schedule_count': schedule_count,
        'log_count': log_count,
        'process': process,
    })

def file_upload(request):
    return render_to_response('index/file_upload.html', {
    })
    
def file_upload2(request):
    return render_to_response('index/file_upload2.html', {
    })

def generate_users(request):
    if request.method == 'POST':
        # 量
        quantity = request.values.get('quantity', 100)
        # task queueに追加
        params = {'quantity': quantity}
        taskqueue.add(url=url_for('index/task_generate_users'), params=params)

    return redirect(url_for('index/index'))

def delete_all_users(request):
    if request.method == 'POST':
        params = {}
        taskqueue.add(url=url_for('index/task_delete_all_users'), params=params)
    return redirect(url_for('index/index'))

def generate_schedules(request):
    if request.method == 'POST':
        # task queueに追加
        params = {}
        taskqueue.add(url=url_for('index/task_generate_schedules'), params=params)
        
    return redirect(url_for('index/index'))

def delete_all_schedules(request):
    if request.method == 'POST':
        params = {}
        taskqueue.add(url=url_for('index/task_delete_all_schedules'), params=params)
    return redirect(url_for('index/index'))

def delete_all_logs(request):
    if request.method == 'POST':
        params = {}
        taskqueue.add(url=url_for('index/task_delete_all_logs'), params=params)
    return redirect(url_for('index/index'))

def summary_daily_schedules(request):
    if request.method == 'POST':
        # 対象日付取得　
        date = request.values.get('date')
        if not date:
            raise BadRequest
        name = 'summary_daily_schedules'
        params = {'date':date, 'name':name}
        taskqueue.add(url=url_for('index/task_summary_daily_schedules'), params=params)
    return redirect(url_for('index/index'))
        