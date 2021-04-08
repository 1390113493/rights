from django.http import JsonResponse
from .auth import doAuth
from .login import wechatLogin, deltoken
from .info import setWechatInfo, setUserInfo, getUserInfo


def login(request):
    if request.method == 'POST':
        code = request.POST.get('code', '')
        if code:
            res = wechatLogin(code)
            return JsonResponse(res)
        else:
            return JsonResponse({
                'code': -1,
                'msg': '请传递字段code(从微信接口获取)给该接口！'
            })

    else:
        return JsonResponse({
            'code': -1,
            'msg': '请使用POST方式来请求该接口！'
        }, status=500)


def logout(request):
    token = request.META.get("HTTP_TOKEN")
    res = deltoken(token)
    return JsonResponse(res)



def getInfo(request):
    if request.method == 'POST':
        token = request.META.get("HTTP_TOKEN")
        info = getUserInfo(token)
        return JsonResponse(info)
    else:
        return JsonResponse({
            'code': -1,
            'msg': '请使用POST方式来请求该接口！'
        }, status=500)

def editinfo(request):
    if request.method == 'POST':
        token = request.META.get("HTTP_TOKEN")
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        qq = request.POST.get('qq', '')
        nickname = request.POST.get('nickname', '')
        sign = request.POST.get('sign', '')
        data = {
            'email': email,
            'phone': phone,
            'qq': qq,
            'nickname': nickname,
            'sign': sign
        }
        try:
            setUserInfo(data, token)
            return JsonResponse({
                'code': 0,
                'msg': '修改个人资料成功！'
            })
        except:
            return JsonResponse({
                'code': -1,
                'msg': '设置个人信息出现异常！'
            })
    else:
        return JsonResponse({
            'code': -1,
            'msg': '请使用POST方式来请求该接口！'
        }, status=500)


# 设置微信资料
def setInfo(request):
    if request.method == 'POST':
        token = request.META.get("HTTP_TOKEN")
        wechatname = request.POST.get('wechatname', '')
        headimg = request.POST.get('headimg', '')
        if wechatname and headimg:
            try:
                setWechatInfo(wechatname, headimg, token)
                return JsonResponse({
                    'code': 0,
                    'msg': '绑定微信资料成功！'
                })
            except:
                return JsonResponse({
                    'code': -1,
                    'msg': '出现异常！'
                })
        else:
            return JsonResponse({
                'code': -1,
                'msg': 'wechatname和headimg字段不得为空'
            })
    else:
        return JsonResponse({
            'code': -1,
            'msg': '请使用POST方式来请求该接口！'
        }, status=500)


def auth(request):
    if request.method == 'POST':
        token = request.META.get("HTTP_TOKEN")
        usr = request.POST.get('username', '')
        pwd = request.POST.get('password', '')
        res = doAuth(usr, pwd, token)
        return JsonResponse(res)
    else:
        return JsonResponse({
            'code': -1,
            'msg': '请使用POST方式来请求该接口！'
        }, status=500)