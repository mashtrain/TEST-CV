import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    ret, frame =cap.read()
    
    if not ret:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10,255,255])
    
    lower_red2 = np.array([170,120,70])
    upper_red2 = np.array([180,255,255])
    
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    mask2 = cv2.inRange(hsv,lower_red2, upper_red2)
    
    mask = mask1 + mask2
    
    cv2.imshow("kamera asli", frame)
    cv2.imshow("Hanya merah", mask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()