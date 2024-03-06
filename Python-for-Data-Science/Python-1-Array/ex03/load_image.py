import cv2
import numpy as np


def ft_load(path: str) -> np.array:  # you can return to the desired format
    '''Prints format of an image and return it'''
    try:
        if not (path.lower().endswith('jpg') or path.lower().endswith('jpeg')):
            raise Exception("Bad file extension")
        img = cv2.imread(path)
        print("The shape of image is:", img.shape)
        return img
    except BaseException as e:
        print("MyError:", e)
