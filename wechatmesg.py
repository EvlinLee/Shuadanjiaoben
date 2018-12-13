import itchat


def login():
    itchat.auto_login(hotReload=True)


def sendmesg(pingtai):
    friends = itchat.get_friends(update=True)[0:]
    for i in friends:
        # print(i)
        if '王鸟鸟' in i['RemarkName']:
            UserName = i['UserName']
    # 发送给UserName消息
    itchat.send(pingtai, toUserName=UserName)
    # 王刚
    # itchat.send('接单啦~！', toUserName='filehelper')


if __name__ == '__main__':
    login()
    sendmesg()
