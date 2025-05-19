import cv2

# Open default camera
cam = cv2.VideoCapture(0)

ret, frame = cam.read()
print(frame.shape)

downscaled_frame = cv2.resize(frame, (64, 48), interpolation = cv2.INTER_AREA)

# Output frame in a GUI
cv2.imshow("DownscaleTest", downscaled_frame)
# Hold output for a set number of milliseconds
cv2.waitKey(5000)

# Release capture objects
cam.release()
cv2.destroyAllWindows()
