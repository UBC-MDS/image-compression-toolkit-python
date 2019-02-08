
import numpy as np
import pytest
from imageFunctions import util

class Test_crop():

    def test_crop_shape(self):
        '''
        Function to test that the crop() function returns an image 
        of the correct shape
        '''

        # Test for correct shape
        assert util.crop(image, 15, 10).shape == (15, 10, 3)
        assert util.crop(image, 10, 5).shape == (10, 5, 3)
        assert util.crop(image, 6, 6).shape == (6, 6, 3)
        assert util.crop(image, 5, 5).shape == (5, 5, 3)
        assert util.crop(image, 1, 1).shape == (1, 1, 3)
        assert util.crop(image, image.shape[0], image.shape[1]).shape == image.shape

    def test_crop_value(self):
        """
        Function to test that ValueErrors are raised when invalid width and
        height are entered
        """
        with pytest.raises(ValueError):
            util.crop(image, -1, 10)
        with pytest.raises(ValueError):
            util.crop(image, 10, -1)
        with pytest.raises(ValueError):
            util.crop(image, 0, 0)
        with pytest.raises(ValueError):
            util.crop(image, 0, 10)
        with pytest.raises(ValueError):
            util.crop(image, 10, 0)
        with pytest.raises(ValueError):
            util.crop(image, image.shape[0], 10)
        with pytest.raises(ValueError):
            util.crop(image, 10, image.shape[1] + 1)
        with pytest.raises(ValueError):
            util.crop(image, int(-1e30), 10)
        with pytest.raises(ValueError):
            util.crop(image, 10, int(-1e30))

    def test_crop_type(self):
        """
        Function to test that a TypeError is raised when the wrong type of input
        is passed into the function.
        """
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
            crop("image.jpg", 10, 10)

class Test_image_size():
    
    def test_size_output(self):
        """
        Function to test that image_size() returns the right size function
        """
        assert image_size(image, 7) < 8 * np.prod(image.shape)/8
        assert image_size(image, 1) < 2 * np.prod(image.shape)/8 
        assert image_size(image, 3) < 4 * np.prod(image.shape)/8

    def test_size_type(self):
        with pytest.raises(TypeError):
            image_size("file/path/to/image.jpg/or/image.png", 8)
        with pytest.raises(TypeError):
            image_size(image, 7.5)
        with pytest.raises(TypeError):
            image_size("image.jpg", True)

    def test_size_value(self):
        with pytest.raises(ValueError):
            image_size(image, -1)
        with pytest.raises(ValueError):
            image_size(image, 9)
        with pytest.raises(ValueError):
            image_size(image, 0)
        with pytest.raises(ValueError):
            image_size(image, 1000)
        with pytest.raises(ValueError):
            image_size(image, -1000)

        
