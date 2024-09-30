import cv2 
import numpy as np
import matplotlib.pyplot as plt

# Load the video
video_path = 'data/feasibility.mp4'
cap = cv2.VideoCapture(video_path)

# Check if the video was opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
else:
    print("Video loaded successfully.")
    
    
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
        
    # Convert the frame from BGR to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Apply thresholding
    gray_frame = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2GRAY)
    _, thre = cv2.threshold(gray_frame, 80, 255, cv2.THRESH_BINARY)


    # Display the frame using Matplotlib
    cv2.imshow('Frame', frame_rgb)
    
    # Add a delay to control the frame rate
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
