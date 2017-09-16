from django.shortcuts import render,HttpResponse
from django.utils.encoding import smart_str
import hashlib,requests
from lxml import etree
from .basic import Basic

#请按照公众平台官网\基本配置中信息填写
TOKEN = 'cjxh2017'
APP_ID = 'wx68c7f70e73029e26'
APP_SERCRET = 'd0eb6851932ae501fe94a6c1160c4e18'
EncodingAESKey = 'dull3eaQLn9d3lhiJHXv3Otj3ukEBzSdai5f7gAjPaX'

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
    if hashstr == signature:
        return echostr
    else:
        return ''

#https://api.weixin.qq.com/cgi-bin/media/upload?access_token=ACCESS_TOKEN&type=TYPE


def upload_tem_pic(path):
    '''
    上传临时图片素材并获取media_id
    :param path: 
    :return: 
    '''
    wx_tem_url = 'https://api.weixin.qq.com/cgi-bin/media/upload'
    B = Basic(APP_ID,APP_SERCRET)
    payload_tem = {
        'access_token':B.get_access_token(),
        'type':'image'
    }
    data = {'media':open(path,'rb')}
    r = requests.post(wx_tem_url,params=payload_tem,files=data)
    dict = r.json()
    return dict['media_id']

