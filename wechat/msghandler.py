from django.template.loader import render_to_string
from .qiushibaike.qiubai_spider import QiuBai
import time

TO_USER = 'ToUserName'
FROM_USER = 'FromUserName'
CREATE_TIME = 'CreateTime'
MSG_TYPE = 'MsgType'
CONTENT = 'Content'
PIC_URL = 'PicUrl'

TEMPLATE_TO_USER = 'ToUserName'
TEMPLATE_FROM_USER = 'FromUserName'
TEMPLATE_CREATE_TIME = 'CreateTime'
TEMPLATE_CONTENT = 'Content'

SUBSCRIBE_STR = '感谢您的关注！\n我的个人博客：http://www.cjxh616.com\n我的微信号：cjxh123'
DEAFAULT_STR = ''

class HandleMessage():
    '''
    处理微信消息
    '''
    def __init__(self):
        self.qiubai = QiuBai()
        self.response_content = ''

    def __getReqTxtAttr(self,xml):
        '''
        获取微信文本消息参数
        :param xml: 
        :return: 
        '''
        self.from_user = xml.find(FROM_USER).text
        self.to_user = xml.find(TO_USER).text
        self.content = xml.find(CONTENT).text

    def __getReqImgAttr(self,xml):
        '''
        获取微信图片消息参数
        :param xml: 
        :return: 
        '''
        self.from_user = xml.find(FROM_USER).text
        self.to_user = xml.find(TO_USER).text
        self.pic_url = xml.find(PIC_URL).text

    def __getReqSubAttr(self,xml):
        '''
        获取微信关注事件参数
        :param xml: 
        :return: 
        '''
        self.from_user = xml.find(FROM_USER).text
        self.to_user = xml.find(TO_USER).text

    def __getResTxtXml(self):
        '''
        获取相应微信用户的文本格式xml
        :return: 
        '''
        ctx = {
            TEMPLATE_TO_USER:self.from_user,
            TEMPLATE_FROM_USER:self.to_user,
            TEMPLATE_CREATE_TIME:time.time(),
            TEMPLATE_CONTENT:self.response_content
        }
        return render_to_string('wechat/wx_text.xml',context=ctx)

    def handleTxtMsg(self,xml):
        '''
        处理微信文本消息请求
        :param xml: 
        :return: 
        '''
        try:
            self.__getReqTxtAttr(xml)
            if self.content == '糗事百科':
                self.response_content = self.qiubai.get_joke()
            elif self.content[:4] == 车票查询：

            return self.__getResTxtXml()

