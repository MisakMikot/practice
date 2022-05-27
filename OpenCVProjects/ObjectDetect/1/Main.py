import cv2

cascade_eye = cv2.CascadeClassifier('cascades\\haarcascade_eye.xml')
cascade_hand = cv2.CascadeClassifier('cascades\\hand.xml')
cascade_face = cv2.CascadeClassifier('cascades\\face.xml')
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while (True):
    # 读取摄像头当前这一帧的画面  ret:True fase image:当前这一帧画面
    ret, img = cap.read()
    dst = img
    h1, w1 = img.shape[0], img.shape[1]
    # 图片进行灰度处理
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 人脸检测
    eyes = cascade_eye.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    hands = cascade_hand.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    faces = cascade_face.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    # 绘制人脸框
    for (x, y, w, h) in eyes:
        cx = int(x + w / 2)
        cy = int(y + h / 2)
        cv2.circle(dst, (cx, cy), 2, (0, 255, 0), 8)  # 做出中心坐标
        cv2.line(dst, (cx, cy), (int(w1 / 2), int(h1 / 2)), (255, 0, 0), 2)
        width = x + w
        height = y + h
        strok = 2
        color = (255, 0, 0)
        cv2.rectangle(img, (x, y), (width, height), color, strok)
        cv2.putText(dst, 'EYE', (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 50, 255), 2)

    for (x, y, w, h) in hands:
        cx = int(x + w / 2)
        cy = int(y + h / 2)
        cv2.circle(dst, (cx, cy), 2, (0, 255, 0), 8)  # 做出中心坐标
        cv2.line(dst, (cx, cy), (int(w1 / 2), int(h1 / 2)), (255, 0, 0), 2)
        width = x + w
        height = y + h
        strok = 2
        color = (255, 0, 0)
        cv2.rectangle(img, (x, y), (width, height), color, strok)
        cv2.putText(dst, 'HAND', (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 50, 255), 2)

    for (x, y, w, h) in faces:
        cx = int(x + w / 2)
        cy = int(y + h / 2)
        cv2.circle(dst, (cx, cy), 2, (0, 255, 0), 8)  # 做出中心坐标
        cv2.line(dst, (cx, cy), (int(w1 / 2), int(h1 / 2)), (255, 0, 0), 2)
        width = x + w
        height = y + h
        strok = 2
        color = (255, 0, 0)
        cv2.rectangle(img, (x, y), (width, height), color, strok)
        cv2.putText(dst, 'FACE', (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 50, 255), 2)

    cv2.imshow('detect', img)
    if cv2.waitKey(20) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
