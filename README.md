# Image Compression Toolkit - Python
Two ways to compress your images!

## Contributors

- [Aditya Sharma](https://github.com/adityashrm21)
- [Alden Chen](https://github.com/aldenchen)
- [Sayanti Ghosh](https://github.com/Sayanti86)

## Project Summary

This Python package specializes in reducing the size of images. It contains three main functions :`crop()`, `compress()` and `image_size()`. The `crop()` function reduces the size of an image by reducing the height and width of the image to the size specified by the user. The `compress()` function reduces the file size of an image by reducing the number of bits used in each colour channel of the image. The image_size function simply calculates and returns the size in bytes of the image passed into it. The size returned is then used to check whether the `compress()` function did its job correctly or not. The package could be used by people to reduce the size of images (dimensions or file size), which could then be uploaded to social media platforms or other websites and applications.

## Functions

- `crop(img_path, H, W)`
  - Description:
    This function will reduce the image to the specified size removing rows and columns of pixels from the borders.
  - Input:
    - img_path (string)
    - H (integer)
    - W (integer)
  - Output:
    - cropped image path (Cropped image with size `H x W x n`)
- `compress(image, b)`
  - Description:
    This function compresses the image by reducing the number of bits for each channel based on user input.
  - Input:
    - img_path (string)
    - b (integer, range [1, 8] (number of bits used for each channel in the compressed image))
  - Output:
    - compressed image path (Compressed image to `b` bits)
- `image_size(image)`
  - Description:
    Calculates and returns the size of an image in bytes.
  - Input:
    - img_path (string)
  - Output:
    - size (integer, size in bytes)

## Related Packages
There already are packages for image processing in R and Python:
  - [The magick package in R](https://cran.r-project.org/web/packages/magick/vignettes/intro.html)
  - [sckit-image in Python](https://scikit-image.org/)

The existing packages are very comprehensive and provide many functions such as transformations, filters, file conversions and other advanced functions. Our package focuses specifically on image compression and reducing image size using K-means Clustering. This package is not a wrapper or an improvement of an existing package. It simply uses an unsupervised learning algorithm (K-means clustering) to reduce the number of bits used to represent an image.
