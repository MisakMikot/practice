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

def breakImg(value:bytes):
    '''
    this is breakImg function
    :return:
    '''
    string = str(value)
    list = string.split('\\')
    index = random.randint(0,len(list)-1)
    list.remove(list[index])
    result = "".join(list)
    if fileext == 'jpg':
        with open("new.jpg", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'jpeg':
        with open("new.jpeg", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'png':
        with open("new.png", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'gif':
        with open("new.gif", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'bmp':
        with open("new.bmp", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'tiff':
        with open("new.tiff", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'ico':
        with open("new.ico", "wb") as f:
            f.write(bytes(result, 'utf-8'))

def breakDisk(value:bytes):
    '''
    this is breakIso function
    :return:
    '''
    string = str(value)
    list = string.split('\\')
    index = random.randint(0,len(list)-1)
    list.remove(list[index])
    result = "".join(list)
    if fileext == 'iso':
        with open("new.iso", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'vcd':
        with open("new.vcd", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'dvd':
        with open("new.dvd", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'blu-ray':
        with open("new.blu-ray", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'cd':
        with open("new.cd", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'vhd':
        with open("new.vhd", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'vmdk':
        with open("new.vmdk", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'vdi':
        with open("new.vdi", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'vhdx':
        with open("new.vhdx", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'vhd':
        with open("new.vhd", "wb") as f:
            f.write(bytes(result, 'utf-8'))

def breakInstaller(value:bytes):
    '''
    This is a breakInstaller function
    :return:
    '''
    string = str(value)
    list = string.split('\\')
    index = random.randint(0, len(list) - 1)
    list.remove(list[index])
    result = "".join(list)
    if fileext == 'msi':
        with open("new.msi", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'msu':
        with open("new.msu", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'msp':
        with open("new.msp", "wb") as f:
            f.write(bytes(result, 'utf-8'))

def breakEbook(value:bytes):
    '''
    This is a breakPdf function
    :return:
    '''
    string = str(value)
    list = string.split('\\')
    index = random.randint(0, len(list) - 1)
    list.remove(list[index])
    result = "".join(list)
    if fileext == 'pdf':
        with open("new.pdf", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'epub':
        with open("new.epub", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'mobi':
        with open("new.mobi", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'azw':
        with open("new.azw", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'azw3':
        with open("new.azw3", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'azw4':
        with open("new.azw4", "wb") as f:
            f.write(bytes(result, 'utf-8'))
    elif fileext == 'azw5':
        with open("new.azw5", "wb") as f:
            f.write(bytes(result, 'utf-8'))

def usage():
    '''
    This is a usage function
    :return:
    '''
    print("Usage: {} <file>".format(sys.argv[0]))
    print("Example: {} test.exe".format(sys.argv[0]))

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
    elif fileext == "jpg" or fileext == "jpeg" or fileext == "png" or fileext == "gif" or fileext == "bmp" or fileext == "tiff" or fileext == "ico":
        confirm = input("Do you want to break this image?(y/n)")
        if confirm == "y":
            with open(filename, "rb") as f:
                value = f.read()
                breakImg(value)
                print("Successfully broken")
        else:
            print("Canceled")
    elif fileext == "iso" or fileext == "vdi" or fileext == "vhdx" or fileext == "vhd" or fileext == "img" or fileext == "vmdk":
        confirm = input("Do you want to break this disk?(y/n)")
        if confirm == "y":
            with open(filename, "rb") as f:
                value = f.read()
                breakDisk(value)
                print("Successfully broken")
        else:
            print("Canceled")
    elif fileext == "msi" or fileext == "cab" or fileext == "msp" or fileext == "msu" or fileext == "msp" or fileext == "msp" or fileext == "msi" or fileext == "msi":
        confirm = input("Do you want to break this installer?(y/n)")
        if confirm == "y":
            with open(filename, "rb") as f:
                value = f.read()
                breakInstaller(value)
                print("Successfully broken")
        else:
            print("Canceled")
    elif fileext == "pdf" or fileext == "mobi" or fileext == "epub" or fileext == "azw" or fileext == "azw3" or fileext == "azw4" or fileext == "azw5":
        confirm = input("Do you want to break this ebook?(y/n)")
        if confirm == "y":
            with open(filename, "rb") as f:
                value = f.read()
                breakEbook(value)
                print("Successfully broken")
        else:
            print("Canceled")
    else:
        print("Unsupported file type")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        exit(1)
    elif len(sys.argv) > 2:
        usage()
    else:
        main(sys.argv)
    argvs = sys.argv