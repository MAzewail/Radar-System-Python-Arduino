import numpy as np
import serial
import cv2

width = 720
hight = 1080
radius = 60
img = np.zeros((width,hight,3))

def pos_angel(base_angel,length):
    pt = (hight // 2 + int(length * np.sin(np.radians(base_angel))), width + int(length * np.cos(np.radians(base_angel))))
    return pt
def put_degree(txt,shift=0,level=0,txt_shift=0,txt_level=0):
    cv2.putText(img, txt, org=pos_angel(int(txt) + 90+txt_shift, 353+txt_level), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.5,
                color=(0, 255, 0), thickness=1)
    cv2.circle(img, center=pos_angel(int(txt) + 90+shift, 378+level), radius=2, color=(0, 255, 0))

for base_angel in range(90,300,30):
    pt1 = (hight // 2 + int(350 * np.sin(np.radians(base_angel))), width + int(350 * np.cos(np.radians(base_angel))))
    cv2.line(img,pt1=pt1,pt2=(hight//2,width),color=[0,255,0],thickness=2)

for i in range(1,320,78):
    cv2.circle(img,(hight//2,width),i,color=[0,255,0])

put_degree('30')
put_degree('60',-2,-2)
put_degree('90',-4,-13)
put_degree('120',-3.5,-18,2,15)
put_degree('150',-2,-20,2,28)

for n,i in enumerate(range(0,300,78)):
    cv2.putText(img,f'{10*(n+1)}cm',org=pos_angel(90 , 50+i), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.5,color=(0, 255, 0), thickness=1)

cv2.imwrite('radar.jpg',img)
ser = serial.Serial(port='COM26',baudrate=9600)
entered_key = -1

while entered_key == -1:
    try:
        data = ser.readline().decode().split()[0].split(',')
        distance, angel = int(data[0]) , int(data[1])+90
        print(distance, angel)
        if not (270 > angel > 90):
            img=cv2.imread('radar.jpg')
        if distance < 40:
            distance = np.interp(distance,[0,40],[0,350])
            pt1 = (hight // 2 + int(distance * np.sin(np.radians(angel))), width + int(distance * np.cos(np.radians(angel))))
            cv2.line(img, pt1=(hight // 2 + int(350 * np.sin(np.radians(angel))), width + int(350 * np.cos(np.radians(angel)))),pt2=pt1, color=(0, 0, 255), thickness=2)
            pt2 = (hight // 2, width)
            color = (0, 255, 0)
            cv2.line(img, pt1=pt1, pt2=pt2, color=color, thickness=1)
        else:
            cv2.line(img, pt1=(
            hight // 2 + int(350 * np.sin(np.radians(angel))), width + int(350 * np.cos(np.radians(angel)))),
                     pt2=(hight // 2, width), color=(0, 255, 0), thickness=1)
    except:
        pass
    cv2.imshow('m', img)
    entered_key = cv2.waitKey(10)


