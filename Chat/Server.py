import json
import socket
import sys
import threading
import time


def init_config():  # 初始化配置
    '''
    初始化配置
    :return:
    '''
    global config  # 声明全局变量
    config = {"password": "", "ban": [], "needwhitelist": False, "whitelist": []}
    with open('config.json', 'w', encoding='utf-8') as f:
        json.dump(config, f)


def read_config():
    '''
    读取配置
    :return:
    '''
    global config  # 声明全局变量
    with open("config.json", "r") as f:  # 打开配置文件
        config = json.load(f)  # 读取配置文件


def svr_Start():
    '''
    启动服务器
    :return:
    '''
    global s  # 声明全局变量
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket对象
    host = '0.0.0.0'  # 主机名
    port = 15587  # 端口号
    s.bind((host, port))  # 绑定端口
    s.listen(5)  # 监听端口
    print("Server is running on port: " + str(port))  # 打印服务器启动信息
    accept_client()  # 启动接收客户端连接线程


def accept_client():
    '''
    接收客户端连接
    :return:
    '''
    global s  # 声明全局变量
    while True:
        conn, addr = s.accept()  # 接收客户端连接
        t = threading.Thread(target=handle_client, args=(conn, addr))  # 创建线程
        t.daemon = True  # 设置为守护线程
        t.start()  # 启动线程


def handle_msg(conn, addr, name):  # 处理消息
    '''
    处理消息
    :param conn:
    :param addr:
    :param name:
    :return:
    '''
    global connection_list  # 声明全局变量
    while True:
        try:  # 判断是否有异常
            data = conn.recv(1024).decode(encoding='utf-8')  # 接收客户端发送的消息
        except ConnectionResetError:  # 判断是否为连接断开异常
            print("Connection lost from: " + str(addr))  # 打印连接断开信息
            leave_bye(name)  # 发送离开消息
            conn.close()  # 关闭连接
            return
        except ConnectionAbortedError:
            print("Connection lost from: " + str(addr))  # 打印连接断开信息
            leave_bye(name)  # 发送离开消息
            conn.close()  # 关闭连接
            return
        data = eval(data)
        if data['type'] == 'message':
            msg = data['data']
            for i in connection_list:  # 遍历连接列表
                c = connection_list[i]  # 获取连接
                if c != conn:  # 判断连接是否为当前连接
                    c.send(str(data).encode('utf-8'))  # 发送消息
            print('{}: '.format(name) + msg)  # 打印消息
        elif data['type'] == 'svrcmd':
            if data['data'] == 'exit':
                leave_bye(name)  # 发送离开消息
                conn.close()
            elif data['data'] == 'list':
                names = []
                for i in connection_list:
                    names.append(i)
                conn.send('{"type": "userlist", "data": {}'.format(names).encode('utf-8'))  # 发送连接列表


def join_welcome(name, conn):
    '''
    :param name:
    :param conn:
    :return:
    '''
    global connection_list  # 声明全局变量
    for i in connection_list:  # 遍历连接列表
        c = connection_list[i]  # 获取连接
        if c != conn:  # 判断连接是否为当前连接
            temp = '{"type": "welcome", "data": "'+name+' join the server", "from": "Server"}'  # 创建欢迎消息
            c.send(temp.encode('utf-8'))  # 发送消息


def leave_bye(name):
    '''
    :param name:
    :return:
    '''
    global connection_list  # 声明全局变量
    try:
        for i in connection_list:  # 遍历连接列表
            c = connection_list[i]  # 获取连接
            if not i == name:  # 判断连接是否为当前连接
                temp = '{"type": "message", "data": " '+ name + ' left the server", "from": "Server"}'
                c.send(temp.encode('utf-8'))  # 发送消息
                connection_list.pop(name)  # 删除连接
    except RuntimeError:
        pass  # 忽略异常


def handle_client(conn, addr):  # 处理客户端连接
    '''
    处理客户端连接
    :param conn:
    :param addr:
    :return:
    '''
    global config
    global connection_list  # 声明全局变量
    print("New connection from: " + str(addr))  # 打印客户端连接信息
    while True:
        name = conn.recv(1024).decode('utf-8')  # 接收客户端名称
        name = eval(name)
        name = name['data']
        if name == '':  # 判断客户端名称是否为空
            name = 'Anonymous'
            break
        elif name:
            break

    if config['needwhitelist'] == True:
        whitelist = config['whitelist']
        if not name in whitelist:
            conn.send('{"type": "error", "data": "You are not in the whitelist"}'.encode('utf-8'))  # 发送错误消息
            conn.close()
            return
    if name in ban_list:  # 判断客户端名称是否被BAN
        conn.send('{"type": "error", "data": "You has been banned by the server"}'.encode('utf-8'))  # 发送被BAN消息
        conn.close()  # 关闭连接
        return
    if name in connection_list:  # 判断客户端名称是否已存在
        conn.send('{"type": "error", "data": "Name Repeat"}'.encode('utf-8'))  # 发送重复消息
        conn.close()  # 关闭连接
        return
    print("Client name: " + name + "for" + str(addr))  # 打印客户端名称
    connection_list[name] = conn  # 将客户端名称和连接添加到连接列表
    time.sleep(0.5)  # 睡眠0.5秒
    temp = '{"type": "message", "data": "Welcome to the server! Your IP is '+str(addr)+'", "from": "Server"}'# 创建欢迎消息
    conn.send(temp.encode(encoding='utf-8'))  # 发送欢迎消息
    join_welcome(name=name, conn=conn)
    t = threading.Thread(target=handle_msg, args=(conn, addr, name))  # 创建线程
    t.start()  # 启动线程
    print("Message handle start for "+name)  # 打印客户端连接信息


