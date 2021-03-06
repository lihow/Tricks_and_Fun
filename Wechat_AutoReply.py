# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#coding=utf8
import itchat
import time

# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息
@itchat.msg_register('Text')
def text_reply(msg):
    # 当消息不是由自己发出的时候
    if not msg['FromUserName'] == myUserName:
        # 发送一条提示给文件助手
        itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
                        (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
                         msg['User']['NickName'],
                         msg['Text']), 'filehelper')
        # 回复给好友
        return u'[自动回复]您好，我现在有事不在，一会再和您联系。\n已经收到您的信息：%s\n' % (msg['Text'])

if __name__ == '__main__':
    itchat.auto_login()

    # 获取自己的UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    
    #test for 特定的人
    '''
    i=0
    while i < 60:  
        user2 = itchat.search_friends(name=u'test')  
        userName2 = user2[0]['UserName']  
        ss = u'每过一秒，我对你的爱就增加一秒~' + str(i) + 's'  
        itchat.send(ss, toUserName=userName2)  
        time.sleep(1)  
        i += 1
    '''

    itchat.run()