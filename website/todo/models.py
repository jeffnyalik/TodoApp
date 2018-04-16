# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(default="some text")
    createdAt = models.DateTimeField(datetime.now(),blank=True, null=False)

    def __str__(self):
        return self.title
