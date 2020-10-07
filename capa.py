import numpy
import cv2



cap = cv2.VideoCapture(0)
_, fondo=cap.read()
fondo = cv2.medianBlur(fondo,3)#para quitar el ruido de la imagen,aki tiene que ser impar para que tenga centro

blue=cv2.cvtColor(numpy.uint8([[[0, 0, 255]]]),cv2.COLOR_BGR2HSV)
lower_blue = numpy.array([50,25,25])
upper_blue = numpy.array([130,255,255])

while 1:
    fin, frame = cap.read()
    median = cv2.medianBlur(frame,3) #para quitar el ruido de la imagen,aki tiene que ser impar para que tenga centro
    hsv = cv2.cvtColor(median, cv2.COLOR_BGR2HSV) #convertir la imagen en hsv
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    kernel = numpy.ones((3,3),numpy.uint8)

    opening = cv2.erode(mask,kernel,iterations=5)
    opening = cv2.dilate(opening,kernel,iterations=5)

    opening_inv=cv2.bitwise_not(opening)
    img2_fg = cv2.bitwise_and(fondo,fondo,mask = opening)
    #cv2.imshow('img1',img2_fg)
    img2_bg=cv2.bitwise_and(median,median,mask = opening_inv)
    #cv2.imshow('algo',img2_bg)
    res=img2_fg + img2_bg #sumamos las imagenes
    cv2.imshow('frame',res)
    k = cv2.waitKey(5) & 0xFF

    if k == 27:
        break
