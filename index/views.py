# -*- coding: utf-8 -*-
"""
index.views
"""
import logging

from google.appengine.api import taskqueue
from werkzeug import (
    redirect, Response
)
from kay.utils import (
    render_to_response, url_for
)
from common.models import User, Schedule

# Create your views here.

def index(request):
    user_count = User.all().count(999999)
    schedule_count = Schedule.all().count()
    return render_to_response('index/index.html', {
        'user_count': user_count,
        'schedule_count': schedule_count,
    })

def generate_user(request):
    if request.method == 'POST':
        # 量
        quantity = request.values.get('quantity', 100)
        # task queueに追加
        params = {'quantity': quantity}
        taskqueue.add(url=url_for('index/task_generate_user'), params=params)

    return redirect(url_for('index/index'))
