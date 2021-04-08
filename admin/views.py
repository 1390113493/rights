from common.models import System
from topic.models import Topic, Reply, Category
from user.models import MyUser
from django.http import JsonResponse, HttpResponse
from time import strftime, localtime
from django.shortcuts import render


def getTopicList1(request):
    if request.method == 'GET':
        # type = '1'
        # return render(request, 'topiclist.html', locals())
        return HttpResponse('404 NOT FOUND', status=404)
    elif request.method == 'POST':
        page = int(request.POST.get('page', 1))
        limit = int(request.POST.get('limit', 10))
        lists = Topic.objects.filter(user_delete__isnull=True, system_delete__isnull=True)
        count = lists.count()
        listdata = list(
            lists.values('id', 'check', 'name', 'headimg', 'title', 'content', 'imgs', 'top', 'like', 'dislike',
                         'visit', 'pid',
                         'create_time'))
        listdata.sort(key=lambda keys: keys['id'], reverse=True)

        data = listdata[(page - 1) * limit:page * limit]
        for i in data:
            i['category'] = Category.objects.get(id=i['pid']).name
            del i['pid']

        return JsonResponse({
            'code': 0,
            'msg': '获取第' + str(page) + '页的数据成功',
            'count': count,
            'data': data
        })


def getTopicList2(request):
    if request.method == 'GET':
        # type = '2'
        # return render(request, 'topiclist.html', locals())
        return HttpResponse('404 NOT FOUND', status=404)
    elif request.method == 'POST':
        page = int(request.POST.get('page', 1))
        limit = int(request.POST.get('limit', 10))
        lists = Topic.objects.filter(check__in=[2, 3], user_delete__isnull=True, system_delete__isnull=True)
        count = lists.count()
        listdata = list(
            lists.values('id', 'check', 'name', 'headimg', 'title', 'content', 'imgs', 'top', 'like', 'dislike',
                         'visit', 'pid',
                         'create_time'))
        listdata.sort(key=lambda keys: keys['id'], reverse=True)

        data = listdata[(page - 1) * limit:page * limit]
        for i in data:
            i['category'] = Category.objects.get(id=i['pid']).name
            del i['pid']

        return JsonResponse({
            'code': 0,
            'msg': '获取第' + str(page) + '页的数据成功',
            'count': count,
            'data': data
        })


def getTopicDetail(request):
    id = request.POST.get('id', 0)
    try:
        detail = Topic.objects.get(id=id)
        category = Category.objects.get(id=detail.pid)
    except:
        return JsonResponse({
            'code': -1,
            'msg': '该id对应话题不存在!'
        })
    d = dict()
    d['id'] = detail.id
    d['category'] = category.name
    d['needreply'] = category.needreply
    d['check'] = detail.check
    d['name'] = detail.name
    d['headimg'] = detail.headimg
    d['title'] = detail.title
    d['content'] = detail.content
    d['imgs'] = eval(detail.imgs)
    d['like'] = detail.like
    d['dislike'] = detail.dislike
    d['visit'] = detail.visit
    d['create_time'] = detail.create_time
    if Category.objects.get(id=detail.pid).needreply and detail.check in [1, 3]:
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
    return JsonResponse({
        'code': 0,
        'msg': '获得话题详细信息成功',
        'data': data
    })


def delTopic(request):
    time = strftime("%Y-%m-%d %H:%M:%S", localtime())
    id = request.POST.get('id', 0)
    try:
        topic = Topic.objects.get(id=id)
    except:
        return JsonResponse({
            'code': -1,
            'msg': '该id对应话题不存在!'
        })
    topic.system_delete = time
    topic.save()
    return JsonResponse({
        'code': 0,
        'msg': '删除话题成功！'
    })


def checkTopic(request):
    if request.method == 'GET':
        type = int(request.GET.get('type', '1'))
        id = request.GET.get('id', 0)
        topic = Topic.objects.get(id=id)
        user = MyUser.objects.get(id=topic.uid)
        name = topic.name
        stu_id = user.student_id
        real_name = user.name
        category = Category.objects.get(id=topic.pid)
        cate = category.name
        title = topic.title
        content = topic.content
        imgs = eval(topic.imgs) if topic.imgs else None
        hide = ['不匿名', '匿名'][topic.hide]
        time = topic.create_time
        check = topic.check
        reply = category.needreply
        if reply and check in [1, 3]:
            try:
                rep = Reply.objects.get(tid=id)
                replycontent = rep.content
                replyname = rep.rname
            except:
                pass
        return render(request, 'topicform.html', locals())
    elif request.method == 'POST':
        check = int(request.POST.get('check', 0))
        id = request.POST.get('id', 0)
        reply = request.POST.get('reply', '')
        name = request.POST.get('name', '系统')
        topic = Topic.objects.get(id=id)
        time = strftime("%Y-%m-%d %H:%M:%S", localtime())

        needreply = Category.objects.get(id=topic.pid).needreply
        r = Reply.objects.filter(tid=id)
        if r:
            r.delete()
        if check not in [1, 3] and reply:
            return JsonResponse({
                'code': -1,
                'msg': '该状态不需要系统回复'
            })

        topic.check = check
        topic.save()
        if reply:
            d = {
                'tid': id,
                'aid': topic.uid,
                'rname': name,
                'content': reply,
                'create_time': time
            }
            Reply.objects.create(**d)

        return JsonResponse({
            'code': 0,
            'msg': '提交成功！'
        })


