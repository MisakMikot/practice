import json
import math
import re
import threading
import time
import tkinter as tk
import tkinter.filedialog
import warnings
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk

import emoji
import requests
import xlwt  # 导入excel官方模块，用于将字典生成excel
from PIL import Image

root = tk.Tk()
warnings.filterwarnings("ignore")


# ----------------------------登录功能函数--------------------------------
def bkn(Skey):
    t = 5381
    n = 0
    o = len(Skey)
    while n < o:
        t += (t << 5) + ord(Skey[n])
        n += 1
    return t & 2147483647


def ptqrtoken(qrsig):
    n = len(qrsig)
    i = 0
    e = 0
    while n > i:
        e += (e << 5) + ord(qrsig[i])
        i += 1
    return 2147483647 & e


def QR():
    url = 'https://ssl.ptlogin2.qq.com/ptqrshow?appid=715030901&e=2&l=M&s=3&d=72&v=4&t=0.' + str(
        time.time()) + '&daid=73&pt_3rd_aid=0'
    r = requests.get(url)
    qrsig = requests.utils.dict_from_cookiejar(r.cookies).get('qrsig')
    with open(r'QQ.png', 'wb') as f:
        f.write(r.content)
    im = Image.open(r'QQ.png')
    im = im.resize((350, 350))
    # print('登录二维码获取成功',time.strftime('%Y-%m-%d %H:%M:%S'))
    im.show()
    return qrsig


def cookies(qrsig, ptqrtoken):
    while 1:
        url = 'https://ssl.ptlogin2.qq.com/ptqrlogin?u1=https%3A%2F%2Fqun.qq.com%2Fmanage.html%23click&ptqrtoken=' + str(
            ptqrtoken) + '&ptredirect=1&h=1&t=1&g=1&from_ui=1&ptlang=2052&action=0-0-' + str(
            time.time()) + '&js_ver=20032614&js_type=1&login_sig=&pt_uistyle=40&aid=715030901&daid=73&'
        cookies = {'qrsig': qrsig}
        r = requests.get(url, cookies=cookies)
        r1 = r.text
        if '二维码未失效' in r1:
            # print('二维码未失效',time.strftime('%Y-%m-%d %H:%M:%S'))
            pass
        elif '二维码认证中' in r1:
            # print('二维码认证中',time.strftime('%Y-%m-%d %H:%M:%S'))
            pass
        elif '二维码已失效' in r1:
            # print('二维码已失效',time.strftime('%Y-%m-%d %H:%M:%S'))
            # 重新获取二维码
            # qrsig = QR()
            pass
        else:
            # print('登录成功',time.strftime('%Y-%m-%d %H:%M:%S'))
            cookies = requests.utils.dict_from_cookiejar(r.cookies)
            # print(cookies)
            uin = requests.utils.dict_from_cookiejar(r.cookies).get('uin')
            regex = re.compile(r'ptsigx=(.*?)&')
            sigx = re.findall(regex, r.text)[0]
            url = 'https://ptlogin2.qun.qq.com/check_sig?pttype=1&uin=' + uin + '&service=ptqrlogin&nodirect=0&ptsigx=' + sigx + '&s_url=https%3A%2F%2Fqun.qq.com%2Fmanage.html&f_url=&ptlang=2052&ptredirect=101&aid=715030901&daid=73&j_later=0&low_login_hour=0&#174;master=0&pt_login_type=3&pt_aid=0&pt_aaid=16&pt_light=0&pt_3rd_aid=0'
            r2 = requests.get(url, cookies=cookies, allow_redirects=False)
            targetCookies = requests.utils.dict_from_cookiejar(r2.cookies)
            skey = requests.utils.dict_from_cookiejar(r2.cookies).get('skey')
            break
        time.sleep(3)
    return targetCookies, skey


join_qun = {}
create_qun = {}
manage_qun = {}


