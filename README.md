# OpenCV Hello World

The [OpenCV_Hello_World](OpenCV_Hello_World.ipynb) is a simple "Hello World" notebook showing how to find the outlines of objects in a picture using the OpenCV Python library. In a nutshell, the code traces the shapes of any object in a picture.


## How to Try This Notebook

If you want to see this in action, you can access everything from this repository in the following ways:
- **Local Usage**: Users are welcome to clone the repository and try out the notebook locally. 
- **ILCI JupyterHub Usage**:
  - Open this notebook at [ILCI's JupyterLab](https://jupyter-sandbox.ilci.scienceversa.com/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fagostof%2FOpenCV_Hello_World&urlpath=lab%2Ftree%2FOpenCV_Hello_World%2FOpenCV_Hello_World.ipynb&branch=main) (you will be asked to log in if not logged in already).
  - Or use [Voilà](https://jupyter-sandbox.ilci.scienceversa.com/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fagostof%2FOpenCV_Hello_World&urlpath=voila/render/OpenCV_Hello_World%2FOpenCV_Hello_World.ipynb&branch=main) to run the notebook, showing only the results (runs notebook with code hidden).

>**⚠️ Heads up**: These links are for **ILCI group members only**. If you're not part of this group, please don't try to access them.


## Inside the Notebook

1. **Getting Started**:
   - Loading essential tools to work with pictures.
   - Using some handy functions to make our task easier.
2. **Viewing and Preparing the Picture**:
   - Viewing our chosen image (of some apples).
   - You can switch to another picture here!
   - Simplifying the picture to grayscale (black and white) and adding a slight blur. This aids in highlighting the edges.
3. **Tracing Edges using Canny and Sobel**:
   - Employing the methods: 'Canny' and Sobel to outline the apple shapes. 
   - Experiment with difference adjustments, and see effects on results.
   - Comparison of the original images to the traces for each method.

## Convert Notebook to Python

If you whish to run this notebook as a Python script, you can use the `jupytext` command-line tool to convert it to a plain text file. For instance for the `OpenCV_Hello_World.ipynb`:

```sh
jupytext OpenCV_Hello_World.ipynb --to py
```

## References

For additional information on edge detection using OpenCV, visit [Learn OpenCV - Edge Detection](https://learnopencv.com/edge-detection-using-opencv/).
