from django.db import models
import datetime
from django.utils import timezone

class Daodej(models.Model):
    banben=models.IntegerField(default=0)
    zhangjie=models.IntegerField()
    zhangming=models.CharField(max_length=50)
    jingwen=models.CharField(max_length=500)
    def __str__(self):
        return self.zhangming

