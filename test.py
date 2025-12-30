import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    ret, frame =cap.read()
    
    if not ret:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    kernel = np.ones((5,5), np.uint8)
    
    #DETEKSI MERAH
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])
    
    lower_red2 = np.array([170,120,70])
    upper_red2 = np.array([180,255,255])
    
    mask_red = cv2.inRange(hsv,lower_red,upper_red) + cv2.inRange(hsv,lower_red2, upper_red2)
    mask_red = cv2.erode(mask_red, kernel, iterations=1)
    mask_red = cv2.dilate(mask_red, kernel, iterations=2)
    
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #kotak merah
    if len(contours_red) > 0 :
        c = max(contours_red, key =cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)
        if w > 10 and h > 10:
            cv2.rectangle(frame,(x,y), (x + w, y + h),(0, 0, 255), 2)
            cv2.putText(frame,"MERAH", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,255),2)
            
    
    #DETEKSI HIJAU
    lower_green = np.array([40, 70, 70])
    upper_green = np.array([80,255,255])

    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_green = cv2.erode(mask_green, kernel, iterations = 1)
    mask_green = cv2.dilate(mask_green, kernel, iterations= 2)
    
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #KOTAK HIJAU
    if len(contours_green) > 0:
        c = max(contours_green, key=cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)
        if w > 10 and h > 10:
            cv2.rectangle(frame,(x,y), (x+w, y+h), (0, 255 , 0), 2 )
            cv2.putText(frame,"HIJAU", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,255,0), 2)

    cv2.imshow("kamera", frame)
    # cv2.imshow("Hanya merah", mask1)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()