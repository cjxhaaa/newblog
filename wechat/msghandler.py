
TO_USER = 'ToUserName'
FROM_USER = 'FromUserName'
CREATE_TIME = 'CreateTime'
MSG_TYPE = 'MsgType'
CONTENT = 'Content'
PIC_URL = 'PicUrl'

class HandleMessage():
    '''
    处理微信消息
    '''
    def __getReqTxtAttr__(self,xml):
        '''
        获取微信文本消息参数
        :param xml: 
        :return: 
        '''
        self.from_user = xml.find(FROM_USER).text
        self.to_user = xml.find(TO_USER).text
        self.content = xml.find(CONTENT).text

    def __getReqImgAttr__(self,xml):
        '''
        获取微信图片消息参数
        :param xml: 
        :return: 
        '''
        self.from_user = xml.find(FROM_USER).text
        self.to_user = xml.find(TO_USER).text
        self.pic_url = xml.find(PIC_URL).text

    def __getReqSubAttr__(self,xml):
        '''
        获取微信关注事件参数
        :param xml: 
        :return: 
        '''
        self.from_user = xml.find(FROM_USER).text
        self.to_user = xml.find(TO_USER).text

    def handleTxtMsg(self,xml):
        '''
        处理微信文本消息请求
        :param xml: 
        :return: 
        '''
        try:
            self.__getReqTxtAttr__(xml)
            if self.content == '段子':

