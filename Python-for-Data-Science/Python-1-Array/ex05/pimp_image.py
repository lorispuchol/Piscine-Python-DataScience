import numpy as np
from load_image import ft_load
import cv2


def ft_invert(array) -> np.array:
    '''Inverts the color of the image received.'''
    cp = array.copy()
    cp = 255-array
    return cp


def ft_red(array) -> np.array:
    '''Returns the red color of the image received.'''
    cp = array.copy()
    for i in cp:
        for j in i:
            j[0] = 0
            j[1] = 0
    return cp


def ft_green(array) -> np.array:
    '''Returns the green color of the image received.'''
    cp = array.copy()
    for i in cp:
        for j in i:
            j[2] = 0
            j[0] = 0
    return cp


def ft_blue(array) -> np.array:
    '''Returns the blue color of the image received.'''
    cp = array.copy()
    for i in cp:
        for j in i:
            j[2] = 0
            j[1] = 0
    return cp


def ft_grey(array) -> np.array:
    '''Returns the gray color of the image received.'''
    cp = array.copy()
    for i in cp:
        for j in i:
            grey = j[1] / 3 + j[0] / 3 + j[2] / 3
            j[1] = grey
    return cp[:, :, 1:-1]


def main():
    '''test'''
    try:
        array = ft_load("landscape.jpg")
        if array == []:
            return
        cv2.imshow('image', ft_invert(array))
        cv2.imshow('image2', ft_red(array))
        cv2.imshow('image3', ft_green(array))
        cv2.imshow('image4', ft_blue(array))
        cv2.imshow('image5', ft_grey(array))
        cv2.waitKey(40000)
        cv2.destroyAllWindows()
        print(ft_invert.__doc__)
    except BaseException as e:
        print("MyError:", e)
        return


if __name__ == "__main__":
    main()
