from load_image import ft_load
import cv2


def ft_zoom(path: str):

    try:
        img = ft_load(path)
        print(img)

        img = img[100:500, 400:800, :1]

        print("New shape after slicing:", img.shape)
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
    print(ft_zoom(path))


if __name__ == "__main__":
    main()
