# -*- coding: utf-8 -*-
"""
admin.forms
"""

from common.models import MailTemplate
from kay.utils.forms.modelform import ModelForm

class AdminMailTemplateForm(ModelForm):
    class Meta:
        model = MailTemplate