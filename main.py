import cv2
import numpy as np

FRAME_DELAY = 20

capture = cv2.VideoCapture(0)

frame_buffer = np.zeros((FRAME_DELAY, int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)), 3), dtype=np.uint8)

i_frame = 0
while True:
    ret, frame = capture.read()
    frame = cv2.flip(frame, 1)
    frame_buffer[i_frame,...] = frame

    cv2.imshow('frame',frame_buffer[(i_frame+1)%FRAME_DELAY,...])

    if i_frame == FRAME_DELAY-1:
        i_frame = 0
    else:
        i_frame += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()