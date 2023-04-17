import cv2

# Read Image
img = cv2.imread("solar-system.jpg")

cv2.putText(img, "sun", (50,50), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(225,225,255))
cv2.putText(img, "mercury", (100,150), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.7, color=(225,225,255))
cv2.putText(img, "venus", (200,150), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.7, color=(225,225,255))
cv2.putText(img, "earth", (300,150), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.7, color=(225,225,255))
cv2.imshow("output", img)

cv2.waitKey(3000)