import threading, time
import guziweb, lekeweb, wechatmesg

# import lekeweb2

print('1.谷子18600232124')
print('2.乐客联盟18600232124')
# print('3.乐客联盟15968772003')
print()
flyg = str(input('输入要跑的脚本序号：'))


def checkThread(retime, initThreadsName=[]):
    while True:
        time.sleep(retime)
        nowThreadsName = []
        now = threading.enumerate()
        for i in now:
            nowThreadsName.append(i.getName())  # 保存当前线程名称

        # for g in nowThreadsName:
        #     print(g)

        for j in initThreadsName:
            if j in nowThreadsName:
                pass
            else:
                if str(j) == '谷子':
                    guzi = threading.Thread(target=guziweb.run, args=(guzitime,), name='谷子')
                    guzi.setName('谷子')
                    guzi.start()
                if str(j) == '乐客联盟':
                    leke = threading.Thread(target=lekeweb.run, args=(leketime,), name='乐客联盟')
                    leke.setName('乐客联盟')
                    leke.start()
                # if str(j) == '乐客联盟2':
                #     leke = threading.Thread(target=lekeweb.run, name='乐客联盟2')
                #     leke.setName('乐客联盟2')
                #     leke.start()


sleeptime = input('输入任务间隔时间（单位：秒）：')
retime = input('输入任务重启时间（单位：秒）：')
guzitime = int(sleeptime[:1])
leketime = int(sleeptime[1:2])
guzi = threading.Thread(target=guziweb.run, args=(guzitime,), name='谷子')
leke = threading.Thread(target=lekeweb.run, args=(leketime,), name='乐客联盟')
# leke2 = threading.Thread(target=lekeweb2.run, name='乐客联盟2')
wechatmesg.login()
if '1' in flyg:
    guzi.start()
if '2' in flyg:
    leke.start()
# if '3' in flyg:
#     leke2.start()

initThreadsName = []
init = threading.enumerate()
for i in init:
    initThreadsName.append(i.getName())
check = threading.Thread(target=checkThread, args=(int(retime), initThreadsName,))
check.start()
