import cv2
import numpy as np


def nothing(x):
    pass


def main():
    cv2.namedWindow("Tracking")
    cv2.createTrackbar("Red", "Tracking", 0, 255, nothing)
    cv2.createTrackbar("Blue", "Tracking", 0, 255, nothing)
    cv2.createTrackbar("Green", "Tracking", 0, 255, nothing)

    while True:
        frame = cv2.imread('example_rock1.jpg')
        red_only = np.copy(frame)
        red_only[:, :, [0, 1]] = 0
        blue_only = np.copy(frame)
        blue_only[:, :, [1, 2]] = 0
        green_only = np.copy(frame)
        green_only[:, :, [0, 2]] = 0

        H_R = cv2.getTrackbarPos("Red", "Tracking")
        H_B = cv2.getTrackbarPos("Blue", "Tracking")
        H_G = cv2.getTrackbarPos("Green", "Tracking")

        red_only[red_only > H_R] = 255
        red_only[red_only < H_R] = 0
        blue_only[blue_only > H_B] = 255
        blue_only[blue_only < H_B] = 0
        green_only[green_only > H_G] = 255
        green_only[green_only < H_G] = 0

        cv2.imshow("frame", frame)
        cv2.imshow("red_only", red_only)
        cv2.imshow("blue_only", blue_only)
        cv2.imshow("green_only", green_only)

        key = cv2.waitKey(1)
        if key == 27:
            break

    cv2.destroyAllWindows()


if __name__ == "__main__": main()
