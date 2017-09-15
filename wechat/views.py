from django.shortcuts import render,HttpResponse
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
import hashlib
from lxml import etree
from .mywechat_tool import *
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
        return HttpResponse(handleMessages(request_xml))

def handleMessages(xml):
    '''
    处理微信消息
    :param xml: 
    :return: 
    '''
    #按消息类型分发处理
    type = xml.find('MsgType').text
    if type == 'text':
        return msgHandler.handleTxtMsg(xml)
    else:
        return 'success'

