from requests import post
from json import loads, dumps
from base64 import b64encode
from common.token import getUserId
from user.models import MyUser
from .info import saveInfo


def doAuth(usr, pwd, token):
    userId = getUserId(token)
    if userId['code'] == 0:
        userId = userId['data']['id']
        # 判断学号是否已经被绑定
        user = MyUser.objects.filter(student_id=usr)
        if user and user[0].id != userId:
            return {
                'code': 1,
                'msg': '学号已被绑定！'
            }
        usr = str(usr)
        pwd = str(pwd)
        pwd = str(b64encode(bytes(pwd, encoding='utf-8')))

        url = 'http://jxglstu.hfut.edu.cn:7070/appservice/home/appLogin/login.action'
        data = {
            "username": usr,
            "password": pwd[2:-1],
            "identity": "0"
        }
        try:
            r = post(url, data=data, timeout=3).text
        except:
            return {
                'code': -2,
                'msg': '发生错误，请检查网络！如非网络错误请联系管理员！'
            }
        try:
            code = loads(r)['code']
            if code == 200:

                data = loads(r)['obj']['business_data']
                saveInfo(data, token)
                return {
                    'code': 0,
                    'msg': '认证身份成功！个人信息已被更新！',
                }
            elif code == 1001:
                return {
                    'code': -1,
                    'msg': '学号或密码错误！'
                }
        except:
            return {
                'code': -3,
                'msg': '学校闭网中，目前无法完成身份认证！'
            }
    else:
        return userId


