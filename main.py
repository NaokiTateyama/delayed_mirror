import cv2
import numpy as np

DELAY_TIME = 1 #seconds you want to delay

capture = cv2.VideoCapture(0)
frame_rate = capture.get(cv2.CAP_PROP_FPS)
frame_delay = int(frame_rate*DELAY_TIME)
frame_buffer = np.zeros((frame_delay, int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)), 3), dtype=np.uint8)

i_frame = 0
while True:
    ret, frame = capture.read()
    frame = cv2.flip(frame, 1)
    frame_buffer[i_frame,...] = frame

    cv2.imshow('frame',frame_buffer[(i_frame+1)%frame_delay,...])

    if i_frame == frame_delay-1:
        i_frame = 0
    else:
        i_frame += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()