def qun(cookies, bkn, num):
    url = 'https://qun.qq.com/cgi-bin/qun_mgr/get_group_list'
    data = {'bkn': bkn}
    cookies = cookies
    # print(cookies)
    r = requests.post(url, data=data, cookies=cookies)
    # --------------------传出去一个res的值，用于后面获取群列表的操作----------------
    res = r.text
    res = res.encode('utf-8', 'replace').decode()
    res1 = json.loads(res)
    global join_qun
    global create_qun
    global manage_qun
    if "create" in res1:
        create_qun = res1['create']
    else:
        create_qun = {}
    if "join" in res1:
        join_qun = res1['join']
    else:
        join_qun = {}
    if "manage" in res1:
        manage_qun = res1['manage']
    else:
        manage_qun = {}
    # --------------------传出去一个res的值，用于后面获取群列表的操作----------------

    regex = re.compile(r'"gc":(\d+),"gn')
    r = re.findall(regex, r.text)
    return cookies


# ----------------------------登录功能函数--------------------------------
# ----------------------------群功能函数----------------------------------
def load_data(st, end):  # 加载数据需要传入st开始位置和end结束位置
    url = 'https://qun.qq.com/cgi-bin/qun_mgr/search_group_members'

    def str_cookie(state):
        str1 = ''
        for i in state:
            str1 = str1 + i + '=' + state[i] + '; '
        return str1

    cookie = str_cookie(state)
    # print('cookie='+cookie)
    headers = {
        "cookie": cookie
    }

    def get_bkn():  # 从QQ群中获取bkn函数
        e = state['skey']
        t = 5381
        n = 0
        o = len(e)
        while n < o:
            t += (t << 5) + ord(e[n])
            n += 1
        return (2147483647 & t)

    # print(get_bkn())
    # gc = input('请输入要查询的群号:')
    global gc
    gc = show_qqqun_number()  # 群号
    data = {
        "gc": gc,
        "st": st,
        "end": end,
        "sort": "0",
        "bkn": get_bkn()
    }

    response = requests.post(url, data=data, headers=headers, verify=False)
    response = response.text
    response = response.encode('utf-8').decode("unicode_escape")
    return response


def get_qq_member_count():  # 获取群成员数量函数
    response = load_data(0, 0)
    qq_member_count = json.loads(response)['count']  # qq群人数
    # print(qq_member_count)
    return qq_member_count


qq_qun_info = []


def get_qq_member_list():  # 获取群成员列表函数
    global qq_qun_info  # 全局变量qq群信息列表
    qq_qun_info = []
    count = math.ceil(get_qq_member_count() / 21)  # 需要循环的次数
    # print('需要循环的次数：'+str(count))
    n = 0  # 用于计数
    j = 0  # 计数器用于判断当前循环的次数
    num = 1  # 用于给字典里的信息加序号
    while j < count:
        # load_data()参数的取值 第一次是从1到20 第二次是从21到42 第三次是从43到63以此类推保证不获取重复值
        response = load_data(n + j, n + 20 + j)
        res = json.loads(response)['mems']
        # print('res='+str(res))
        qq_name = ''  # qq名字
        qq_qun_name = ''  # qq群名字
        qq_number = ''  # qq号码
        sex = ''  # 性别
        qq_age = ''  # q龄
        join_qun_time = ''  # 入群时间
        last_speak_time = ''  # 最后一次发言
        for i in res:
            qq_name = i['nick']
            # 替换qq昵称中的\为空
            qq_name = filter_emoji(qq_name, '??????')

            qq_qun_name = i['card']
            # 替换qq群昵称中的\为空
            qq_qun_name = filter_emoji(qq_qun_name, '??????')

            qq_number = str(i['uin'])

            sex = i['g']  # 如果sex = 0则为男性, sex = -1未知, sex = 1为女性
            if sex == 0:
                sex = '男'
            elif sex == 1:
                sex = '女'
            elif sex == -1:
                sex = '未知'
            else:
                sex = '错误'

            qq_age = i['qage']
            join_qun_time = i['join_time']  # 这里返回的是10位整数
            last_speak_time = i['last_speak_time']
            # 将以上内容加入字典dict1中
            dict1 = {}
            dict1['num'] = num
            dict1["qq_name"] = qq_name
            dict1["qq_qun_name"] = qq_qun_name
            dict1["qq_number"] = qq_number
            dict1["sex"] = sex
            dict1["qq_age"] = qq_age
            # 将十位数入群时间转为正常时间
            join_qun_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(join_qun_time))
            dict1["join_qun_time"] = join_qun_time
            # 将十位数最后一次发言时间转为正常时间
            last_speak_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(last_speak_time))
            dict1["last_speak_time"] = last_speak_time
            # 将字典dict1加入列表qq_qun_info列表中
            qq_qun_info.append(dict1)

            if select_var.get() == 0:
                table.insert('', 'end',
                             values=(num, qq_name, qq_qun_name, qq_number, sex, qq_age, join_qun_time, last_speak_time))
                # 滚动到table的最下方

                # 打印输出日志 由于num是从1开始的 但是列表是从0计数，所以此处num-1
                scroll.insert(END, "\n" + str(qq_qun_info[num - 1]))
                scroll.see("end")
                # print(qq_qun_info[num-1]) 

            num = num + 1
        j = j + 1
        n += 20
    # print(qq_qun_info)

    member_count = get_qq_member_count()
    if member_count > 0:
        if (select_var.get() == 1):  # 选中
            messagebox.showinfo('提示', '查询到' + str(member_count) + '个好友数据，正在扫描后四位信息，此过程可能会比较漫长，请耐心等待...')
            from_qq_get_info()  # 调用查后四位数据的函数
            messagebox.showinfo('提示', '导入完成，一共导入' + str(member_count) + '个好友数据')
        else:
            messagebox.showinfo('提示', '查询到' + str(member_count) + '个好友数据')
    else:
        messagebox.showinfo('提示', '没有查询到任何好友数据')

    return qq_qun_info
    # print(qq_qun_info) #显示群成员列表


