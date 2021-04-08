from rest_framework.authtoken.models import Token


def getUserId(token):
    user = Token.objects.filter(key=token)
    if not user:
        return {
            'code': -1,
            'msg': 'token不存在或登录状态已失效'
        }
    else:
        userId = user[0].user_id
        return {
            'code': 0,
            'msg': '查询到对应token',
            'data': {
                'id':userId
            }
        }