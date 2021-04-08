from .models import Topic, Reply, Category
from user.models import MyUser
from common.token import getUserId
from time import strftime, localtime


def getList(page, token):
    userId = getUserId(token)
    if userId['code'] == 0:
        lists = Topic.objects.filter(check__in=[1, 3], user_delete=None, system_delete=None)
        count = lists.count()
        listdata = list(lists.values('id', 'pid', 'name', 'headimg', 'title', 'content', 'imgs', 'top', 'like', 'dislike', 'visit', 'create_time'))
        listdata.sort(key=lambda keys: keys['id'], reverse=True)
        data = listdata[(page-1)*10:page*10]
        for i in data:
            i['desca'] = i['content'][:30]
            i['categort'] = Category.objects.get(id=i['pid']).name
            i['imgs'] = eval(i['imgs']) if i['imgs'] else None
            del i['content']
            del i['pid']
        return {
            'code': 0,
            'msg': '获取第'+str(page)+'页的数据成功',
            'count': count,
            'data': data
        }

    else:
        return userId

def getDetail(token, id):
    userId = getUserId(token)
    if userId['code'] == 0:
        detail = Topic.objects.get(id=id)
        detail.visit += 1
        detail.save()
        d = dict()
        d['id'] = detail.id
        d['category'] = Category.objects.get(id=detail.pid).name
        d['name'] = detail.name
        d['headimg'] = detail.headimg
        d['title'] = detail.title
        d['content'] = detail.content
        d['imgs'] = eval(detail.imgs) if detail.imgs else None
        d['like'] = detail.like
        d['dislike'] = detail.dislike
        d['visit'] = detail.visit
        d['create_time'] = detail.create_time
        if Category.objects.get(id=detail.pid).needreply:
            reply = Reply.objects.get(tid=id)
            r = dict()
            r['id'] = reply.id
            r['rname'] = reply.rname
            r['content'] = reply.content
            r['create_time'] = reply.create_time
            data = {
                'detail': d,
                'reply': r
            }
        else:
            data = {
                    'detail': d,
                }
        return {
            'code': 0,
            'msg': '获取话题详细内容成功',
            'data': data
        }
    else:
        return userId


def addTopic(token, data):
    timenow = localtime()
    day = strftime("%Y-%m-%d", timenow)
    time = strftime("%Y-%m-%d %H:%M:%S", timenow)
    userId = getUserId(token)
    if userId['code'] == 0:
        userId = userId['data']['id']

        if Topic.objects.filter(uid=userId, create_time__contains=day, system_delete__isnull=True):
            return {
                'code': -1,
                'msg': '今天已经发表过话题了，每人每天仅限一条哦！'
            }

        d = dict()
        user = MyUser.objects.get(id=userId)
        if data['hide']:
            d['name'] = user.nickname+' '+user.major
            d['headimg'] = ''
        else:
            d['name'] = user.name+' '+user.major
            d['headimg'] = user.headimg
        d['title'] = data['title']
        d['pid'] = data['category']
        d['uid'] = userId
        d['content'] = data['content']
        try:
            d['imgs'] = eval(data['imgs'])
        except:
            d['imgs'] = data['imgs'].split(',') if data['imgs'] else data['imgs']
        d['hide'] = data['hide']
        d['create_time'] = time
        print(d)
        topic = Topic.objects.create(**d)
        topic.save()
        return {
            'code': 0,
            'msg': '新增话题成功！'
        }

    else:
        return userId


def getCate(token):
    userId = getUserId(token)
    if userId['code'] == 0:
        category = Category.objects.all()
        return {
            'code': 0,
            'msg': '获取分类成功',
            'count': category.count(),
            'data': list(category.values())
        }
    else:
        return userId