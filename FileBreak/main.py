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

def breakDoc(value:bytes):
    '''
    this is breakDoc function
    :return:
    '''
    string = str(value)
    result = string.replace('word','fakeword')
    if fileext == 'docx':
        with open("new.docx", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'doc':
        with open("new.doc", "wb") as f:
            f.write(bytes(result, 'utf-8'))

def breakVideo(value:bytes):
    '''
    this is breakVideo function
    :return:
    '''
    string = str(value)
    list = string.split('\\')
    index = random.randint(0,len(list)-1)
    list.remove(list[index])
    result = "".join(list)
    if fileext == 'mp4':
        with open("new.mp4", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'avi':
        with open("new.avi", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'mkv':
        with open("new.mkv", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'flv':
        with open("new.flv", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'mpg':
        with open("new.mpg", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'wmv':
        with open("new.wmv", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'mov':
        with open("new.mov", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == '3gp':
        with open("new.3gp", "wb") as f:
            f.write(bytes(result, 'utf-8'))

def breakAudio(value:bytes):
    '''
    this is breakAudio function
    :return:
    '''
    string = str(value)
    list = string.split('\\')
    index = random.randint(0,len(list)-1)
    list.remove(list[index])
    result = "".join(list)
    if fileext == 'mp3':
        with open("new.mp3", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'wav':
        with open("new.wav", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'flac':
        with open("new.flac", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'ogg':
        with open("new.ogg", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'aac':
        with open("new.aac", "wb") as f:
            f.write(bytes(result, 'utf-8'))

def breakArc(value:bytes):
    '''
    this is breakArc function
    :return:
    '''
    string = str(value)
    list = string.split('\\')
    index = random.randint(0, len(list) - 1)
    list.remove(list[index])
    result = "".join(list)
    if fileext == 'zip':
        with open("new.zip", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'rar':
        with open("new.rar", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == '7z':
        with open("new.7z", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'tar':
        with open("new.tar", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'gz':
        with open("new.gz", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'bz2':
        with open("new.bz2", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'xz':
        with open("new.xz", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'tar.gz':
        with open("new.tar.gz", "wb") as f:
            f.write(bytes(result, 'utf-8'))

def main(argvs:list):
    '''
    this is main function
    :return:
    '''
    global fileext
    filename = argvs[1]
    fileext = filename.split(".")[-1]
    if fileext == "exe":
        confirm = input("Do you want to break this executable?(y/n)")
        if confirm == "y":
            with open(filename, "rb") as f:
                value = f.read()
                breakExe(value)
                print("Successfully broken")
        else:
            print("Canceled")
    elif fileext == "doc" or fileext == "docx":
        confirm = input("Do you want to break this document?(y/n)")
        if confirm == "y":
            with open(filename, "rb") as f:
                value = f.read()
                breakDoc(value)
                print("Successfully broken")
        else:
            print("Canceled")
    elif fileext == "mp4" or fileext == "avi" or fileext == "mkv" or fileext == "flv" or fileext == "mpg" or fileext == "wmv" or fileext == "mov" or fileext == "3gp":
        confirm = input("Do you want to break this video?(y/n)")
        if confirm == "y":
            with open(filename, "rb") as f:
                value = f.read()
                breakVideo(value)
                print("Successfully broken")
        else:
            print("Canceled")
    elif fileext == "mp3" or fileext == "wav" or fileext == "flac" or fileext == "ogg" or fileext == "aac":
        confirm = input("Do you want to break this audio?(y/n)")
        if confirm == "y":
            with open(filename, "rb") as f:
                value = f.read()
                breakAudio(value)
                print("Successfully broken")
        else:
            print("Canceled")
    elif fileext == "zip" or fileext == "rar" or fileext == "7z" or fileext == "tar" or fileext == "gz" or fileext == "bz2" or fileext == "xz" or fileext == "tar.gz":
        confirm = input("Do you want to break this archive?(y/n)")
        if confirm == "y":
            with open(filename, "rb") as f:
                value = f.read()
                breakArc(value)
                print("Successfully broken")
        else:
            print("Canceled")



if __name__ == "__main__":
    argvs = sys.argv
    main(argvs)