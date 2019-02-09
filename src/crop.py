
import numpy as np
import pytest


def crop(image, height, width):
    '''
    Function to crop images

    Parameters:
    image, a 3d array of the image (obtained using plt.imread(image))
    height, integer, the desired height of the cropped image
    width, integer, the desired width of the cropped image

    Returns:
    cropped_image, a 3d array with dimensions height x width x 3

    Example:
    crop(image, 10, 15) returns an array with shape (10, 15, 3)
    '''
    pass

def crop_test(image):
    '''
    Function to test crop() function

    Parameter: image, a 3d array of an image to be used to test crop
    Returns: None

    '''

    # Test for correct shape
    assert crop(image, 15, 10).shape == (15, 10, 3)
    assert crop(image, 10, 5).shape == (10, 4, 3)
    assert crop(image, 6, 6).shape == (6, 6, 3)
    assert crop(image, 1, 1).shape == (1, 1, 3)
    assert crop(image, image.shape[0], image.shape[1]).shape == image.shape

    # ValueError should be raised when invalid dimensions are entered
    with pytest.raises(ValueError):
        crop(image, -1, 10)
    with pytest.raises(ValueError):
        crop(image, 10, -1)
    with pytest.raises(ValueError):
        crop(image, 0, 0)
    with pytest.raises(ValueError):
        crop(image, 0, 10)
    with pytest.raises(ValueError):
        crop(image, 10, 0)
    with pytest.raises(ValueError):
        crop(image, int(1e30), 10)
    with pytest.raises(ValueError):
        crop(image, 10, int(1e30))
    with pytest.raises(ValueError):
        crop(image, int(-1e30), 10)
    with pytest.raises(ValueError):
        crop(image, 10, int(-1e30))

    # TypeError should be raised when the wrong type is entered
    with pytest.raises(TypeError):
        crop(image, 9.5, 10)
    with pytest.raises(TypeError):
        crop(image, 10, 9.5)
    with pytest.raises(TypeError):
        crop(image, 9.5, 9.5)
    with pytest.raises(TypeError):
        crop(image, -9.9, -4.5)
    with pytest.raises(TypeError):
        crop(image, "10", True)
    with pytest.raises(TypeError):
        crop("image", 10, 10)
