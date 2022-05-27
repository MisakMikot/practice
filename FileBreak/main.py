import sys
import os
import random

def breakExe(value:bytes):
    '''
    this is breakExe function
    :return:
    '''
    string = str(value)
    list = string.split('\\')
    index = random.randint(0,len(list)-1)
    list.remove(list[index])
    result = "".join(list)
    with open("new.exe", "wb") as f:
        f.write(bytes(result, 'utf-8'))

def main(argvs:list):
    '''
    this is main function
    :return:
    '''
    filename = argvs[1]
    fileext = filename.split(".")[-1]
    if fileext == "exe":
        with open(filename, "rb") as f:
            data = f.read()
        breakExe(data)


if __name__ == "__main__":
    argvs = sys.argv
    main(argvs)