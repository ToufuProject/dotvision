import cv2
import numpy as np

# Change the ID if needed (e.g., 0 → 1)
# If your iPhone camera opens instead, try using 1 or 2
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Unable to access the camera. Try a different ID.")
    exit()

# Size of the pixelated image (smaller values = more pixelated)
DOT_WIDTH = 64
DOT_HEIGHT = 48

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to retrieve frame.")
        break

    # Resize the frame to a smaller resolution to create pixelation
    small = cv2.resize(frame, (DOT_WIDTH, DOT_HEIGHT), interpolation=cv2.INTER_NEAREST)

    # Reduce color depth by rounding each channel to 0, 64, 128, or 192
    quantized = (small // 64) * 64

    # Scale the image back up to original size (keep blocky style)
    dot_image = cv2.resize(quantized, (frame.shape[1], frame.shape[0]), interpolation=cv2.INTER_NEAREST)

    # Display the pixelated image
    cv2.imshow('DotCam', dot_image)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
