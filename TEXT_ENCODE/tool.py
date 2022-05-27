import base64
import binascii
import math
import os
import sys
import time

import winsound
from Crypto.Cipher import AES
from PIL import Image

from AESTool import AEScryptor


def plain2base64(text):
    res = base64.b64encode(text)
    return res


def base642plain(text):
    try:
        res = base64.b64decode(text)
    except binascii.Error as e:
        print('错误！！BASE64解码失败，可能是在秘钥解码时出现问题！')
        with open("ERRORLOG.txt", "w", encoding="utf-8") as f:
            f.write(str(e))
        sys.exit()
    return res


def plain2image(text):
    str_len = len(text)
    width = math.ceil(str_len ** 0.5)
    im = Image.new("RGB", (width, width), 0x0)

    x, y = 0, 0
    for i in text:
        index = ord(i)
        rgb = (0, (index & 0xFF00) >> 8, index & 0xFF)
        im.putpixel((x, y), rgb)
        if x == width - 1:
            x = 0
            y += 1
        else:
            x += 1
    return im


def plain2key(text, key):
    # if len(key) > 2 and len(key) < 10:
    text2 = ''
    newkey = []
    for i in key:
        newkey.append(ord(i))
    ii = 0
    for i in text:
        if ord(i) != 10:
            text2 = text2 + chr(ord(i) + newkey[ii])
        else:
            text2 = text2 + chr(10)
        ii = ii + 1
        if ii >= len(newkey):
            ii = 0
    return text2


def img2plain(im):
    width, height = im.size
    lst = []
    for y in range(height):
        for x in range(width):
            red, green, blue = im.getpixel((x, y))
            if (blue | green | red) == 0:
                break

            index = (green << 8) + blue
            lst.append(chr(index))
    return ''.join(lst)


def key2plain(key, text):
    # if len(key) > 2 and len(key) < 10:
    text2 = ''
    newkey = []
    for i in key:
        newkey.append(ord(i))
    ii = 0
    for i in text:
        if ord(i) != 10:
            text2 = text2 + chr(ord(i) - newkey[ii])
        else:
            text2 = text2 + chr(10)
        ii = ii + 1
        if ii >= len(newkey):
            ii = 0
    return text2


def plain2aes(text):
    iv = b'0000000000000000'
    key = b'crKSLeJXuOFi4Dam'
    aes = AEScryptor(key, AES.MODE_CBC, iv, paddingMode="ZeroPadding", characterSet='utf-8')
    rData = aes.encryptFromString(text)
    return rData.toBase64()


def ZeroPadding(data):
    data += b'\x00'
    while len(data) % 16 != 0:
        data += b'\x00'
    return data


def aes2plain(text):
    iv = b'0000000000000000'
    key = b'crKSLeJXuOFi4Dam'
    aes = AEScryptor(key, AES.MODE_CBC, iv, paddingMode="ZeroPadding", characterSet='utf-8')
    rData = aes.decryptFromBase64(text)
    return rData.toString()


def encode(all_text, SECRET_KEY):
    keylen = len(SECRET_KEY) - 2
    print('开始编码(阶段一)')
    aes = plain2aes(all_text)
    print('开始进行总共' + str(len(SECRET_KEY)) + '次编码(阶段二)')
    b64 = plain2base64(aes.encode('utf-8'))
    for i in range(1, keylen):
        b64 = plain2base64(b64)
    b64 = plain2base64(b64)
    print('编码(阶段二)完成，开始编码(阶段三)')
    fnl = plain2key(text=b64.decode('utf-8'), key=SECRET_KEY)
    print('编码(阶段三)完成，开始编码(阶段四)')
    img = plain2image(fnl)
    print('图片编码完成')
    return img


def decode(img, SECRET_KEY):
    keylen = len(SECRET_KEY) - 2
    print('开始解码(阶段一)')
    fnl = img2plain(img)
    print('解码(阶段一)完成，开始解码(阶段二)')
    b64 = key2plain(text=fnl, key=SECRET_KEY).encode('utf-8')
    print('解码(阶段二)完成，开始总共' + str(len(SECRET_KEY)) + '次解码(阶段三)')
    aes = base642plain(b64)
    for i in range(1, keylen):
        aes = base642plain(aes)
    aes = base642plain(aes).decode('utf-8')
    print('解码(阶段三)完成，开始解码(阶段四)')
    all_text = aes2plain(aes)
    print('解码(阶段四)完成')
    return all_text


