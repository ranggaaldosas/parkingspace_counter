import cv2

image_path = "assets/image.png"
image = cv2.imread(image_path)

# vid_path = "assets/video.mp4"
# video = cv2.VideoCapture(vid_path)
while True:
    cv2.rectangle(image, (49, 145), (156, 193), (255, 100, 100), 2)
    cv2.imshow("Input Image", image)
    if cv2.waitKey(10) & 0xFF==ord('1'):
        break