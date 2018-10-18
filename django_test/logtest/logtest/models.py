# coding:utf-8
from django.db import models

class People(models.Model):
    "行业表"
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')