# 利用qq号码获取更多信息，此方法耗时严重，不建议使用
def from_qq_get_info():
    time.sleep(2)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    }
    for i in qq_qun_info:
        url = 'https://zy.xywlapi.cc/qqcx?qq=' + i['qq_number']
        response = requests.get(url, headers=headers)
        response = response.text
        response = json.loads(response)
        # print(response)
        if response['status'] == 200:
            qq_qun_info[qq_qun_info.index(i)]['phone'] = response['phone']
            qq_qun_info[qq_qun_info.index(i)]['diqu'] = response['phonediqu']
            qq_qun_info[qq_qun_info.index(i)]['lol'] = response['lol']
            qq_qun_info[qq_qun_info.index(i)]['wb'] = response['wb']
        else:
            qq_qun_info[qq_qun_info.index(i)]['phone'] = '未知'
            qq_qun_info[qq_qun_info.index(i)]['diqu'] = '未知'
            qq_qun_info[qq_qun_info.index(i)]['lol'] = '未知'
            qq_qun_info[qq_qun_info.index(i)]['wb'] = '未知'

        table.insert('', 'end', values=(
            i['num'], i['qq_name'], i['qq_qun_name'], i['qq_number'], i['sex'], i['qq_age'], i['join_qun_time'],
            i['last_speak_time'], i['phone'], i['diqu'], i['lol'], i['wb']))

        def log():
            scroll.insert(END, "\n" + str(qq_qun_info[qq_qun_info.index(i)]))
            scroll.see("end")

        # print(qq_qun_info[qq_qun_info.index(i)])
        threading.Thread(target=log).start()


