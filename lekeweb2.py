import lekeshuadan2, wechatmesg


def wechatlogin():
    wechatmesg.login()


def run():
    lekeshuadan2.addcookies()
    lekeshuadan2.login()
    if lekeshuadan2.shuadan() == 1:
        wechatmesg.sendmesg('3、乐客联盟15968772003接单啦！~')
    if lekeshuadan2.shuadan() == 2:
        wechatmesg.sendmesg('3、乐客联盟15968772003还有评价任务未完成，请先完成。~')
    return True
