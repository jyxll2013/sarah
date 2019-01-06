#!/user/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'apple_queen'
import unittest
import requests
#from case.loginblog import Blog
from common.logger import Log

class Blog_login(unittest.TestCase):
    log = Log()
    def login(self, username, psw, reme=True):
        '''三个参数：
        账号：username，密码：psw,记住登录：reme=True'''
        url = "https://passport.cnblogs.com/user/signin"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
            "Cookie": "__gads=ID=79675e6b2e2a2cc5:T=1540021164:S=ALNI_MbcaBHB7l0wWPz6HqJZSDL4jnjlCg; _ga=GA1.2.1052198134.1529647312; _gid=GA1.2.1553588805.1540820399; ASP.NET_SessionId=fv1kvoa1szr4e0wvh0vm5nyg; SERVERID=34e1ee01aa40e94e2474dffd938824db|1540820659|1540820341",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Content-Length": "385"
                 }
        json_data = {"input1": "DxjDUqHurYLadyrBTj2VC1SvElbffhxGdmMM0VelSSiIzWKojppd3ZxrRSwQi6NqkLaAkR0PzVe2hTfkZneFtHCndbyIBExh4VQmxmh4CoqoOY8sSQfJH2wi8zOzNc4ZnuBFNr7Gw3YXq1pSymmyqaNSnsN5YlXDVBH042+lSbw=",
                "input2": "RXhcTrGtmilPyC+Dl8Qj14fXeP6WW6KFoqJOFpfZhMyFglCDT6BqnlVILrLetSuDrH94QHWVl08btKa+DnaKuJxkP7bXJUdZGQAnoNPyTqUmcH7v8EI2GDwveNM9PwVHb8Ymb7CSRPO9fcrHSpypoGBWrLgaE/y2TMv5R8uUy/0=",
                "remember": True}


        res = requests.post(url, headers=header, json=json_data, verify=False)
        result1 = res.content  # 字节输出
        self.log.info("博客园登录结果：%s"%result1)
        return res.json()      # 返回json

    def test_login1(self):
        u'''测试登录：正确账号，正确密码'''
        self.log.info("------登录成功用例：start!---------")
        username = "DxjDUqHurYLadyrBTj2VC1SvElbffhxGdmMM0VelSSiIzWKojppd3ZxrRSwQi6NqkLaAkR0PzVe2hTfkZneFtHCndbyIBExh4VQmxmh4CoqoOY8sSQfJH2wi8zOzNc4ZnuBFNr7Gw3YXq1pSymmyqaNSnsN5YlXDVBH042+lSbw=",
        self.log.info("输入正确账号：%s"%username)
        psw = "RXhcTrGtmilPyC+Dl8Qj14fXeP6WW6KFoqJOFpfZhMyFglCDT6BqnlVILrLetSuDrH94QHWVl08btKa+DnaKuJxkP7bXJUdZGQAnoNPyTqUmcH7v8EI2GDwveNM9PwVHb8Ymb7CSRPO9fcrHSpypoGBWrLgaE/y2TMv5R8uUy/0=",
        self.log.info("输入正确密码：%s"%psw )
        result = self.login(username, psw)
        self.log.info("获取测试结果：%s"%result)
        self.assertEqual(result["success"], True)
        self.log.info("------pass!---------")

    def test_login2(self):
        u'''测试登录：正确账号，错误密码'''
        self.log.info("------登录失败用例：start!---------")
        username = "DxjDUqHurYLadyrBTj2VC1SvElbffhxGdmMM0VelSSiIzWKojppd3ZxrRSwQi6NqkLaAkR0PzVe2hTfkZneFtHCndbyIBExh4VQmxmh4CoqoOY8sSQfJH2wi8zOzNc4ZnuBFNr7Gw3YXq1pSymmyqaNSnsN5YlXDVBH042+lSbw=",
        self.log.info("输入正确账号：%s"%username)
        psw = "xxx",
        self.log.info("输入错误密码：%s"%username)
        result = self.login(username, psw)
        self.log.info("获取测试结果：%s"%result)
        self.assertEqual(result["success"], False)
        self.log.info("------pass!---------")


if __name__ == "__main__":
    unittest.main()

