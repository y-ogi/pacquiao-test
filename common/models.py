# -*- coding: utf-8 -*-
# common.models
import logging
from datetime import (
    datetime, timedelta
)
from google.appengine.ext import db

# Create your models here.

class User(db.Model):
    name = db.StringProperty(required=True)
    shift = db.IntegerProperty(required=True)

class Schedule(db.Model):
    name = db.StringProperty(required=True)
    user = db.Reference(User)
    title = db.StringProperty(required=True)
    schedule_at = db.DateTimeProperty(required=True)
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)

    @classmethod
    def schedules_from_date(cls, date):
        min_date = datetime(date.year, date.month, date.day)
        max_date = min_date + timedelta(days=1)
        logging.debug('min_date:%s, max_date:%s' %(min_date, max_date,))
        query = Schedule.all().filter('schedule_at >=', min_date).filter('schedule_at <', max_date)
        # 1000件以上の場合はどうするのか
        # (23 - 09) * 50 = 700(1日単位でも超える可能性がある)
        return query.fetch(1000)

class Process(db.Model):
    name = db.StringProperty(required=True)
    is_processed = db.BooleanProperty(required=True)
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)
    content = db.StringProperty(required=False)

class Log(db.Model):
    name = db.StringProperty(required=False)
    started_at = db.DateTimeProperty(auto_now_add=True)
    ended_at = db.DateTimeProperty(auto_now=True)