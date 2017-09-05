from django.shortcuts import render,HttpResponse
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
import hashlib
from lxml import etree
from .main import *
from .mywechat_tool import *



def checkWeChat(signature,timestamp)

@csrf_exempt
def wechat(request):
    '''
    微信消息处理
    '''
    if request.method == 'GET':
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr  = request.GET.get('echostr')
        echo = checkWeChat(signature,timestamp,nonce,echostr,token)
        return HttpResponse(echo)

    elif request.method == 'POST':
        xml_str = smart_str(request.body)
        request_xml = etree.fromstring(xml_str)
        response_xml = auto_reply_main(request_xml)
        return HttpResponse(request_xml)


