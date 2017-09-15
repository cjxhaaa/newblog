from django.template.loader import render_to_string
from .qiushibaike.qiubai_spider import QiuBai
from .train_spider.tickets import SearchTickets
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
DEAFAULT_STR = '''
 
回复「指南」
即可获得精品文章
回复「爬虫」
即可获得相关文章
回复「段子/来个段子」
即可获新鲜的段子
回复「今天吃什么」
即可随机获得一道美食
回复 「图片+关键词」
即可获得相关图片链接
重复搜索能得到不同答案
'''

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
            TEMPLATE_CREATE_TIME:int(time.time()),
            TEMPLATE_CONTENT:self.response_content
        }
        return render_to_string('wechat/wx_text.xml',context=ctx)

    def __getResNewsXml(self):
        '''
        响应微信用户的图文消息
        :return: 
        '''
        ctx = {
            TEMPLATE_TO_USER: self.from_user,
            TEMPLATE_FROM_USER: self.to_user,
            TEMPLATE_CREATE_TIME: int(time.time()),
        }

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
            elif self.content[:3] == '查车票':
                self.train = SearchTickets(self.content)
                self.response_content = self.train.get_train_info()
            return self.__getResTxtXml()
        except:
            return 'success'

    def hangdleSubscribe(self,xml):
        '''
        处理微信关注事件请求
        :param xml: 
        :return: 
        '''



