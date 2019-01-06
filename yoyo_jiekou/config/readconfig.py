#!/user/bin/env python
# -*-coding:utf-8 -*-
import os
import configparser
cur_path = os.path.dirname(os.path.realpath(__file__))
configpath = os.path.join(cur_path,"config.ini")
conf = configparser.ConfigParser()#是配置文件生效
conf.read(configpath,encoding="utf-8")
smtp_server = conf.get("email","smtp_server")
port = conf.get("email","port")
sender = conf.get("email","sender")
psw = conf.get("email","psw")
receiver = conf.get("email","receiver")