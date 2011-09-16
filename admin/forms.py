# -*- coding: utf-8 -*-
"""
admin.forms
"""

from common.models import User, MailTemplate
from kay.utils.forms.modelform import ModelForm

class AdminUserForm(ModelForm):
    class Meta:
        model = User
        
class AdminMailTemplateForm(ModelForm):
    class Meta:
        model = MailTemplate