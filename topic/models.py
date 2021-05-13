from django.db import models
from user.models import MyUser


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='分类名')
    needreply = models.IntegerField(default=0, verbose_name='需要系统回复')  # 是否需要系统回复，0为否，1为是

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '话题分类'
        verbose_name_plural = verbose_name


class Topic(models.Model):
    # uid = models.IntegerField(verbose_name='发表人')
    # pid = models.IntegerField(default=1, verbose_name='分类')
    pid = models.ForeignKey(to='Category', on_delete=models.Case, db_column='pid', related_name='pId', verbose_name='分类id')
    check = models.IntegerField(default=0, verbose_name='审核')  # 审核， -1为不通过，0为未申核，1为通过， 2为提交二审， 3为二审不通过， 4为二审通过
    name = models.CharField(max_length=100, verbose_name='要显示的名字')
    uid = models.ForeignKey(to='user.MyUser', on_delete=models.Case, db_column='uid', related_name='uid',
                            verbose_name='用户')
    headimg = models.CharField(max_length=300, verbose_name='要显示的头像')
    title = models.CharField(max_length=40, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    imgs = models.TextField(verbose_name='图片(以列表形式)')
    hide = models.IntegerField(default=0, verbose_name='是否匿名')  # 0为非匿名（默认）, 1为匿名
    top = models.IntegerField(default=0, verbose_name='是否置顶')  # 是否置顶，0为否
    # like = models.IntegerField(default=0, verbose_name='点赞数')  # 点赞数
    # dislike = models.IntegerField(default=0, verbose_name='倒赞数')  # 倒赞数
    visit = models.IntegerField(default=0, verbose_name='阅读数')  # 阅读数
    create_time = models.CharField(max_length=20, verbose_name='创建时间')
    user_delete = models.CharField(max_length=20, null=True, verbose_name='(自行)删除时间')
    system_delete = models.CharField(max_length=20, null=True, verbose_name='(系统)删除时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '话题内容'
        verbose_name_plural = verbose_name


class Comment(models.Model):
    uid = models.ForeignKey(to='user.MyUser', on_delete=models.Case, db_column='user', related_name='user')
    pid = models.IntegerField(default=1, verbose_name='回复话题')
    check = models.IntegerField(default=0, verbose_name='审核')  # 审核， -1为不通过，0为未申核，1为通过， 2为提交二审， 3为二审不通过， 4为二审通过
    content = models.TextField(verbose_name='回复内容')
    imgs = models.TextField(verbose_name='图片')
    like = models.IntegerField(default=0, verbose_name='点赞数')  # 点赞数
    create_time = models.CharField(max_length=20, verbose_name='回复时间')
    user_delete = models.CharField(max_length=20, null=True, verbose_name='(自行)删除时间')
    system_delete = models.CharField(max_length=20, null=True, verbose_name='(系统)删除时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '话题评论'
        verbose_name_plural = verbose_name


class Reply(models.Model):
    """
    系统回复
    """
    id = models.AutoField(primary_key=True)
    aid = models.IntegerField(verbose_name='话题发起人')  # 话题发起人
    rname = models.CharField(max_length=50, verbose_name='回复人名字', default='系统')
    tid = models.IntegerField(verbose_name='回复的话题')  # 回复的话题的id
    content = models.TextField(verbose_name='内容')
    create_time = models.CharField(max_length=20, verbose_name='系统回复时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '后台回复'
        verbose_name_plural = verbose_name


class Like(models.Model):
    """
    点赞
    """
    uid = models.IntegerField(verbose_name='用户id')
    tid = models.IntegerField(verbose_name='话题id')
    cancel = models.BooleanField(default=True, verbose_name='是否取消点赞')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '点赞记录'
        verbose_name_plural = verbose_name
