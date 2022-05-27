# -*- coding:UTF-8 -*-
import sys

def startscan():
    from pyzbar import pyzbar
    import cv2
    import pyperclip
    import tkinter.messagebox
    import webbrowser
    root = tkinter.Tk()  # 创建一个Tkinter.Tk()实例
    root.withdraw()
    # 二维码动态识别
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    camera.set(3, 1280)  # 设置分辨率
    camera.set(4, 768)
    url = None
    result = None
    while True:
        (grabbed, frame) = camera.read()
        # 获取画面中心点
        h1, w1 = frame.shape[0], frame.shape[1]

        # 纠正畸变
        dst = frame

        # 扫描二维码
        text = pyzbar.decode(dst)
        for texts in text:
            textdate = texts.data.decode('UTF-8')
            # print(textdate)
            (x, y, w, h) = texts.rect  # 获取二维码的外接矩形顶点坐标
            # print('识别内容:' + textdate)

            # 二维码中心坐标
            cx = int(x + w / 2)
            cy = int(y + h / 2)
            cv2.circle(dst, (cx, cy), 2, (0, 255, 0), 8)  # 做出中心坐标
            # print('中间点坐标：', cx, cy)
            coordinate = (cx, cy)

            # 在画面左上角写出二维码中心位置
            cv2.putText(dst, 'Location' + str(coordinate), (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # 画出画面中心与二维码中心的连接线
            cv2.line(dst, (cx, cy), (int(w1 / 2), int(h1 / 2)), (255, 0, 0), 2)
            # cv2.rectangle(dst, (x, y), (x + w, y + h), (0, 255, 255), 2)  # 做出外接矩形

            # 二维码最小矩形
            if texts.type == 'QRCODE':
                cv2.line(dst, texts.polygon[0], texts.polygon[1], (255, 0, 0), 2)
                cv2.line(dst, texts.polygon[1], texts.polygon[2], (255, 0, 0), 2)
                cv2.line(dst, texts.polygon[2], texts.polygon[3], (255, 0, 0), 2)
                cv2.line(dst, texts.polygon[3], texts.polygon[0], (255, 0, 0), 2)
                #print(texts.polygon)
            elif texts.type == 'CODE128':
                pass
                #cv2.line(dst, x, y, (255, 0, 0), 2)
                #cv2.line(dst, y, w, (255, 0, 0), 2)
                #cv2.line(dst, w, h, (255, 0, 0), 2)
                #cv2.line(dst, h, x, (255, 0, 0), 2)
                #print(texts.polygon)

            # 写出扫描内容
            txt = ('(' + texts.type + ')  ' + textdate)
            cv2.putText(dst, txt, (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 50, 255), 2)
            if 'http://' in textdate or 'https://' in textdate:
                if textdate == url:
                    break
                url = textdate
                webbrowser.open_new_tab(url)
                break
            if result == textdate:
                break
            result = textdate
            x = tkinter.messagebox.showinfo(title='扫描完成', message='扫描结果\n' + result + '\n按‘确定’复制到剪贴板')
            pyperclip.copy(result)
        cv2.imshow('dst', dst)
        if cv2.waitKey(1) & 0xFF == ord('S'):  # 按S保存一张图片
            cv2.imwrite("./frame.jpg", frame)

        if cv2.waitKey(20) & 0XFF == ord('q'):
            camera.release()
            cv2.destroyAllWindows()
            break
argv = sys.argv
if '-g' in argv:
    import qrcode
    filename = 'result.png'
    content_i = argv.index('-g') + 1
    content = argv[content_i]
    if '-n' in argv:
        filename_i = argv.index('-n') + 1
        filename = argv[filename_i]
    img = qrcode.make(content)
    img.save(filename)
elif '-s' in argv:
    startscan()
elif len(argv) == 1:
    startscan()
else:
    sys.exit()
