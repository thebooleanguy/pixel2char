import cv2

# Open default camera
cam = cv2.VideoCapture(0)

ret, frame = cam.read()

width = 40
height =40
downscaled_frame = cv2.resize(frame, (width, height), interpolation = cv2.INTER_AREA)
grayscaled_frame = cv2.cvtColor(downscaled_frame, cv2.COLOR_BGR2GRAY)

# Map to ASCII
chars = "█▓▒░@#%&*+=-:. "  # 16 levels
ascii_art = [[0 for i in range(height)] for j in range(width)]

for y in range(height):
    for x in range(width):
        ascii_art.append(0)
        brightness = grayscaled_frame[y][x]
        index = int(brightness / 16)
        index = min(index, len(chars) - 1)
        ascii_char = chars[index]
        ascii_art[y][x] = ascii_char
        print(ascii_char,end="")
    print()

# Output frame in a GUI
cv2.imshow("DownscaleTest", grayscaled_frame)
# Hold output for a set number of milliseconds
cv2.waitKey(5000)

# Release capture objects
cam.release()
cv2.destroyAllWindows()