def svr_speak():
    global connection_list
    global config
    whitelist = config['whitelist']
    while True:
        msg = input("->")
        if msg == '/exit':
            try:
                for i in connection_list:  # 遍历连接列表
                    c = connection_list[i]  # 获取连接
                    c.send('{"type": "message", "data": "Server: Shutting down"}'.encode('utf-8'))
                    c.close()
                sys.exit(0)
            except RuntimeError:
                pass
        elif msg == '/list':
            try:
                for i in connection_list:  # 遍历连接列表
                    c = connection_list[i]  # 获取连接
                    print(i, c)
            except RuntimeError:
                print('No client connected')
        elif msg.startswith('/kick') == True:
            try:
                name = msg.split(' ')[1]
                if name in connection_list:
                    c = connection_list[name]
                    c.send('{"type": "error", "data": "You has been kicked out"}'.encode('utf-8'))
                    c.close()
                    connection_list.pop(name)
                else:
                    print('No such client')
            except RuntimeError:
                pass
        elif msg.startswith('/ban') == True:
            try:
                name = msg.split(' ')[1]
                if name in connection_list:
                    c = connection_list[name]
                    c.send('{"type": "error", "data": "You has been banned"}'.encode('utf-8'))
                    c.close()
                    connection_list.pop(name)
                    ban_list.append(name)
                    with open('ban.txt', 'w') as f:
                        f.writelines(ban_list)
                else:
                    print('No such client')
            except RuntimeError:
                pass
        elif msg.startswith('/unban') == True:
            try:
                name = msg.split(' ')[1]
                if name in ban_list:
                    ban_list.remove(name)
                    with open('ban.txt', 'w') as f:
                        f.writelines(ban_list)
                else:
                    print('Name is not in ban list')
            except RuntimeError:
                pass
        elif msg.startswith('/whitelist') == True:
            try:
                name = msg.split(' ')[1]
                if name == 'add':
                    if name in whitelist:
                        print('Name is already in whitelist')
                    else:
                        whitelist.append(name)
                        with open('whitelist.txt', 'w') as f:
                            f.writelines(whitelist)
                elif name == 'remove':
                    if name in whitelist:
                        whitelist.remove(name)
                        with open('whitelist.txt', 'w') as f:
                            f.writelines(whitelist)
                    else:
                        print('Name is not in whitelist')
                elif name == 'list':
                    print(whitelist)
                elif name == 'clear':
                    whitelist.clear()
                    with open('whitelist.txt', 'w') as f:
                        f.writelines(whitelist)
                elif name == 'help':
                    print('add: add name to whitelist')
                    print('remove: remove name from whitelist')
                    print('list: list all names in whitelist')
                    print('clear: clear whitelist')
                elif name == 'activate':
                    config['needwhitelist'] = True
                    with open('config.json', 'w') as f:
                        json.dump(config, f)
                elif name == 'deactivate':
                    config['needwhitelist'] = False
                    with open('config.json', 'w') as f:
                        json.dump(config, f)
            except RuntimeError:
                pass
        else:
            if msg.startswith('/') == True:
                print("Unknown command")
            try:
                for i in connection_list:  # 遍历连接列表
                    c = connection_list[i]  # 获取连接
                    temp = '{"type": "message", "data": "' + msg + '", "from": "Server"}'
                    c.send(temp.encode('utf-8'))
            except RuntimeError:
                pass


def Main():  # 主函数
    '''
    主函数
    :return:
    '''
    read_config()
    t = threading.Thread(target=svr_Start)  # 创建线程
    t.start()  # 启动线程
    t1 = threading.Thread(target=svr_speak)  # 创建线程
    t1.start()  # 启动线程


if __name__ == "__main__":  # 判断是否为主线程
    s = None  # init socket
    connection_list = {}  # init connection list
    config = {}
    try:
        with open("ban.txt", "r") as f:  # open ban file
            ban_list = f.readlines()  # read ban file
    except FileNotFoundError:  # if file not found
        with open("ban.txt", "w") as f:  # create ban file
            print("ban.txt not found, creating...")  # print message
            f.write("")  # write empty string to ban file
            ban_list = []  # init ban list

    try:
        with open("config.json", "r") as f:  # open ip file
            config = f.readlines()  # read ip file
    except FileNotFoundError:  # if file not found
        with open("config.json", "w") as f:  # create ip file
            print("config.json not found, creating...")  # print message
            f.write("")  # write empty string to ip file
        init_config()  # init config file
    Main()  # 调用主函数
