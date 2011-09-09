# -*- coding: utf-8 -*-
# common.models

from google.appengine.ext import db

# Create your models here.

class User(db.Model):
    name = db.StringProperty()

class Schedule(db.Model):
    name = db.StringProperty()
    user = db.Reference(User)
    title = db.StringProperty()
    schedule_at = db.DateTimeProperty()
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)


class Log(db.Model):
    started_at = db.DateTimeProperty(auto_now_add=True)
    ended_at = db.DateTimeProperty(auto_now=True)