# -*- coding: utf-8 -*-
import string
import random

def generate_string(length=10):
    ret = ''
    for i in range(0, length):
        ret = ret + random.choice(string.lowercase)
    return ret