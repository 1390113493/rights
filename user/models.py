from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    auth = models.IntegerField('学生认证', default=0) # 为认证0， 已认证1
    openid = models.TextField('微信用户唯一标识')
    session_key = models.TextField('会话密钥')
    wechatname = models.CharField('微信用户名', max_length=30, null=True)
    student_id = models.CharField('学号', max_length=15, null=True)
    name = models.CharField('姓名', max_length=50, null=True)
    campus = models.CharField('校区', max_length=20, null=True)
    department = models.CharField('学院', max_length=25, null=True)
    major = models.CharField('专业', max_length=25, null=True)
    adminclass = models.CharField('班级', max_length=25, null=True)
    dormitory = models.CharField('宿舍', max_length=20, null=True)
    phone = models.CharField('手机号', max_length=15, null=True)
    qq = models.CharField('QQ号', max_length=15, null=True)
    nickname = models.CharField('昵称', max_length=50, default='Hfuter')
    headimg = models.CharField('头像', max_length=300, null=True)
    sign = models.CharField('个性签名', max_length=240, default='厚德、笃学、崇实、尚新')
    gender = models.CharField(max_length=2, null=True)
    birthday = models.CharField(max_length=15, null=True)