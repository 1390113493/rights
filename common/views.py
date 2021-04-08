from django.http import JsonResponse
from .models import System
import uuid


def upimg(request):
    url = 'https://rights.huii.top/'
    try:
        file = request.FILES.get('img', None)
        if not file:
            return JsonResponse({
                'code': -1,
                'msg': 'no img for upload!'
            })
        uuid_str = uuid.uuid4().hex
        # 构成完整文件存储路径
        tmp_file_name = 'media/img/' + uuid_str + '.' + file.name.split('.')[-1]

        f = open(tmp_file_name, 'wb+')
        for chunk in file.chunks():
            f.write(chunk)
        f.close()
        return JsonResponse({
            'code': 0,
            'data': {
                'path': tmp_file_name,
            },
            'msg': '成功上传图片！'
        })
    except:
        return JsonResponse({
            'code': -1,
            'msg': '上传图片失败！'
        })


# 小程序信息
def about(request):
    about = list(System.objects.all().values())
    d = {}
    for i in about:
        if i['name'] in ['version', 'help', 'newx', 'us']:
            try:
                d[i['name']] = eval(i['value'])
            except:
                d[i['name']] = i['value']
    return JsonResponse({
        'code': 0,
        'msg': '获得小程序信息成功！',
        'data': d
    })
