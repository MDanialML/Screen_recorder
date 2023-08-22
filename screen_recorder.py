# requaired libraries
import pyautogui
import numpy as np
import cv2

# specify video resolution
resolution = (1920, 1080)

# specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# name of output file
file_name = "Recording.avi"

# specify frame rate
# we can choose any value and eperiment with it
fps = 60.0

# creating a videowriter object
output_object = cv2.VideoWriter(file_name, codec, fps, resolution)

# create an empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# resize this window
cv2.resizeWindow("Live", 480, 270)

# infinte loop to take screenshot
while True:
    # screenshot
    img = pyautogui.screenshot()

    # convert screenshot to numpy array
    frame = np.array(img)

    # now convert it from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # write it to the output file
    output_object.write(frame)

    # displaying the recorded screen
    cv2.imshow("Live", frame)

    # stop recording when we press 'q'
    if cv2.waitKey(1) == ord('q'):
        break
# release the video writer
output_object.release()

# display all windows
cv2.destroyAllWindows()
