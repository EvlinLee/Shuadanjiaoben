from urllib import parse, request
from http import cookiejar
import time, os, json
import types


# username=18600232124&password=Wang..1314Yan

def addcookies():
    global guziopener
    guzicj = cookiejar.CookieJar()
    guzihandler = request.HTTPCookieProcessor(guzicj)
    guziopener = request.build_opener(guzihandler, request.HTTPHandler)
    # request.install_opener(guziopener)


def login():
    # 登陆
    login = {"username": "15659805963", "pwd": "", 'code': '', 'cid': 'passport'}
    # login = {"username": "", "password": ""}
    # login = {"username": "", "password": ""}
    print(login)
    login = parse.urlencode(login).encode(encoding='utf-8')
    heard_dict = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 MicroMessenger/6.7.2 NetType/WIFI Language/zh_CN",
        "Content-Type": "application/x-www-form-urlencoded"}
    url_login = 'http://aaa.698mn.com/passport/login.html'
    req_login = request.Request(url_login, login, heard_dict)
    res_login = guziopener.open(req_login)
    res_login = res_login.read()
    res_login = res_login.decode('unicode_escape')
    print(res_login)


def shuadan(sleeptime):
    count = 1
    secces = 0
    while True:
        # os.system('cls')
        # 请求刷单
        textmod = {"outtime": int(time.time()), "PlatformTypes": "0", 'TaskType': '无线端', 'TaskTypelen': '2',
                   'TaskPriceEnd': '20000', 'FineTaskClassType': '销量任务'}
        textmod = parse.urlencode(textmod).encode(encoding='utf-8')
        # print(textmod)
        heard_dict = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 MicroMessenger/6.7.2 NetType/WIFI Language/zh_CN",
            "Content-Type": "application/x-www-form-urlencoded"}
        url = 'http://aaa.698mn.com/site/acceptTask01.html'
        req = request.Request(url=url, data=textmod, headers=heard_dict)
        res = guziopener.open(req)
        res = res.read()
        res = res.decode('unicode_escape')
        # print(res)
        msg = json.loads(res)['acceptarr']['msg']
        # msgs = json.loads(res)['msgs']
        # print(type(code))
        print('***********************第 ', count, ' 次请求刷单任务***********************\n', res)
        print()
        # if err_code != 0:
        #     if err_code == 1:
        #         # 接单成功停止任务
        #         print('')
        #         print('')
        #         print('**************************************')
        #         print('**************************************')
        #         print('******         接单啦！         ******')
        #         print('**************************************')
        #         print('**************************************')
        #         return 1
        #     if err_code == 2 and msg == '连接超时，请重新登录':
        #         print('')
        #         print('')
        #         print('**************************************')
        #         print('**************************************')
        #         print('***连接超时啦，10分钟后重启自动登陆***')
        #         print('**************************************')
        #         print('**************************************')
        #         return 3
        if not '正在接销量任务' in msg:
            # 有未完成任务停止任务
            print('')
            print('')
            print('**************************************')
            print('**************************************')
            print('******   有未完成任务停止任务！ ******')
            print('**************************************')
            print('**************************************')
            return False
        count += 1
        time.sleep(sleeptime)
    return True


if __name__ == '__main__':
    addcookies()
    login()
    shuadan(4)
