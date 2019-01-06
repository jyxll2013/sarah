#!/user/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'apple_queen'
from common.logger import Log
# #禁用安全警告
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Blog():
    # s = requests.seession() #全局参数
    log = Log()
    def __init__(self, s):
        self.s = s
    def login(self):
        url = "https://passport.126.com/dl/l"
        header = {   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Cookie": "P_INFO=jyxll2013@126.com|1540303758|0|mail126|00&99|sic&1540303518&mail126#sic&510100#10#0#0|138880&0|mail126|jyxll2013@126.com; nts_mail_user=jyxll2013@126.com:-1:1; starttime=; _ihtxzdilxldP8_=30; JSESSIONID-WYTXZDL=k769zRM8wJuSmXuAcZtJq6NGJqlnfurnFgqVFUT0y%2FQfPHyDAtcXxkpG3%2FQzOMXWRj%2BWliNkWI2gHJLVSgJXjkDwyctjpMwlwBcHx4f4gVQUQVilGA1F2RDSVudUwR6A7yRMyTta2umuiKpwYLni%2FuqF2EGa3b1gnhQvPiyQuIQvwzqy%3A1540822025543; THE_LAST_LOGIN=jyxll2013@126.com; jsessionid-cpta=VTKNZB24Zj6qEubFfkgyjvoFuFcmDg4W6Uv%5CASYXw1T6OhI%2B6zgfa9IDU2aDqirSj7oeWDhdjUF8MpijGBFxA%5C%5CtQwJCYBOnme8bnENnIiKKo%2FImHBLE%5CQlHTfpri0k88Mj2Xcq8y7C1rbi4y65OtrfBFLTjfZBDDA9CkhMg6DrRVtpC%3A1540304353406; c98xpt_=30; l_s_mail126QdQXWEQ=55835D327313F36E6F208A63B108DBD4A604DA410A79F5717D4FD25E4DCAA35D267EFCF61C58A368D966F1773F6AFDDBB92EEE537122A947DE647D5DDEEDCB4C435D89939EBDC8965C49FA853CC6398035F69E2BFEA2A675FB45407EE1053BF3072CD2BF461C1050A99D6229353B821B; utid=zAODi8GUcFwG2L2bhsQzEaxI5Bbjku0C; webzjcookiecheck=1",
            #"X-Requested-With": "XMLHttpRequest",
            # "Connection":"keep-alive",
            # "Content-Length":"385"
        }
        json_data = {"un":"jyxll2013@126.com",
                     "pw":"NW0IEWqEf2e7B0eh2fLcc3vOoSUsLIPaEDeNqRyq1tIymdbZPQont/HPp1cb/igqApEUvEGFV9udcsNQ1FKvlFE2Fcvg5EYN2MFp0vEiJ7z0mxabP3mlNv/QNQScXzXhK4KIthf0+YzoL44cfC7IaGVKVRtLnXI2+l9RIAcIyeE=",
                     "pd":"mail126",
                     "l":0,
                     "d":10,
                     "t":1540821470415,
                     "pkid":"QdQXWEQ",
                     "domains":"",
                     "tk":"923aba64f8c4dc376b670f089cb10084",
                     "pwdKeyUp":1,
                     "topURL":"http://126.com/",
                     "rtid":"O6Tl0TO2si4cJUBr3ZWkrgAWFlRfUFKO"
        }
        res = self.s.post(url,headers=header,json=json_data,verify=False)
        result1 = res.content  # 字节输出
        print(res.text)
        self.log.info(u"调用登录方法，获取结果：%s"%result1)
        #return res.json()
if __name__ == "__main__":
    import requests
    s = requests.session()
    Blog(s).login()