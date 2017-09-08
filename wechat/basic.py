import requests
import time

class Basic():
    def __init__(self,appId,appSecret):
        self.appId = appId
        self.appSecret = appSecret

    def get_access_token(self):
        payload_access_token={
            'grant_type':'client_credential',
            'appid':self.appId,
            'secret':self.appSecret
        }
        postUrl = 'https://api.weixin.qq.com/cgi-bin/token'
        r = requests.get(postUrl,params=payload_access_token)
        dict_result = r.json()
        return dict_result['access_token']


# class Basic():
#     def __init__(self,appId,appSecret):
#         self.__accessToken = ''
#         self.__leftTime = 0
#         self.appId = appId
#         self.appSecret = appSecret
#
#     def __real_get_access_token(self):
#         payload_access_token={
#             'grant_type':'client_credential',
#             'appid':self.appId,
#             'secret':self.appSecret
#         }
#         postUrl = 'https://api.weixin.qq.com/cgi-bin/token'
#         r = requests.get(postUrl,params=payload_access_token)
#         dict_result = r.json()
#         self.__accessToken = dict_result['access_token']
#         self.__leftTime = dict_result['expires_in']
#
#     def get_access_token(self):
#         if self.__leftTime < 10:
#             self.__real_get_access_token()
#         return self.__accessToken
#
#     def run(self):
#         while True:
#             if self.__leftTime > 10:
#                 time.sleep(2)
#                 self.__leftTime -= 2
#             else:
#                 self.__real_get_access_token()

