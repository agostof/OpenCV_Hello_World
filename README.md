# OpenCV Hello World

## Overview

The [OpenCV_Hello_World](OpenCV_Hello_World.ipynb) Notebook demonstrates the application of various edge detection techniques to an image using OpenCV and Matplotlib in Python. It explores different parameters and methods, focusing primarily on Canny and Sobel Edge Detection, to identify and visualize the boundaries within an image.

## Structure of the Notebook

1. **Import Libraries and Utility Functions**
   - Necessary libraries such as `cv2`, `numpy`, and `matplotlib.pyplot` are imported.
   - Utility functions from a custom module `cvutils`, including `cv2_imshow` and `auto_canny_edge_detection`, are imported.

2. **Load and Display Original Image**
   - An image of different types of apples is loaded from the `data` directory and displayed using the custom `cv2_imshow` function.
   - The `image_file` variable can be modified to point to a new image if needed.

3. **Preprocess the Image**
   - The original image is converted to grayscale and blurred using a Gaussian filter.

4. **Canny Edge Detection**
   - Canny edge detection is applied with different threshold values (wide, mid, and tight).
   - An additional method, `auto_canny_edge_detection`, is also utilized.
   - The results of the edge detection are displayed in a 2x2 grid.

5. **Sobel Edge Detection**
   - The Sobel operator is used to detect edges in the X and Y directions separately.
   - Combined X and Y Sobel Edge Detection is also performed.
   - The resulting images are displayed in a 2x2 grid.

## Utility Functions

- **cv2_imshow**: A utility function to display images in the notebook with the option to add a title. It can be used with or without specifying the `axes` parameter.
- **auto_canny_edge_detection**: A function for performing Canny edge detection with automatically determined threshold values.

## References

For additional information on edge detection using OpenCV, refer to [Learn OpenCV - Edge Detection](https://learnopencv.com/edge-detection-using-opencv/).

## Convert Notebook to Python
To convert this notebook to a Python script, you can use the `jupytext` command-line tool. If you have the notebook file named `OpenCV_Hello_World.ipynb`, you can convert it to a Python file by running the following command in your terminal:

```sh
jupytext OpenCV_Hello_World.ipynb --to py
```

## Trying out the Notebook

Users are welcome to clone the repository and try out the notebook locally. Additionally, ILCI users have the option of trying it out on the cloud using JupyterLab: [![Open In Jupyter](https://img.shields.io/badge/jupyter-open_in_ILCI_Jupyter_Hub-blue?logo=jupyter)](https://jupyter-sandbox.ilci.scienceversa.com/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fagostof%2FOpenCV_Hello_World&urlpath=lab%2Ftree%2FOpenCV_Hello_World%2FOpenCV_Hello_World.ipynb&branch=main)

**Note**: The above link is intended **only for authorized ILCI users**. Unauthorized access is strictly prohibited.