def export_excel(export):  # 将qq_qun_info列表保存为excel函数
    '''
    #将字典列表转换为DataFrame
    pf = pd.DataFrame(list(export))
    #指定字段顺序
    if select_var.get() == 1:
        order = ['num','qq_name','qq_qun_name','qq_number','sex','qq_age','join_qun_time','last_speak_time','phone','diqu','lol','wb']
    else:
        order = ['num','qq_name','qq_qun_name','qq_number','sex','qq_age','join_qun_time','last_speak_time']
    pf = pf[order]
    #将列名替换为中文
    columns_map = {
        'num':'序号',
        'qq_name':'qq昵称',
        'qq_qun_name':'qq群昵称',
        'qq_number':'qq号码',
        'sex':'性别',
        'qq_age':'Q龄',
        'join_qun_time':'入群时间',
        'last_speak_time':'最近发言时间',
        'phone':'手机号',
        'diqu':'地区',
        'lol':'lol',
        'wb':'微博UID'
    }
    pf.rename(columns = columns_map,inplace = True)
    #指定生成的Excel表格名称
    file_path = pd.ExcelWriter(save_path+'.xlsx')
    #替换空单元格
    pf.fillna(' ',inplace = True)
    #输出
    pf.to_excel(file_path,encoding = 'utf-8',index = False)
    #保存表格
    file_path.save()
    '''
    wb = xlwt.Workbook(encoding='utf-8')  # 开始创建excel
    # style = xlwt.XFStyle()  # 初始化样式
    # style.alignment.wrap = 1  # 自动换行

    SHEET = wb.add_sheet('test', cell_overwrite_ok=True)  # excel中的表名
    SHEET.write(0, 0, '序号')  # 列名
    wid0 = SHEET.col(0)  # 设置第一个格的宽度
    wid0.width = 20 * 80
    SHEET.write(0, 1, 'QQ昵称')
    wid1 = SHEET.col(1)  # 设置第二个格的宽度
    wid1.width = 80 * 80
    SHEET.write(0, 2, 'QQ群昵称')
    wid2 = SHEET.col(2)  # 设置第二个格的宽度
    wid2.width = 80 * 80
    SHEET.write(0, 3, 'QQ号')
    wid3 = SHEET.col(3)  # 设置第二个格的宽度
    wid3.width = 50 * 80
    SHEET.write(0, 4, '性别')
    wid4 = SHEET.col(4)  # 设置第二个格的宽度
    wid4.width = 20 * 80
    SHEET.write(0, 5, 'Q龄')
    wid5 = SHEET.col(5)  # 设置第二个格的宽度
    wid5.width = 20 * 80
    SHEET.write(0, 6, '入群时间')
    wid6 = SHEET.col(6)  # 设置第二个格的宽度
    wid6.width = 60 * 80
    SHEET.write(0, 7, '最近发言时间')
    wid7 = SHEET.col(7)  # 设置第二个格的宽度
    wid7.width = 60 * 80
    SHEET.write(0, 8, '手机号')
    wid8 = SHEET.col(8)  # 设置第二个格的宽度
    wid8.width = 40 * 80
    SHEET.write(0, 9, '地区')
    wid9 = SHEET.col(9)  # 设置第二个格的宽度
    wid9.width = 80 * 80
    SHEET.write(0, 10, 'LOL')
    wid10 = SHEET.col(10)  # 设置第二个格的宽度
    wid10.width = 80 * 80
    SHEET.write(0, 11, '微博UID')
    wid11 = SHEET.col(11)  # 设置第二个格的宽度
    wid11.width = 50 * 80
    row = 1
    for i in export:
        for key, value in i.items():
            if key == "num":
                SHEET.write(row, 0, value)
            elif key == "qq_name":
                SHEET.write(row, 1, value)
            elif key == "qq_qun_name":
                SHEET.write(row, 2, value)
            elif key == "qq_number":
                SHEET.write(row, 3, value)
            elif key == "sex":
                SHEET.write(row, 4, value)
            elif key == "qq_age":
                SHEET.write(row, 5, value)
            elif key == "join_qun_time":
                SHEET.write(row, 6, value)
            elif key == "last_speak_time":
                SHEET.write(row, 7, value)
            elif key == "phone":
                SHEET.write(row, 8, value)
            elif key == "diqu":
                SHEET.write(row, 9, value)
            elif key == "lol":
                SHEET.write(row, 10, value)
            elif key == "wb":
                SHEET.write(row, 11, value)
        row += 1
    wb.save(save_path + '.xls')


# 过滤特殊字符函数
def filter_emoji(desstr, restr=''):
    # desstr是要过滤的字符串
    # restr是替换的字符串
    # 过滤表情
    res = re.compile(u'[\U00010000-\U0010ffff\\uD800-\\uDBFF\\uDC00-\\uDFFF]')
    return res.sub(restr, desstr)


