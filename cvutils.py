import cv2
import numpy as np
from matplotlib import pyplot as plt

def cv2_imshow(title, image, axes=None, **kwargs):
    a = image.clip(0, 255).astype('uint8')
    plt.axis('off')

    # cv2 stores colors as BGR; convert to RGB
    if a.ndim == 3:
        if a.shape[2] == 4:
            a = cv2.cvtColor(a, cv2.COLOR_BGRA2RGBA)
        else:
            a = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    if axes is not None:
        axes.axis('off')
        if title is not None:
            axes.set_title(title)
        #return axes.imshow(a, **kwargs)
        im = axes.imshow(a, **kwargs)
    else:
        #plt.axis('off')
        if title is not None:
            plt.title(title)
        im = plt.imshow(a, **kwargs)

    #if save_path is not None:
    #    plt.savefig(save_path, bbox_inches='tight', pad_inches=0)
    # return im
    #return plt.imshow(a, **kwargs)
    return im 


# This function was extracted
# from https://towardsdatascience.com/easy-method-of-edge-detection-in-opencv-python-db26972deb2d
def auto_canny_edge_detection(image, sigma=0.33):
    md = np.median(image)
    lower_value = int(max(0, (1.0-sigma) * md))
    upper_value = int(min(255, (1.0+sigma) * md))
    return cv2.Canny(image, lower_value, upper_value)

#__all__ = ['cv2_imshow', 'auto_canny_edge_detection']