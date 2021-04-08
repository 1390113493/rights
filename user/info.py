from common.token import getUserId
from user.models import MyUser


# 从学校接口获得资料
def saveInfo(data, token):
    userId = getUserId(token)
    if userId['code'] == 0:
        userId = userId['data']['id']
    else:
        exit(0)
    d = {
        'email': data['account_email'],
        'adminclass': data['adminclass_name'],
        'birthday': data['birthday'],
        'department': data['depart_name'],
        'gender': data['gender'],
        'major': data['major_name'],
        'phone': data['mobile_phone'],
        'student_id': data['user_code'],
        'name': data['user_name'],
        'auth': 1
    }
    user = MyUser.objects.filter(id=userId).update(**d)

# 从微信接口获得资料
def setWechatInfo(wechatname, headimg, token):
    userId = getUserId(token)
    if userId['code'] == 0:
        userId = userId['data']['id']
    else:
        exit(0)
    d = {
        'wechatname': wechatname,
        'headimg': headimg
    }
    user = MyUser.objects.filter(id=userId).update(**d)


#
def setUserInfo(data, token):
    userId = getUserId(token)
    if userId['code'] == 0:
        userId = userId['data']['id']
    else:
        exit(0)
    d = {k: v for k, v in data.items() if v}
    MyUser.objects.filter(id=userId).update(**d)


# 获取用户资料
def getUserInfo(token):
    userId = getUserId(token)
    if userId['code'] == 0:
        userId = userId['data']['id']
    else:
        exit(0)
    user = MyUser.objects.get(id=userId)
    info = dict()
    info['id'] = user.id
    info['wechatname'] = user.wechatname
    info['student_id'] = user.student_id
    info['auth'] = user.auth
    info['name'] = user.name
    info['department'] = user.department
    info['major'] = user.major
    info['adminclass'] = user.adminclass
    info['dormitory'] = user.dormitory
    info['email'] = user.email
    info['phone'] = user.phone
    info['qq'] = user.qq
    info['nickname'] = user.nickname
    info['headimg'] = user.headimg
    info['sign'] = user.sign
    info['gender'] = user.gender
    info['birthday'] = user.birthday
    return {
            'code': 0,
            'msg': '获取个人资料成功',
            'data': info
        }
