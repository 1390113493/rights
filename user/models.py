from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    auth = models.IntegerField(verbose_name='学生认证', default=0) # 为认证0， 已认证1
    openid = models.TextField(verbose_name='微信用户唯一标识')
    session_key = models.TextField(verbose_name='会话密钥')
    wechatname = models.CharField(verbose_name='微信用户名', max_length=30, null=True)
    student_id = models.CharField(verbose_name='学号', max_length=15, null=True)
    name = models.CharField(verbose_name='姓名', max_length=50, null=True)
    campus = models.CharField(verbose_name='校区', max_length=20, null=True)
    department = models.CharField(verbose_name='学院', max_length=25, null=True)
    major = models.CharField(verbose_name='专业', max_length=25, null=True)
    adminclass = models.CharField(verbose_name='班级', max_length=25, null=True)
    dormitory = models.CharField(verbose_name='宿舍', max_length=20, null=True)
    phone = models.CharField(verbose_name='手机号', max_length=15, null=True)
    qq = models.CharField(verbose_name='QQ号', max_length=15, null=True)
    nickname = models.CharField(verbose_name='昵称', max_length=50, default='Hfuter')
    headimg = models.CharField(verbose_name='头像', max_length=300, null=True)
    sign = models.CharField(verbose_name='个性签名', max_length=240, default='厚德、笃学、崇实、尚新')
    gender = models.CharField(max_length=2, null=True, verbose_name='性别')
    birthday = models.CharField(max_length=15, null=True, verbose_name='生日')