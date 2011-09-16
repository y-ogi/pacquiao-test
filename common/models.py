# -*- coding: utf-8 -*-
# common.models
import logging
from datetime import (
    datetime, timedelta
)

from google.appengine.api import taskqueue
from google.appengine.ext import db
from kay.utils import url_for
# Create your models here.

class User(db.Model):
    name = db.StringProperty(required=True)
    shift = db.IntegerProperty(required=True)

    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)
   
    searchable_prop = 'name'
    
    def __unicode__(self):
        return 'user/%s' % self.name
    
    def put(self):
        db.put(self)
        # indexing
        params = {'key':self.key()}
        taskqueue.add(url=url_for('common/indexing'), params=params)

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
    
class MailTemplate(db.Model):    
    name = db.StringProperty(required=True)
    subject = db.StringProperty(required=True)
    body = db.TextProperty(required=True)
    
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)

    def __unicode__(self):
        return 'mail_template/%s' % self.name
    
class InvertedNameIndex(db.Model):
    """
    転置Index
    名前用の転置Index
    """
    word = db.StringProperty(required=True)
    keys = db.StringListProperty()
    
    key_template = 'inverted_name_index/%s/%s'
    
    @classmethod
    def add(cls, word, key, count=0):
        key_name = cls.key_template % (count, word, )
        index = cls.get_by_key_name(key_name)
        if not index:
            index = InvertedNameIndex(word=word, key_name=key_name)
        if len(index.keys) > 1000:
            cls.add(cls, word, key, count + 1)
            return
            
        # 追加
        if not key in index.keys:
            index.keys.append(key)
        index.put()
        
    @classmethod
    def indexing(cls, key):
        """
        転置Indexの生成を行う
        今は、名前を想定しているために、以下の様に区切り、それぞれのIndexとする。
        例：
        　豊臣秀吉
        　-> /豊/豊臣/豊臣秀/豊臣秀吉/
        
        名前と名字で区切りたかったりした場合は、Unigramを使う必要があるかも。
        要件に合わせて、Indexの生成方法を変える必要がある。
        """
        model = db.get(key)
        try:
            getattr(model, 'searchable_prop')
        except:
            pass
        else:
            value = getattr(model, model.searchable_prop)
            if value:
                words = [value[0:i + 1] for i in range(0, len(value))]
                for word in words:
                    cls.add(word, key)
                

    @classmethod
    def search(cls, word):
        models = []
        count = 0
        while True:
            key_name = cls.key_template % (count, word,)
            index = cls.get_by_key_name(key_name)
            if not index: break
            models = models + db.get(index.keys)
            count = count + 1
        return models     