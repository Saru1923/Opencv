import cv2
import numpy as np

# Define input video properties
input_video_filename = "Butterfly.mp4"  # Replace with your actual video file
video_filename = "C:\\Opencv\\presentation_output.mp4"  # Output video filename

# Open the input video
cap = cv2.VideoCapture(input_video_filename)

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Create VideoWriter object
out = cv2.VideoWriter(video_filename, fourcc, frame_rate, (frame_width, frame_height))

# List of overlay colors for different frames (cycling through)
colors = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Black, Blue, Green, Red

frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Stop when the video ends

    # Select color based on frame count (cycling through colors)
    color = colors[frame_count % len(colors)]

    # Create a transparent overlay
    overlay = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
    overlay[:] = color  # Fill frame with color

    # Blend overlay with original frame (adjust opacity)
    alpha = 0.3  # Adjust transparency level
    frame = cv2.addWeighted(frame, 1 - alpha, overlay, alpha, 0)

    # Add caption text
    caption_text = f"Frame {frame_count + 1}: Color {color}"
    cv2.putText(frame, caption_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Overlay shapes (same as original)
    cv2.rectangle(frame, (100, 100), (300, 300), (255, 255, 255), 2)
    cv2.circle(frame, (450, 200), 50, (255, 255, 255), 2)
    cv2.line(frame, (50, 400), (590, 400), (255, 255, 255), 2)

    # Write the modified frame to the output video
    out.write(frame)
    cv2.namedWindow('Presentation',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Presentation',700,600)

    # Display the frame (optional)
    cv2.imshow('Presentation', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):  # Adjust waitKey based on frame rate
        break

    frame_count += 1

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Video saved as {video_filename}")