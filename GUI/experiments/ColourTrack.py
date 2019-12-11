class Cam:

    import cv2
    import numpy as np

    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_skin = np.array([0, 48, 80])
        upper_skin = np.array([20, 255, 255])

        mask = cv2.inRange(hsv, lower_skin, upper_skin)

        # apply a series of erosions and dilations to the mask
        # using an elliptical kernel
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        mask = cv2.erode(mask, kernel, iterations=2)
        mask = cv2.dilate(mask, kernel, iterations=5)

        # blur the mask to help remove noise, then apply the
        # mask to the frame
        mask = cv2.GaussianBlur(mask, (11, 11), cv2.BORDER_WRAP)
        res = cv2.bitwise_and(frame, frame, mask = mask)

        # cv2.imshow('skinny', np.hstack([frame, res]))
        # cv2.imshow('mask', mask)
        cv2.imshow('res', res)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
            cv2.destroyAllWindows()
            cap.release
