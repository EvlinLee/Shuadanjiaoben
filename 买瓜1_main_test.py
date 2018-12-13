import timeapi
import 买瓜1_信客 as xinke
import 买瓜1_微信 as wechat
import time

if timeapi.Check_time(1544104710):
    while True:
        sleeptime = int(input('请输入任务间隔时间（单位：秒）：'))
        retime = int(input('请输入任务重启时间（单位：秒）：'))
        wechat.login()
        xinke.addcookies()
        xinke.login()
        if xinke.shuadan(sleeptime=sleeptime):
            pass
        else:
            wechat.sendmesg('接到单啦~！ or 异常若没有接到单请截图程序打印信息发送给我！')
        time.sleep(retime)
else:
    print('脚本已过期')
