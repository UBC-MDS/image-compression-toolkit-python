def crop(image, height, width):
    """
    Function to crop images

    Parameters:
    ----------
    image, a 3d array of the image (obtained using plt.imread(image))
    height, integer, the desired height of the cropped image
    width, integer, the desired width of the cropped image

    Returns:
    --------
    cropped_image, a 3d array with dimensions height x width x 3

    Example:
    crop(image, 10, 15) returns an array with shape (10, 15, 3)
    """
    pass

def image_size(image):
    """
    Function to estimate the size of an image in bytes

    Parameters:
    ----------
    image, a 3d array representation of an image
    like the one returned by plt.imread()

    Returns:
    --------
    size, integer, estimated size of the image in number of bytes

    Example:
    size(image)
    """

    pass

def compress(img, b):
    """
    Compresses an image into a format with bits to
    represent each channel.

    Parameters:
    ----------
    img : a (H,W,3) numpy array
    b   : an integer

    Returns:
    -------
    compressed_img : a (H,W,3) numpy array with each channel
                    compressed to b bits
    """

    pass