# ----------------------------群功能函数----------------------------------

# ----------------------------获取群列表----------------------------------
def get_allqun_list(group_name):  ####修改这里####修改这里####修改这里####修改这里####修改这里####修改这里
    if group_name == '我创建的群':
        # print('create_qun:',create_qun)
        return create_qun
    if group_name == '我加入的群':
        # print('join_qun:',join_qun)
        return join_qun
    if group_name == '我管理的群':
        # print('manage_qun:',manage_qun)
        return manage_qun


# ----------------------------获取群列表----------------------------------

# ----------------------------界面----------------------------------
label1 = tk.Label(root, text='QQ群号:')
label1.place(x=150, y=10)
label1.config(font=('微软雅黑', 12))
# -------------------------选择相应的分组----------------------------------
qq_qun_gc = []
qq_qun_gn = []


def show_group(*arg):
    global qq_qun_gc
    global qq_qun_gn
    qq_qun_gc = []
    qq_qun_gn = []
    all_qun1 = get_allqun_list(value_group.get())
    # print(all_qun1)
    for i in all_qun1:
        qq_qun_gc.append(i['gc'])
        gn = emoji.demojize(i['gn'])
        gn = re.sub(emoji.get_emoji_regexp(), r"?", gn)
        gn = filter_emoji(gn, '?')
        qq_qun_gn.append(gn)
    # print(qq_qun_gc)
    # print(qq_qun_gn)
    # 下拉列表框中的值
    xiala_list["values"] = qq_qun_gn
    xiala_list.current(0)


value_group = StringVar()
# 定义一个下拉列表
data_group = ["我创建的群", "我管理的群", "我加入的群"]
# if create_qun =={}:
#     data_group.remove('我创建的群')
# if join_qun =={}:
#     data_group.remove('我加入的群')
# if manage_qun =={}:
#     data_group.remove('我管理的群')
# 创建一个下拉列表
group_list = ttk.Combobox(root, width=10, height=10, textvariable=value_group, state="readonly")
# 设置字体
group_list.config(font=('微软雅黑', 12))
group_list.bind("<<ComboboxSelected>>", show_group)  # 事件的绑定
group_list.place(x=230, y=10)
# 下拉列表框中的值
group_list["values"] = data_group


# -------------------------选择相应的分组----------------------------------

# -------------------------对应分组的群号----------------------------------
def show_qqqun_number(*arg):
    index1 = xiala_list.current()
    qq_qun_num = qq_qun_gc[index1]
    # print(qq_qun_num)
    return qq_qun_num


value = StringVar()
# 创建一个下拉列表
xiala_list = ttk.Combobox(root, width=13, height=10, textvariable=value)
# 设置字体
xiala_list.config(font=('微软雅黑', 12))
xiala_list.place(x=360, y=10)
# -------------------------对应分组的群号----------------------------------

