# -*- coding: utf-8 -*-
"""
common.utils.mail
"""
import logging

from kay.conf import settings
from google.appengine.api import mail
from google.appengine.ext import db

def send_mail_with_template(to, template_key, **kw):
    """
    メールテンプレートを元にメール送信を行う
    """
    mail_template = db.get(template_key)
    # テンプレート適用
    from jinja2 import Template
    subject = Template(mail_template.subject).render(kw)
    body = Template(mail_template.body).render(kw)

    send_mail(settings.FROM_EMAIL_ADDR, to, subject, body)
    
    
def send_mail(sender, to, subject, body, **kw):
    """
    メール送信を行う
    """
    mail.send_mail(sender, to, subject, body)