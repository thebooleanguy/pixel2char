import cv2

# Open default camera
cam = cv2.VideoCapture(0)

ret, frame = cam.read()
print(frame.shape)
# Output frame in a GUI
cv2.imshow("CamTest", frame)
# Hold output for a set number of milliseconds
cv2.waitKey(5000)

# Release capture objects
cam.release()
cv2.destroyAllWindows()
