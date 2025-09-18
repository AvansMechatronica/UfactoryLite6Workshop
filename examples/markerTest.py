import cv2
# import the opencv library
import keyboard  # load keyboard package
import time
from DahengAvansLibrary.DahengLibrary import dahengCamera
from Ufactory.libraries.vision.markers_detection import *
from Ufactory.libraries.vision.enums import *

camera_index = 1

def main():
    camera = dahengCamera(1, True)
    camera.setSoftwareTriggerMode()
    print("Press [q] and then [Enter] to Exit the Program")
    camera.startStraem()

    while True:
        if keyboard.is_pressed("q"):  # returns True if "q" is pressed
            camera.close();
            break

        if keyboard.is_pressed("p"):  # returns True if "q" is pressed

            camera.softwareTrigger()
            image = camera.grab_frame()
            result = False
            result, crop_image = extract_img_markers(image, workspace_ratio=1.0)
            if result:
                cv2.imshow("Crop", crop_image)
            else:
                print("Unable to extract image markers")

            result, marker_image = draw_markers(image, workspace_ratio=1.0)
            if result:
                cv2.imshow("Marker", marker_image)
            else:
                print("Unable to draw image markers")

            cv2.waitKey(1)
            time.sleep(1)

if __name__ == "__main__":
    main()