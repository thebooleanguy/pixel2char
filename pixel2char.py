import cv2
import os
import time

# Open default camera
cam = cv2.VideoCapture(0)

width = 40
height = 40

try:
    while True:
        ret, frame = cam.read()

        downscaled_frame = cv2.resize(frame, (width, height), interpolation = cv2.INTER_AREA)
        grayscaled_frame = cv2.cvtColor(downscaled_frame, cv2.COLOR_BGR2GRAY)

        # Map to ASCII
        chars = "█▓▒░@#%&*+=-:. "  # 16 levels
        ascii_art = [[0 for i in range(height)] for j in range(width)]

        os.system('clear')
        for y in range(height):
            for x in range(width):
                brightness = grayscaled_frame[y][x]
                index = int(brightness / 16)
                index = min(index, len(chars) - 1)
                ascii_char = chars[index]
                ascii_art[y][x] = ascii_char
                print(ascii_char,end="")
            print("")
        time.sleep(0.15)

except KeyboardInterrupt:
    print("\nASCII webcam closed!")

# Output frame in a GUI
# cv2.imshow("DownscaleTest", grayscaled_frame)
# Hold output for a set number of milliseconds
# cv2.waitKey(5000)

# Release capture objects
cam.release()
cv2.destroyAllWindows()
