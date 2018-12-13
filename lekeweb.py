import lekeshuadan, wechatmesg


def wechatlogin():
    wechatmesg.login()


def run(sleeptime):
    lekeshuadan.addcookies()
    lekeshuadan.login()
    flyg=lekeshuadan.shuadan(sleeptime)
    if flyg == 1:
        wechatmesg.sendmesg('2、乐客联盟接单啦！~')
    elif flyg == 2:
        wechatmesg.sendmesg('2、乐客联盟还有评价任务未完成，请先完成。~')
    return True