screenwidth = root.winfo_screenwidth()  # 屏幕宽度
screenheight = root.winfo_screenheight()  # 屏幕&#12220;度
width = 1000
height = 500
x = int((screenwidth - width) / 2)
y = int((screenheight - height) / 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # &#12068;&#12073;以及位置
xscroll = Scrollbar(root, orient=HORIZONTAL)
yscroll = Scrollbar(root, orient=VERTICAL)
columns = ['序号', 'qq昵称', 'qq群昵称', 'qq号码', '性别', 'Q龄', '入群时间', '最近发言时间', '手机号', '地区', 'lol', '微博UID']
table = ttk.Treeview(
    master=root,  # &#12119;容器
    height=20,  # 表格显&#12144;的&#12175;数,height&#12175;
    columns=columns,  # 显&#12144;的列
    show='headings',  # 隐藏&#12216;列
    xscrollcommand=xscroll.set,  # x轴滚动条
    yscrollcommand=yscroll.set,  # y轴滚动条
)
xscroll.config(command=table.xview)
xscroll.pack(side=BOTTOM, fill=X)
yscroll.config(command=table.yview)
yscroll.pack(side=RIGHT, fill=Y)
table.pack(fill=BOTH, expand=True)
table.heading(column='序号', text='序号', anchor='w',
              command=lambda: print('序号'))  # 定义表头
table.heading('qq昵称', text='qq昵称', )  # 定义表头
table.heading('qq群昵称', text='qq群昵称', )  # 定义表头
table.heading('qq号码', text='qq号码', )  # 定义表头
table.heading('性别', text='性别', )  # 定义表头
table.heading('Q龄', text='Q龄', )  # 定义表头
table.heading('入群时间', text='入群时间', )  # 定义表头
table.heading('最近发言时间', text='最近发言时间', )  # 定义表头
table.heading('手机号', text='手机号', )  # 定义表头
table.heading('地区', text='地区', )  # 定义表头
table.heading('lol', text='lol', )  # 定义表头
table.heading('微博UID', text='微博UID', )  # 定义表头
table.column('序号', width=50, minwidth=50, anchor=S, )  # 定义列
table.column('qq昵称', width=100, minwidth=100, anchor=S)  # 定义列
table.column('qq群昵称', width=100, minwidth=100, anchor=S)  # 定义列
table.column('qq号码', width=100, minwidth=100, anchor=S)  # 定义列
table.column('性别', width=50, minwidth=50, anchor=S)  # 定义列
table.column('Q龄', width=50, minwidth=50, anchor=S)  # 定义列
table.column('入群时间', width=150, minwidth=150, anchor=S)  # 定义列
table.column('最近发言时间', width=150, minwidth=150, anchor=S)  # 定义列
table.column('手机号', width=100, minwidth=100, anchor=S)  # 定义列
table.column('地区', width=100, minwidth=100, anchor=S)  # 定义列
table.column('lol', width=100, minwidth=100, anchor=S)  # 定义列
table.column('微博UID', width=100, minwidth=100, anchor=S)  # 定义列
table.place(x=10, y=50)

# 添加一个命令输出框 log
scroll = scrolledtext.ScrolledText(root, width=164, height=14, font=('黑体', 10))


def Scroll(root):
    scroll.place(x=10, y=480)


Scroll(root)

# ----------------------------操作数据------------------------------
# 添加一个复选框
select_var = IntVar()
select = Checkbutton(root, text='查询后四位数据(耗时)', variable=select_var)
select.place(x=520, y=10)


def chaxun():
    # 清空Scroll中的全部内容
    scroll.delete(1.0, END)
    # 清除table中的数据
    table.delete(*table.get_children())
    # 设置查询的线程
    threading.Thread(target=get_qq_member_list).start()


# 添加一个btn1按钮
btn1 = tk.Button(root, text='查询', command=chaxun)
btn1.config(font=('微软雅黑', 9))
btn1.config(width=8)
btn1.place(x=680, y=10)


def save():
    export_excel(qq_qun_info)
    messagebox.showinfo('提示', '保存成功')


save_path = ''


def FileSave():
    global save_path
    save_path = tkinter.filedialog.asksaveasfilename(title='保存', initialfile=value.get(),
                                                     filetypes=[('excel', '*.xlsx')])
    # 如果用户点击了保存按钮则返回保存的文件名
    if save_path:
        save()
    else:
        messagebox.showinfo('提示', '取消保存')


# 添加一个btn2按钮
btn2 = tk.Button(root, text='保存表格', command=FileSave)
btn2.config(font=('微软雅黑', 9))
btn2.config(width=8)
btn2.place(x=770, y=10)

# ----------------------------操作数据------------------------------

# ----------------------------界面----------------------------------

if __name__ == '__main__':
    # ---------------只调试界面请注释本段代码----------------
    global state
    qrsig = QR()
    ptqrtoken = ptqrtoken(qrsig)
    cookie = cookies(qrsig, ptqrtoken)
    skey = cookie[1]
    bkn = bkn(skey)
    ck = cookie[0]
    state = qun(ck, bkn, '434252251')  # 获取的cookie
    # ---------------只调试界面请注释本段代码----------------
    # root.iconbitmap('imgs/favicon.ico')
    root.geometry('1190x700')
    root.title("QQ群信息爬取")
    root.resizable(False, False)
    root.mainloop()
