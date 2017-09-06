from django.shortcuts import render,HttpResponse
from django.utils.encoding import smart_str
import hashlib
from lxml import etree

#请按照公众平台官网\基本配置中信息填写
TOKEN = 'cjxh2017'

def checkWeChat(signature,timestamp,nonce,echostr):
    '''
    验证微信是否接入正确
    :param signature: 
    :param timestamp: 
    :param nonce: 
    :param echostr: 
    :return: 
    '''
    token = TOKEN
    list = [token,timestamp,nonce]
    list.sort()
    hashstr = "%s%s%s" % tuple(list)
    hashstr = hashlib.sha1(hashstr.encode('utf-8')).hexdigest()
    print("handle/GET func: hashcode, signature: ", hashstr, signature)
    if hashstr == signature:
        return echostr
    else:
        return ''