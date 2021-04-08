from .models import Topic, Reply
from user.models import MyUser
from common.token import getUserId
from django.db.models import Q


def sresult(token, word, page):
    userId = getUserId(token)
    if userId['code'] == 0:
        res = Topic.objects.filter(check__in=[1, 3], user_delete=None, system_delete=None).filter(Q(title__contains=word)|Q(content__contains=word))
        count = res.count()
        listdata = list(
            res.values('id', 'name', 'headimg', 'title', 'content', 'imgs', 'top', 'like', 'dislike', 'visit',
                         'create_time'))
        listdata.sort(key=lambda keys: keys['id'], reverse=True)
        data = listdata[(page - 1) * 10:page * 10]
        print(data)
        for i in data:
            i['desca'] = i['content'][:30]
            del i['content']
        return {
            'code': 0,
            'msg': '获取关键词"'+str(word)+'",第' + str(page) + '页的数据成功',
            'count': count,
            'data': data
        }

    else:
        return userId