# -*- coding: utf-8 -*-
from __future__ import absolute_import 
import time
from pitchersite.celery import app
@app.task
def add(x, y):
       time.sleep(10)
       return x + y