def categoryList(request):
    if request.method == 'GET':
        return HttpResponse('404 NOT FOUND', status=404)
        # return render(request, 'catelist.html', locals())
    elif request.method == 'POST':
        page = int(request.POST.get('page', 1))
        limit = int(request.POST.get('limit', 10))
        category = Category.objects.all()
        count = category.count()
        data = list(category.values())[(page - 1) * limit:page * limit]
        for i in data:
            i['count'] = Topic.objects.filter(pid=i['id']).count()
        return JsonResponse({
            'code': 0,
            'msg': '获取分类成功',
            'count': count,
            'data': data
        })


def editCategory(request):
    if request.method == 'GET':
        id = request.GET.get('id', 0)
        cate = Category.objects.get(id=id)
        name = cate.name
        needreply = int(cate.needreply)
        type = '修改'
        return render(request, 'cateform.html', locals())
    elif request.method == 'POST':
        id = int(request.POST.get('id', 0))
        name = request.POST.get('name', '')
        needreply = int(request.POST.get('needreply', 0))
        print(needreply)
        if not name:
            return JsonResponse({
                'code': -1,
                'msg': '分类名不能为空！'
            })
        category = Category.objects.filter(id=id)
        if category:
            category.update(name=name, needreply=needreply)
            return JsonResponse({
                'code': 0,
                'msg': '修改分类信息成功'
            })
        else:
            return JsonResponse({
                'code': -1,
                'msg': '该id对应分类不存在!'
            })


def addCategory(request):
    if request.method == 'GET':
        type = '新增'
        return render(request, 'cateform.html', locals())
    elif request.method == 'POST':
        name = request.POST.get('name', '')
        needreply = int(request.POST.get('needreply', 0))
        if not name:
            return JsonResponse({
                'code': -1,
                'msg': '分类名不能为空！'
            })
        c = Category.objects.create(name=name, needreply=needreply)
        if c.id:
            return JsonResponse({
                'code': 0,
                'msg': '新增分类成功！'
            })
        else:
            return JsonResponse({
                'code': -1,
                'msg': '新增分类失败'
            })


def delCategory(request):
    id = int(request.POST.get('id', 0))
    category = Category.objects.filter(id=id)
    if category:
        category.delete()
        return JsonResponse({
            'code': 0,
            'msg': '删除分类成功'
        })
    else:
        return JsonResponse({
            'code': -1,
            'msg': '该id对应分类不存在!'
        })


def userList(request):
    if request.method == 'GET':
        return HttpResponse('404 NOT FOUND', status=404)
        # return render(request, 'catelist.html', locals())
    elif request.method == 'POST':
        page = int(request.POST.get('page', 1))
        limit = int(request.POST.get('limit', 10))
        user = MyUser.objects.filter(auth=1)
        count = user.count()
        data = list(
            user.values('id', 'name', 'auth', 'gender', 'headimg', 'student_id', 'phone', 'adminclass', 'department',
                        'email'))[
               (page - 1) * limit:page * limit]
        return JsonResponse({
            'code': 0,
            'msg': '获取用户成功',
            'count': count,
            'data': data
        })


def userDetail(request):
    id = request.GET.get('id', 1)
    count = Topic.objects.filter(uid=id).count()
    user = MyUser.objects.get(id=id)
    wechatname = user.wechatname
    student_id = user.student_id
    name = user.name
    campus = user.campus
    department = user.department
    major = user.major
    adminclass = user.adminclass
    dormitory = user.dormitory
    email = user.email
    phone = user.phone
    qq = user.qq
    nickname = user.nickname
    headimg = user.headimg
    gender = user.gender
    auth = user.auth
    birthday = user.birthday
    sign = user.sign
    date = user.date_joined
    return render(request, 'userdetail.html', locals())


def appSet(request):
    if request.method == 'GET':
        about = list(System.objects.all().values())
        d = {}
        for i in about:
            if i['name'] in ['version', 'help', 'newx', 'us']:
                d[i['name']] = i['value']
        version = d['version']
        help = d['help']
        newx = d['newx']
        us = d['us']
        return render(request, 'appform.html', locals())
    elif request.method == 'POST':
        d = dict()
        d['version'] = request.POST.get('version', '')
        d['help'] = request.POST.get('help', '')
        d['newx'] = request.POST.get('newx', '')
        d['us'] = request.POST.get('us', '')
        for k, v in d.items():
            s = System.objects.get(name=k)
            s.value = v
            s.save()
        return JsonResponse({
            'code': 0,
            'msg': '修改小程序信息成功！'
        })
