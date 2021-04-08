from requests import get
from json import loads
from .models import MyUser
from rest_framework.authtoken.models import Token
from django.contrib import auth


def wechatLogin(code):
    url = 'https://api.weixin.qq.com/sns/jscode2session?appid=wx59f18a51baf7d36a&secret=47a7f44b5970c6eccab21e9c2cc95757&js_code='+str(code)+'&grant_type=authorization_code'
    # datas = {
    #     'appid': 'wx59f18a51baf7d36a',  # 从微信小程序后台获取
    #     'secret': '47a7f44b5970c6eccab21e9c2cc95757',
    #     'js_code': code,
    #     'grant_type': 'authorization_code'
    # }
    try:
        res = loads(get(url, timeout=2).text)
    except:
        return {
            'code': -1,
            'msg': '请求超时'
        }
    print(res)
    try:
        res['errcode']
        return {
            'code': -1,
            'errcode': res['errcode'],
            'msg': res['errmsg']
        }
    except:
        openid = res['openid']
        session_key = res['session_key']
        if not MyUser.objects.filter(openid=openid):
            register(openid, session_key)
        # auth为判断是否已进行身份验证。由于身份验证会在首次登录时进行，若未身份验证，则说明用户的头像、微信名等未被保存到数据库中。
        # auth 0:未验证，1:已验证
        auth = MyUser.objects.filter(openid=openid)[0].auth
        token = getToken(openid)
        return {
            'code': 0,
            'msg': '登录成功！',
            'data': {
                'token': token,
                'auth': auth
            }

        }




def register(openid, session_key):
    data = dict(username=openid, password=openid, openid=openid, session_key=session_key, email='hfuter@mail.hfut.edu.cn')
    user = MyUser.objects.create_user(**data)
    user.save()


def getToken(openid):
    user = auth.authenticate(username=openid, password=openid)
    token = Token.objects.update_or_create(user=user)
    return str(token[0])


def deltoken(token):
    try:
        Token.objects.get(key=token).delete()

        return {
            'code': 0,
            'msg': '去除登录状态成功！'
        }
    except:
        return {
            'code': -1,
            'msg': '该token不存在！'
        }