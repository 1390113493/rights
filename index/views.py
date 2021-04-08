from django.http import JsonResponse
def err404(request, exception):
    return JsonResponse({
        'code':-1,
        'errcode':'404',
        'msg':'学生权益提醒您：页面未找到！'
    })

def err500(request):
    return JsonResponse({
        'code':-1,
        'errcode':'500',
        'msg':'学生权益提醒您：系统发生了一些错误！'
    })

