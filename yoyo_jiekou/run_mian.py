#!/user/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'apple_queen'
import os
import unittest
import time
import HTMLTestRunner_cn
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
#当前脚本所在文件中真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))
print(cur_path)
def add_case(caseName = "case",rule = "test*.py"):
    '''第一步：加载所有的测试用例'''
    case_path = os.path.join(cur_path,caseName)#用例文件夹
    #如果不存在这个case文件夹，就自动创建一个
    if not os.path.exists(case_path):os.mkdir(case_path)
    #定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path, pattern = rule, top_level_dir = None)
    print(discover)
    return discover
def run_case(all_case, reportName = "report"):
    '''第二步：执行所有的用例，并把结果写入HTML报告'''
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path,reportName)
    #如果不存在report这个文件夹，自动创建一个
    if not os.path.exists(report_path):os.mkdir(report_path)
    report_abspath = os.path.join(report_path,now+"result.html")
    print("report path is :%s"%report_abspath)
    fp = open(report_abspath,"wb")
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title="自动化测试报告，测试结果如下：",description="用例执行情况")
    #调用add_case函数返回值
    runner.run(all_case)
    fp.close()
def get_report_file(report_path):
    '''第三步：获取最新的测试报告'''
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn:os.path.getmtime(os.path.join(report_path,fn)))#按照报告修改时间排序
    print("最新生成的报告："+lists[-1])#取列表中最后一个，即最新修改的测试报告
    #找到最新生成的报告文件
    report_file = os.path.join(report_path,lists[-1])
    return report_file
def send_mail(sender, psw, receiver, smtpserver, report_file, port):
    '''第四步：发送最新的测试报告内容'''
    with open(report_file,"rb") as f:
        mail_body = f.read()
    #定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype="html", _charset="utf-8")#邮件正文
    msg["subject"] = u"自动化测试报告"
    msg["from"] = sender
    msg["to"] = receiver
    msg.attach(body)
    #添加附件
    att = MIMEText(open(report_file,"rb").read(),"base64","utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment;filename = "report.html"'

    msg.attach(att)
    #连接邮件服务器，ssl加密的就走SMTP_SSL，其他使用SMTP
    try:
        smtp = smtplib.SMTP_SSL(smtpserver,port)
    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver,port)
    #用户名密码
    smtp.login(sender,psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print("test report email has send out！")
#执行代码
if __name__ == "__main__":
    all_case = add_case()#1 加载用例
    #生成测试报告的路径
    run_case(all_case)#2 执行用例
    #获取最新的测试报告
    report_path = os.path.join(cur_path,"report")#报告文件夹
    report_file = get_report_file(report_path)#3 获取最新的测试报告
    #邮箱配置
    from config import readconfig
    smtp_server = readconfig.smtp_server
    port = readconfig.port
    sender = readconfig.sender
    psw = readconfig.psw
    receiver = readconfig.receiver
    send_mail(sender, psw,receiver,smtp_server,report_file,port)#4 发送邮件



