import numpy as np
import pytest

def image_size(image):
    """
    Function to estimate the size of an image in bytes

    Parameters: image, a 3d array representation of an image
    like the one returned by plt.imread()

    Returns:
    size, integer, estimated size of the image in number of bytes 

    Example:
    size(image)
    """

    pass

def image_size_test(image):
    """
    Function to test image_size()

    Parameters: image, a 3d array representation of an image
    like the on returned by plt.imread()

    Returns: none

    Example:
    image_size_test(image)
    """

    # test that size returned is not too big
    assert image_size(image, b) < (b+1) * np.prod(image.shape)/8 

    # TypeError should be raised when wrong type passed in
    with pytest.raises(TypeError):
        image_size("file/path/to/image.jpg/or/image.png", b)
    with pytest.raises(TypeError):


    # 

