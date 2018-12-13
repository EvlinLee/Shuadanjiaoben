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
    login = {"username": "", "password": ""}
    # login = {"username": "", "password": ""}
    login = parse.urlencode(login).encode(encoding='utf-8')
    print(login)
    heard_dict = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 MicroMessenger/6.7.2 NetType/WIFI Language/zh_CN",
        "Content-Type": "application/x-www-form-urlencoded"}
    url_login = 'http://aaa.guzi58.com/index.php?s=/Index/login.html'
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
        textmod = {"task_type": "1", "maxmoney": "200000"}
        textmod = parse.urlencode(textmod).encode(encoding='utf-8')
        # print(textmod)
        heard_dict = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 MicroMessenger/6.7.2 NetType/WIFI Language/zh_CN",
            "Content-Type": "application/x-www-form-urlencoded"}
        url = 'http://aaa.guzi58.com/index.php?s=/Indexajax/taskset.html'
        req = request.Request(url=url, data=textmod, headers=heard_dict)
        res = guziopener.open(req)
        res = res.read()
        res = res.decode('unicode_escape')
        print(res)
        code = json.loads(res)['code']
        msgs = json.loads(res)['msgs']
        # print(type(code))
        print('***********************第 ', count, ' 次请求刷单任务***********************\n', '谷子18600232124：code =', code,
              ' msgs =',
              msgs)
        print()
        if code != 0:
            if code == 1:
                # 接单成功停止任务
                print('')
                print('')
                print('**************************************')
                print('**************************************')
                print('******         接单啦！         ******')
                print('**************************************')
                print('**************************************')
                return 1
            if code == 2 and msgs == '连接超时，请重新登录':
                print('')
                print('')
                print('**************************************')
                print('**************************************')
                print('***连接超时啦，10分钟后重启自动登陆***')
                print('**************************************')
                print('**************************************')
                return 3
        if msgs == '您还有进行中的任务没完成，请先完成任务':
            # 有未完成任务停止任务
            print('')
            print('')
            print('**************************************')
            print('**************************************')
            print('******   有未完成任务停止任务！ ******')
            print('**************************************')
            print('**************************************')
            return 2
        count += 1
        time.sleep(sleeptime)
    return True


if __name__ == '__main__':
    addcookies()
    login()
    shuadan()
