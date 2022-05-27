import socket
import os
import random
import sys
import threading
import time

s = None # init socket
connection_list = {} # init connection list
try:
    with open("ban.txt", "r") as f: # open ban file
        ban_list = f.readlines() # read ban file
except FileNotFoundError: # if file not found
    with open("ban.txt", "w") as f: # create ban file
        print("ban.txt not found, creating...") # print message
        f.write("") # write empty string to ban file
        ban_list = [] # init ban list

def svr_Start():
    '''
    启动服务器
    :return:
    '''
    global s # 声明全局变量
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 创建socket对象
    host = '0.0.0.0' # 主机名
    port = 15587 # 端口号
    s.bind((host, port)) # 绑定端口
    s.listen(5) # 监听端口
    print("Server is running on port: " + str(port)) # 打印服务器启动信息
    accept_client() # 启动接收客户端连接线程

def accept_client():
    '''
    接收客户端连接
    :return:
    '''
    global s # 声明全局变量
    while True:
        conn, addr = s.accept() # 接收客户端连接
        t = threading.Thread(target=handle_client, args=(conn, addr)) # 创建线程
        t.daemon = True # 设置为守护线程
        t.start() # 启动线程

def handle_msg(conn, addr, name): # 处理消息
    '''
    处理消息
    :param conn:
    :param addr:
    :param name:
    :return:
    '''
    global connection_list # 声明全局变量
    while True:
        try: # 判断是否有异常
            data = conn.recv(1024).decode(encoding='utf-8') # 接收客户端发送的消息
        except ConnectionResetError: # 判断是否为连接断开异常
            print("Connection lost from: " + str(addr)) # 打印连接断开信息
            leave_bye(name) # 发送离开消息
            conn.close() # 关闭连接
            return
        except ConnectionAbortedError:
            print("Connection lost from: " + str(addr)) # 打印连接断开信息
            leave_bye(name) # 发送离开消息
            conn.close() # 关闭连接
            return
        data = "From {}: {}".format(name, data) # 拼接消息
        print(data) # 打印消息
        if data == '/exit': # 判断消息是否为退出消息
            conn.close() # 关闭连接
        for i in connection_list: # 遍历连接列表
            c = connection_list[i] # 获取连接
            if c != conn: # 判断连接是否为当前连接
                c.send(data.encode('utf-8')) # 发送消息

def join_welcome(name, conn):
    '''
    :param name:
    :param conn:
    :return:
    '''
    global connection_list # 声明全局变量
    for i in connection_list:  # 遍历连接列表
        c = connection_list[i]  # 获取连接
        if c != conn:  # 判断连接是否为当前连接
            c.send("{} join the server".format(name).encode('utf-8'))  # 发送消息

def leave_bye(name):
    '''
    :param name:
    :return:
    '''
    global connection_list # 声明全局变量
    try:
        for i in connection_list:  # 遍历连接列表
            c = connection_list[i]  # 获取连接
            if not i == name: # 判断连接是否为当前连接
                c.send("{} left the server".format(name).encode('utf-8'))  # 发送消息
                connection_list.pop(name) # 删除连接
    except RuntimeError:
        pass # 忽略异常

def handle_client(conn, addr): # 处理客户端连接
    '''
    处理客户端连接
    :param conn:
    :param addr:
    :return:
    '''
    global connection_list # 声明全局变量
    print("New connection from: " + str(addr)) # 打印客户端连接信息
    while True:
        name = conn.recv(1024).decode('utf-8') # 接收客户端名称
        if name != '': # 判断客户端名称是否为空
            break
    if name in ban_list: # 判断客户端名称是否被BAN
        conn.send('This username has been banned by the server'.encode('utf-8')) # 发送被BAN消息
        conn.close() # 关闭连接
        return
    if name in connection_list: # 判断客户端名称是否已存在
        conn.send('name repeat'.encode('utf-8')) # 发送重复消息
        conn.close() # 关闭连接
        return
    connection_list[name] = conn # 将客户端名称和连接添加到连接列表
    time.sleep(1) # 睡眠1秒
    conn.send(("Welcome to the server!"+"Your IP is {}").format(addr).encode(encoding='utf-8')) # 发送欢迎消息
    join_welcome(name=name,conn=conn)
    t = threading.Thread(target=handle_msg, args=(conn, addr, name)) # 创建线程
    t.start() # 启动线程

def svr_speak():
    global connection_list
    while True:
        msg = input()
        if msg == '/exit':
            try:
                for i in connection_list:  # 遍历连接列表
                    c = connection_list[i]  # 获取连接
                    c.send("Server: shutting down".encode('utf-8'))
                    c.close()
                    sys.exit(0)
            except RuntimeError:
                pass
        elif msg == '/list':
            try:
                for i in connection_list:  # 遍历连接列表
                    c = connection_list[i]  # 获取连接
                    print(i,c)
            except RuntimeError:
                print('No client connected')
        elif msg.startswith('/kick') == True:
            try:
                name = msg.split(' ')[1]
                if name in connection_list:
                    c = connection_list[name]
                    c.send('Server: You have been kicked out'.encode('utf-8'))
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
                    c.send('Server: You have been banned'.encode('utf-8'))
                    c.close()
                    connection_list.pop(name)
                    ban_list.append(name)
                    with open('ban.txt','w') as f:
                        f.writelines(ban_list)
                else:
                    print('No such client')
            except RuntimeError:
                pass
        else:
            if msg.startswith('/') == True:
                print("Unknown command")
            try:
                for i in connection_list:  # 遍历连接列表
                    c = connection_list[i]  # 获取连接
                    c.send("Server: {}".format(msg).encode('utf-8'))
            except RuntimeError:
                pass


def Main(): # 主函数
    '''
    主函数
    :return:
    '''
    t = threading.Thread(target=svr_Start) # 创建线程
    t.start() # 启动线程
    t1 = threading.Thread(target=svr_speak) # 创建线程
    t1.start() # 启动线程



if __name__ == "__main__": # 判断是否为主线程
    Main() # 调用主函数