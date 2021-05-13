from django.http import JsonResponse

from .comment import add
from .topics import getList, getDetail, addTopic, getCate, like, my_topic
from .search import sresult

def topic_list(request):
    if request.method == 'POST':
        token = request.META.get("HTTP_TOKEN")
        page = int(request.POST.get('page', 1))
        pid = int(request.POST.get('pid', 1))
        res = getList(page, token, pid)
        return JsonResponse(res)
    else:
        return JsonResponse({
            'code': -1,
            'msg': '请使用POST方式来请求该接口！'
        }, status=500)


def detail(request):
    if request.method == 'POST':
        token = request.META.get("HTTP_TOKEN")
        id = request.POST.get('id', 0)
        if id:
            res = getDetail(token, id)
            return JsonResponse(res)
        else:
            return JsonResponse({
                'code': -1,
                'msg': '请传入id字段！'
            })

    else:
        return JsonResponse({
            'code': -1,
            'msg': '请使用POST方式来请求该接口！'
        }, status=500)


def new_topic(request):
    if request.method == 'POST':
        data = dict()
        token = request.META.get("HTTP_TOKEN")
        data['title'] = request.POST.get('title', '')
        data['category'] = request.POST.get('category', 1)
        data['content'] = request.POST.get('content', '')
        data['imgs'] = str(request.POST.get('imgs', ''))
        data['hide'] = int(request.POST.get('hide', 0))
        res = addTopic(token, data)
        return JsonResponse(res)
    else:
        return JsonResponse({
            'code': -1,
            'msg': '请使用POST方式来请求该接口！'
        }, status=500)


def add_comment(request):
    if request.method == 'POST':
        token = request.META.get("HTTP_TOKEN")
        tid = request.POST.get('tid')
        content = request.POST.get('content')
        if not (tid and content):
            return JsonResponse({
                'code': -1,
                'msg': '参数错误'
            })
        res = add(tid, content, token)
        return JsonResponse(res)
    else:
        return JsonResponse({
            'code': -1,
            'msg': '请使用POST方式来请求该接口！'
        }, status=500)


def search(request):
    if request.method == 'POST':
        token = request.META.get("HTTP_TOKEN")
        word = request.POST.get('word', '')
        if not word:
            return JsonResponse({
                'code': -1,
                'msg': '请输入要搜索的关键词'
            })
        page = int(request.POST.get('page', 1))
        res = sresult(token, word, page)
        return JsonResponse(res)

    else:
        return JsonResponse({
            'code': -1,
            'msg': '请使用POST方式来请求该接口！'
        }, status=500)


def cate(request):
    if request.method == 'POST':
        token = request.META.get("HTTP_TOKEN")
        res = getCate(token)
        return JsonResponse(res)

    else:
        return JsonResponse({
            'code': -1,
            'msg': '请使用POST方式来请求该接口！'
        }, status=500)

def like_topic(request):
    if request.method == 'POST':
        token = request.META.get("HTTP_TOKEN")
        tid = int(request.POST.get('tid', 0))
        res = like(token, tid)
        return JsonResponse(res)

    else:
        return JsonResponse({
            'code': -1,
            'msg': '请使用POST方式来请求该接口！'
        }, status=500)


def my(request):
    if request.method == 'POST':
        token = request.META.get("HTTP_TOKEN")
        res = my_topic(token)
        return JsonResponse(res)

    else:
        return JsonResponse({
            'code': -1,
            'msg': '请使用POST方式来请求该接口！'
        }, status=500)