def help():
    help_content = '''
            Text_Encoder v0.1

            Usage: {} <-e|-d filename> [-s SECRET_KEY]

            -e : Encode the file
            -d : Decode the file
            -s : Use custom SECRET_KEY
            '''.format(sys.argv[0])
    print(help_content)


def startEnc():
    if '-d' in argvs:
        print('不能同时编解码')
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        os.system('pause')
        sys.exit()
    filename = argvs[(argvs.index('-e') + 1)]
    fileext = filename.split(sep='.')[-1]
    if not fileext == 'txt':
        print('格式不支持')
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        os.system('pause')
        sys.exit()
    try:
        with open(filename, encoding="utf-8") as f:
            all_text = f.read()
    except Exception as e:
        print(e)
        print('读取文件失败')
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        os.system('pause')
        sys.exit()
    if '-s' in argvs:
        SECRET_KEY = argvs[(argvs.index('-s') + 1)]
    else:
        SECRET_KEY = '123456'
    op = time.time()
    res = encode(all_text=all_text, SECRET_KEY=SECRET_KEY)
    print('开始写入')
    res.save("{}_encrypt.bmp".format('.'.join(filename.split('.')[:-1])))
    ed = time.time()
    dua = ed - op
    print('完成！共用时' + str(round(dua)) + '秒')
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    os.system('pause')
    sys.exit()


def startDec():
    if '-e' in argvs:
        print('不能同时编解码')
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        os.system('pause')
        sys.exit()
    filename = argvs[(argvs.index('-d') + 1)]
    fileext = filename.split(sep='.')[-1]
    if not fileext == 'bmp':
        print('格式不支持')
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        os.system('pause')
        sys.exit()
    try:
        img = Image.open(filename)
    except Exception as e:
        print(e)
        print('读取图片失败')
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        os.system('pause')
        sys.exit()
    if '-s' in argvs:
        SECRET_KEY = argvs[(argvs.index('-s') + 1)]
    else:
        SECRET_KEY = '123456'
    op = time.time()
    res = decode(img=img, SECRET_KEY=SECRET_KEY)
    print('开始写入')
    with open("{}_decrypt.txt".format('.'.join(filename.split('.')[:-1])), "w", encoding="utf-8") as f:
        f.write(res)
    ed = time.time()
    dua = ed - op
    print('完成！共用时' + str(round(dua)) + '秒')
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    os.system('pause')
    sys.exit()


def quick():
    try:
        filename = argvs[1].split(sep='.')[-2]
        fileext = argvs[1].split(sep='.')[-1]
        full = filename + '.' + fileext
        print(full)
    except IndexError:
        help()
        os.system('pause')
        sys.exit()
    if not os.path.isfile(full):
        print('文件不存在')
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        os.system('pause')
        sys.exit()
    if fileext == 'txt':
        print('开始读取文本')
        try:
            with open(full, encoding="utf-8") as f:
                all_text = f.read()
        except Exception as e:
            print(e)
            print('读取失败')
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
            os.system('pause')
            sys.exit()
        SECRET_KEY = input('请输入你要加密的密码：')
        if SECRET_KEY == '':
            SECRET_KEY = '123456'
        op = time.time()
        res = encode(all_text=all_text, SECRET_KEY=SECRET_KEY)
        print('开始文件写入')
        res.save("{}_encrypt.bmp".format('.'.join(full.split('.')[:-1])))
        ed = time.time()
        dua = ed - op
        print('完成！共用时' + str(round(dua)) + '秒')
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        os.system('pause')
        sys.exit()
    elif fileext == 'bmp':
        print('开始读取图像')
        try:
            img = Image.open(full)
        except Exception as e:
            print(e)
            print('读取失败')
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
            os.system('pause')
            sys.exit()
        SECRET_KEY = input('请输入密码：')
        if SECRET_KEY == '':
            SECRET_KEY = '123456'
        op = time.time()
        res = decode(img=img, SECRET_KEY=SECRET_KEY)
        print('开始写入')
        with open("{}_decrypt.txt".format('.'.join(full.split('.')[:-1])), "w", encoding="utf-8") as f:
            f.write(res)
        ed = time.time()
        dua = ed - op
        print('完成！共用时' + str(round(dua)) + '秒')
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        os.system('pause')
        sys.exit()


def main():
    if '-e' in argvs:
        startEnc()
    elif '-d' in argvs:
        startDec()
    elif len(argvs) == 2 and not '-e' in argvs and not '-d' in argvs:
        quick()
    else:
        help()


if __name__ == '__main__':
    argvs = sys.argv
    main()
