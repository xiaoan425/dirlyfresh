#-*-coding:utf-8-*-
from django.db import models

class UserInfo(models.Model):
    uname = models.CharField(max_length=10)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=20)
    ureceiver = models.CharField(max_length=20,default='') #收件人
    uaddress = models.CharField(max_length=100,default='')
    upostcode = models.IntegerField(max_length= 6,null=True)# 邮编
    uphone = models.IntegerField(max_length=11,null=True)

