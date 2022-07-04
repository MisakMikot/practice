import socket
import sys
import os
import time

import pywifi
import subprocess
from pywifi import const # 引入一个常量

class client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #try:
        self.sock.connect((self.host, self.port))
        '''except:
            print('Connection failed')
            return'''
        self.wifi = pywifi.PyWiFi() # create a PyWiFi object
        self.ifaces = self.wifi.interfaces()[0] # get the first interface

    def cls(self):
        if sys.platform == "win32" or sys.platform == "win64":
            os.system("cls")
        elif sys.platform == "linux" or sys.platform == "linux2":
            os.system("clear")

    def main(self):
        self.cls()
        text = '''    ____  ___   ___________       ______  ____  ____             
           / __ \/   | / ___/ ___/ |     / / __ \/ __ \/ __ \            
          / /_/ / /| | \__ \\__ \| | /| / / / / / /_/ / / / /            
         / ____/ ___ |___/ /__/ /| |/ |/ / /_/ / _, _/ /_/ /             
        /_/___/_/__|_/____/____/ |__/|__/\____/_/ |_/_____/______________
          / ___// ____/ __ \ |  / / ____/ __ \   /_  __/ ____/ ___/_  __/
          \__ \/ __/ / /_/ / | / / __/ / /_/ /    / / / __/  \__ \ / /   
         ___/ / /___/ _, _/| |/ / /___/ _, _/    / / / /___ ___/ // /    
        /____/_____/_/ |_| |___/_____/_/ |_|    /_/ /_____//____//_/     '''
        print(text)
        print('\n')
        print('1. Search WiFi password')
        print('2. Upload WiFi password')
        print('3. Exit')
        print('\n')
        choice = input('Enter your choice: ')
        if choice == '1':
            self.cls()
            self.ifaces.scan()  # 扫描WiFi
            self.result = self.ifaces.scan_results()  # get the scan results
            print('0. I want to input manually')
            for i in range(len(self.result)):  # for each WiFi in the scan results
                a = i + 1
                print(str(a) + '. ', self.result[i].ssid, 'Signal:',
                      self.result[i].signal)  # print the WiFi name and signal strength
            print('\n')  # print a new line
            wifiindex = int(input('Select a WiFi network to search: '))
            if wifiindex == 0:
                self.cls()
                SSID = input('Enter the SSID: ')
            else:
                self.cls()
                SSID = self.result[wifiindex - 1].ssid
            self.result = self.search(SSID)
            if self.result == None:
                print('No password found')
            else:
                print('Password found!')
                print(self.result)
            print('\nPress any key to continue...')
            os.system('pause >nul')
            self.main()
        elif choice == '2':
            self.cls()
            self.upload()
            print('Upload success!')
            time.sleep(1)
            self.main()


    def upload(self):
        msg = '{"type": "add", "data": '+str(self.getWifiAndPassword())+'}'
        self.sock.send(msg.encode('utf-8'))

    def getWifiAndPassword(self):
        self.list = []
        # 获取wifi列表
        self.output = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True).stdout.decode('gbk').split('\n')
        self.wifis = [line.split(':')[1][1:-1] for line in self.output if "所有用户配置文件" in line]
        # 查看每个wifi对应的密码
        for wifi in self.wifis:
            self.results = subprocess.run(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear'],
                                     capture_output=True).stdout.decode('gbk', errors='ignore').split('\n')
            self.results = [line.split(':')[1][1:-1] for line in self.results if "关键内容" in line]
            try:
                self.list.append([wifi, self.results[0]])
            except IndexError:
                pass
        return self.list

    def search(self, SSID):
        msg = '{"type": "search", "data": {"SSID": "' + SSID + '"}}'
        self.sock.send(msg.encode('utf-8'))
        data = self.sock.recv(1024).decode('utf-8')
        print(data)
        data = eval(data)

        if data['type'] == 'error':
            print('Error: ' + data['data'])
            return None
        elif data['type'] == 'result':
            return data['data']