from load_image import ft_load
import cv2
import numpy


def transpose(path: str):
    '''rotate image of 90degree'''
    try:
        img = ft_load(path)

        img = img[100:500, 400:800, :1]
        print("The shape of image is:", img.shape)
        print(img)
        img = [
            [img[j][i] for j in range(len(img))]
            for i in range(len(img[0])-1, -1, -1)
        ]
        img = img[::-1]
        img = numpy.array(img)
        print("New shape after Transpose:", img.shape)
        cv2.imshow('image', img)
        cv2.waitKey(4000)
        cv2.destroyAllWindows()
        return img
    except BaseException as e:
        print("MyError:", e)
        return []


def main():
    '''test'''
    path = "animal.jpeg"
    print(transpose(path))


if __name__ == "__main__":
    main()
