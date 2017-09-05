from django.http import HttpResponse
from django.template.loader import render_to_string


def auto_reply_main(request_xml):
    '''
    识别消息事件，分类处理
    :param request_xml: 
    :return: 
    '''
