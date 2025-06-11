import cv2
from cvzone.HandTrackingModule import HandDetector
import math

# Setup webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

zoom_factor = 1.0
prev_distance = None
anchor_x, anchor_y = 640, 360  # default center

while True:
    success, img = cap.read()
    if not success:
        break

    hands, img = detector.findHands(img)  # With landmarks drawn

    if hands:
        lmList = hands[0]['lmList']
        if lmList:
            x1, y1 = lmList[4][0], lmList[4][1]   # Thumb tip
            x2, y2 = lmList[8][0], lmList[8][1]   # Index tip

            # Distance between thumb and index
            distance = math.hypot(x2 - x1, y2 - y1)

            # Midpoint for dynamic anchor
            anchor_x = int((x1 + x2) / 2)
            anchor_y = int((y1 + y2) / 2)

            # Adjust zoom factor based on finger pinch
            if prev_distance is not None:
                diff = distance - prev_distance
                zoom_factor += diff * 0.005
                zoom_factor = max(0.5, min(3.0, zoom_factor))
            prev_distance = distance
    else:
        prev_distance = None

    # Resize the image based on zoom factor
    h, w, _ = img.shape
    zoomed_img = cv2.resize(img, None, fx=zoom_factor, fy=zoom_factor)
    zh, zw, _ = zoomed_img.shape

    # Calculate zoomed anchor position
    zoom_anchor_x = int(anchor_x * zoom_factor)
    zoom_anchor_y = int(anchor_y * zoom_factor)

    # Crop window around the zoomed anchor
    x_start = max(zoom_anchor_x - w // 2, 0)
    y_start = max(zoom_anchor_y - h // 2, 0)
    x_end = x_start + w
    y_end = y_start + h

    # Crop and adjust if zoomed image is smaller
    cropped = zoomed_img[y_start:y_end, x_start:x_end]

    # Pad if needed
    ch, cw, _ = cropped.shape
    pad_top = (h - ch) // 2 if ch < h else 0
    pad_bottom = h - ch - pad_top if ch < h else 0
    pad_left = (w - cw) // 2 if cw < w else 0
    pad_right = w - cw - pad_left if cw < w else 0

    final_img = cv2.copyMakeBorder(cropped, pad_top, pad_bottom, pad_left, pad_right, cv2.BORDER_CONSTANT)

    # Show result
    cv2.imshow("Dynamic Finger-Anchored Zoom", final_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
