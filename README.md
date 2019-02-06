# Image Compression Toolkit
Three ways to compress your images!

## Contributors

- [Aditya Sharma](https://github.com/adityashrm21)
- [Alden Chen](https://github.com/aldenchen)
- [Sayanti Ghosh](https://github.com/Sayanti86)

## Project Summary

This Python package specializes in reducing the size of images. It contains three main functions :`seam_carve()`, `crop()`, and `compress()`. The `seam_carve()` and `crop()` functions reduce the size of an image by reducing the height and width of an image to the size specified by the user. The `compress()` function reduces the size of an image by reducing the number of bits used in each colour channel of the image. The package could be used by people to reduce the size of images, which could then be uploaded to social media platforms or other websites and applications.

## Functions

- `SeamCarve` (class)
  Note : We plan to use some code provided for an assignment in DSCI 512 to implement seam carving. In particular, the functions `energy` and `remove_vertical_seam`/`remove_horizontal_seam` were provided.

  - `seam_carve(img, height, width)`
    - Description:
      This function will apply seam carving to the input image using Dynamic Programming to carve out lowest energy pixels depending on the input size given. The function will call other utility functions to calculate the minimum energy seams and remove them.
    - Input:
      - image (2d or 3d np array)
      - desired_height (integer)
      - desired_width (integer)
    - Output:
      - compressed image (3d numpy array, size `desired_height x desired_width x 3`)
  - `energy(image)`
    - Description:
      Computes the "energy" of an image, using the Laplacian of each colour channel and summing them up.
    - Input:
      - image: (a 3d numpy array)
    - Output: energy (a 2d numpy array)
  - `find_vertical_seam(energy)`/`find_horizontal_seam(energy)`
    - Description:
      This function uses dynamic programming to calculate the minimum energy vertical/horizontal seam.
    - Input:
      - energy (2d numpy array)
    - Output:
      - seam (1d numpy array, same as height/width in size)
  - `remove_vertical_seam(image, seam)`/`remove_vertical_seam(image, seam)`
      - Description:
        This function removes the calculated seam from the image.
      - Input:
        - image (3d numpy array, size `h x w x 3`)
        - seam (1d numpy array, same as height/width in size)
      - Output:
        - image (3d numpy array, of size `(h-1) x w x 3` / `h x (w-1) x 3`

- `crop(image, height, width)`
  - Description:
    This function will reduce the image to the specified size removing rows and columns of pixels from the borders.
  - Input:
    - image (3d np array)
    - desired_height (integer)
    - desired_width (integer)
  - Output:
    - cropped image (3d numpy array, size `desired_height x desired_width x 3`)
- `compress(image, b = 4)`
  - Description:
    This function compresses the image by reducing the number of bits for each channel based on user input.
  - Input:
    - image (3d numpy array)
    - b (integer, range [1, 7] (number of bits used for each channel in the compressed image))
  - Output:
    - image (3d numpy array, compressed to `b` bits)
- `image_size(image)`
  - Description:
    Calculates and returns the size of an image in bytes.
  - Input:
    - image (3d numpy array)
  - Output:
    - size (integer, size in bytes)

There already are packages for image processing in R and Python:
  - [The magick package in R](https://cran.r-project.org/web/packages/magick/vignettes/intro.html)
  - [sckiti-image in Python](https://scikit-image.org/)

The existing packages are very comprehensive and provide many functions such as transformations, filters, file conversions and other advanced functions. Our packages focus specifically on image compression and reducing image size using Dynamic Programming and K-means Clustering.
