import cv2
import picamera
import picamera.array
import numpy as np
# TODO: Merge this with tflite_detection_webcam code and increase frame rate


def test_camera():
    cv2.namedWindow("img", 0)
    with picamera.PiCamera() as camera:
        camera.resolution = (1920, 1080)
        camera.awb_mode = "off"
        rg, bg = (1.8, 1.4)
        camera.awb_gains = (rg, bg)
        with picamera.array.PiRGBArray(camera) as output:
            for _ in camera.capture_continuous(output, "rgb", use_video_port=True):
                img = cv2.cvtColor(output.array, cv2.COLOR_RGB2BGR)
                cv2.imshow("img", img)
                cv2.waitKey(1)
                # cv2.imwrite("test.jpg", img)
                r, g, b = (np.mean(output.array[..., i]) for i in range(3))
                if abs(r - g) > 2:
                    if r > g:
                        rg -= 0.1
                    else:
                        rg += 0.1
                if abs(b - g) > 1:
                    if b > g:
                        bg -= 0.1
                    else:
                        bg += 0.1
                camera.awb_gains = (rg, bg)
                output.seek(0)
                output.truncate(0)


if __name__ == "__main__":
    test_camera()
