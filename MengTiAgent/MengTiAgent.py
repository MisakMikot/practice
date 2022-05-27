# -*- coding: UTF-8 -*-
import random
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def modeSelect():
    welcome = '蒙题助手v0.1.0!'
    print(welcome)
    modes = '1、四位选择题\n2、七选六'
    print(modes)
    mode = input('请你选择蒙题模式:')
    if mode == '1':
        clear()
        print('结果:', *mode1(input('请输入总共的题数：')), sep='')
        modeSelect()
    elif mode == '2':
        clear()
        print('结果:', *mode2(), sep='')
        modeSelect()
    else:
        clear()
        print('输入不合法，请重新输入！')
        modeSelect()


def mode2():
    list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    random.shuffle(list)
    list.pop()
    return list


def mode1(times):
    result = []
    try:
        times = int(times)
    except Exception as e:
        return e
    for i in range(0, times):
        list = ['A', 'B', 'C', 'D']
        temp = random.choice(list)
        result.append(temp)
    return result


clear()
modeSelect()
