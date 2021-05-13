# -*- coding: utf-8 -*-
# @Time    : 2021/5/6 21:13
# @Author  : HUII
# @FileName: comment.py
# @Software: PyCharm
import time

from common.token import getUserId
from topic.models import Topic, Comment


def add(tid, content, token):
    userId = getUserId(token)
    if userId['code'] == 0:
        if not Topic.objects.filter(id=tid, user_delete=None, system_delete=None):
            return {
                'code': -1,
                'msg': '话题不存在'
            }
        timenow = time.localtime()
        now = time.strftime("%Y-%m-%d %H:%M:%S", timenow)
        uid = userId['data']['id']
        Comment.objects.create(uid_id=uid, pid=tid, content=content, create_time=now)
        return {
            'code': 0,
            'msg': '新增评论成功'
        }
    else:
        return userId