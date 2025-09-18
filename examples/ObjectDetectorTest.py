import cv2
# import the opencv library
import keyboard  # load keyboard package
from DahengAvansLibrary.DahengLibrary import dahengCamera
from Ufactory.libraries.vision.markers_detection import *
from Ufactory.libraries.vision.ObjectDetector import ObjectDetector
from Ufactory.libraries.vision.Workspace import Workspace
from Ufactory.libraries.vision.enums import *
import time

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
            detector = ObjectDetector(
                obj_type=ObjectType.ANY, obj_color=ColorHSVPrime.TEST,
                workspace_ratio=1.0,
                ret_image_bool=True,
            )
            all = False
            if all:
                status, cx_rel_list, cy_rel_list, list_size, angle_list, color_list, object_type_list = detector.extract_all_object_with_hsv(image)
            else:
                status, result_pose, obj_type, obj_color, im_draw = detector.extract_object_with_hsv(image)
                if status:
                    print(result_pose)
                    print(obj_type)
                    print(obj_color)
                    cv2.imshow("Result", im_draw)
                    cv2.waitKey(1)
                    #realword_pose = workspace.get_pose(result_pose.x, result_pose.y, result_pose.yaw)
                    #print(realword_pose)
            time.sleep(1)


if __name__ == "__main__":
    main()