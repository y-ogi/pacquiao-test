# -*- coding: utf-8 -*-
# common.models

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


class Log(db.Model):
    name = db.StringProperty(required=False)
    started_at = db.DateTimeProperty(auto_now_add=True)
    ended_at = db.DateTimeProperty(auto_now=True)