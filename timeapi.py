from urllib import request
import json


def Get_time():
    return int(str(json.loads(request.urlopen(url='http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp').read())['data']['t'])[:-3])


def Check_time(time):
    if time > Get_time():
        return True
    elif time < Get_time():
        return False


if __name__ == '__main__':
    print(Get_time())
    print(Check_time(1546776412))