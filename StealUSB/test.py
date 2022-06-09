import time
import psutil
import os
res = []
#  设置休眠时间
time.sleep(1)
data = os.popen("wmic VOLUME GET Label").read()
list = data.split('\n')
l2 = []
for i in list:
    a = i.replace(' ', '')
    if a == '':
        pass
    else:
        l2.append(a)
l2.pop(0)
#  检测所有的驱动器，进行遍历寻找哦
for i in psutil.disk_partitions():
    driver, opts = i.device, i.opts
    print(driver)
    res.append({"letter": driver})
a = 0
for i in l2:
    res[a]["label"] = i
    a += 1
print(res)
