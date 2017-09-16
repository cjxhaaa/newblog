from django.shortcuts import render,HttpResponse
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
import hashlib
from lxml import etree
from .mywechat_tool import checkWeChat
from .msghandler import HandleMessage

msgHandler = HandleMessage()

@csrf_exempt
def wechat(request):
    '''
    微信消息处理
    '''
    if request.method == 'GET':
        try:
            signature = request.GET.get('signature')
            timestamp = request.GET.get('timestamp')
            nonce = request.GET.get('nonce')
            echostr  = request.GET.get('echostr')
            echo = checkWeChat(signature,timestamp,nonce,echostr)
            return HttpResponse(echo)
        except:
            return HttpResponse('啥都没有呀')

    elif request.method == 'POST':
        xml_str = smart_str(request.body)
        request_xml = etree.fromstring(xml_str)
        return HttpResponse(msgHandler.handleMessages(request_xml))



def create_menu(request):
    url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % Config.access_token
    data = {
        "button": [
            {
                "name": "web",
                "sub_button": [
                    {
                        "type": "view",
                        "name": "个人博客",
                        "url": "http://www.cjxh616.com"
                    }]
            },
            {
                "name": "爬虫",
                "sub_button": [
                    {
                        "type": "click",
                        "name": "糗事百科",
                        "key": "糗事百科"
                    },
                    {
                        "type": "click",
                        "name": "12306查询",
                        "key": "查车票"
                    }]
            }
        ]
    }
    # data = json.loads(data)
    # data = urllib.urlencode(data)
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    req.add_header('encoding', 'utf-8')
    response = urllib2.urlopen(req, json.dumps(data, ensure_ascii=False))
    result = response.read()
    return HttpResponse(result)

