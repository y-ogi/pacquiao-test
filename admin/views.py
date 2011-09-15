# -*- coding: utf-8 -*-
"""
admin.views
"""
import logging

from kay.utils import render_to_response
from kay.generics.crud import CRUDViewGroup


# Create your views here.
def index(request):
    return render_to_response('admin/index.html')

class AdminMailTemplateCRUDViewGroup(CRUDViewGroup):
    model = 'common.models.MailTemplate'
    form = 'admin.forms.AdminMailTemplateForm'