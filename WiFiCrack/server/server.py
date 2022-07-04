import socket
import sys
import threading
import json
import time
import sqlite3
import os
import dbtool


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

def handle_client(conn, addr):  # 处理客户端连接
    '''
    处理客户端连接
    :param conn:
    :param addr:
    :return:
    '''
    print("New connection from: " + str(addr))  # 打印客户端连接信息
    t = threading.Thread(target=handle_msg, args=(conn, addr))  # 创建线程
    t.start()  # 启动线程

def handle_msg(conn, addr):
    global db
    while True:
        try:
            data = conn.recv(1024)  # 接收客户端发送的数据
        except:
            print("Connection lost from: " + str(addr))  # 打印客户端断开连接信息
            conn.close()  # 关闭连接
            break
        data = eval(data)  # 将字符串转换为字典
        if data['type'] == 'search':  # 如果消息类型为查询
            msg = data['data']['SSID']  # 获取查询内容
            print('Searching for: ' + str(msg))  # 打印查询内容
            result = db.search(msg)  # 获取查询结果
            if len(result) == 0:  # 如果查询结果为空
                temp = '{"type": "error", "data": "No result"}'  # 创建查询结果消息
            else:
                temp = '{"type": "result", "data": "' + str(result) + '"}'  # 创建查询结果消息
            conn.send(temp.encode(encoding='utf-8'))  # 发送查询结果消息
        elif data['type'] == 'add':  # 如果消息类型为添加
            for i in data['data']:  # 循环添加消息
                db.add(i[0], i[1])  # 添加消息


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




def main():
    global db # 声明全局变量
    if os.path.isfile('data.db'):
        db = dbtool.dbtool('data.db')
    else:
        db = dbtool.dbtool('data.db')
        db.init()
    t = threading.Thread(target=svr_Start)  # 创建线程
    t.start()  # 启动线程

if __name__ == '__main__':
    db = None
    main()