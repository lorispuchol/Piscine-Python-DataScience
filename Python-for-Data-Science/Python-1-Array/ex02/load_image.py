import cv2
import numpy as np
import matplotlib.pyplot as plt

def ft_load(path: str) -> np.array: # you can return to the desired format
    '''Prints format of an image and return is '''
    
    try:
        if not (path.lower().endswith('jpg') or path.lower().endswith('jpeg')):
            raise Exception("Bad file extension")
        # Save image in set directory
        # Read RGB image
        img = cv2.imread(path)

        print("The shape of image is:", img.shape)
        # Output img with window name as 'image'
        cv2.imshow('image', img) 
        
        # Maintain output window until
        # user presses a key
        cv2.waitKey(4000)

        # Destroying present windows on screen
        cv2.destroyAllWindows()
        return img
    except BaseException as e:
        print ("MyError:", e)


def main():
    print(ft_load("landscape.jpg"))

if __name__ == "__main__":
    main()