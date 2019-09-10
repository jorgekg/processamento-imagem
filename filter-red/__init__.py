import cv2

# get camera object
cam = cv2.VideoCapture(0)

while True:
    # get camera stream
    status, image = cam.read()
    
    # get canal of imagens
    b, g, r = cv2.split(image)

    # apply threshold
    (status, img) = cv2.threshold(r, 100, 255, cv2.THRESH_BINARY_INV)

    # show image
    cv2.imshow("image", img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
