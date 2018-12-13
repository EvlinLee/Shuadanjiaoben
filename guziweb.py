import guzishuadan, wechatmesg


def wechatlogin():
    wechatmesg.login()


def run(sleeptime):
    guzishuadan.addcookies()
    guzishuadan.login()
    flyg = guzishuadan.shuadan(sleeptime)
    if flyg == 1:
        wechatmesg.sendmesg('1、谷子接单啦！~')
    elif flyg == 2:
        wechatmesg.sendmesg('1、谷子还有进行中的任务没完成，请先完成任务~')
    elif flyg == 3:
        wechatmesg.sendmesg('1、谷子cookie失效啦，10分钟自动重新登陆~')
    return True
