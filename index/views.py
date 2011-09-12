# -*- coding: utf-8 -*-
"""
index.views
"""
import logging

from google.appengine.api import taskqueue
from google.appengine.ext import db

from werkzeug import (
    redirect, Response
)
from kay.utils import (
    render_to_response, url_for
)
from common.models import (
    User, Schedule, Log
)

# Create your views here.

def index(request):
    user_count = User.all().count(999999)
    schedule_count = Schedule.all().count(999999)
    log_count = Log.all().count(999999)
    return render_to_response('index/index.html', {
        'user_count': user_count,
        'schedule_count': schedule_count,
        'log_count': log_count,
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