import cv2

capture = cv2.VideoCapture(0) # Webcam

while True:

    ret, frame = capture.read() # Get the frame

    cv2.imshow("Stream", frame) # Imshow the frame in window named 'Stream'

    if cv2.waitKey(1) & 0xFF == ord('q'): # Press the 'q' to quit
        break

capture.release()
cv2.destroyAllWindows()
