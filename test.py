
import numpy as np
import pytest
from imageCompress import util

image = np.random.randint(0,255,(10,10,3)).astype("uint8")

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
        '''
        Function to test that ValueErrors are raised when invalid width and
        height are entered
        '''
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
            util.crop(image, image.shape[0] + 1, 10)
        with pytest.raises(ValueError):
            util.crop(image, 10, image.shape[1] + 1)
        with pytest.raises(ValueError):
            util.crop(image, int(-1e30), 10)
        with pytest.raises(ValueError):
            util.crop(image, 10, int(-1e30))

    def test_crop_type(self):
        '''
        Function to test that a TypeError is raised when the
        wrong type of input is passed into the function.
        '''
        with pytest.raises(TypeError):
            util.crop(image, 9.5, 10)
        with pytest.raises(TypeError):
            util.crop(image, 10, 9.5)
        with pytest.raises(TypeError):
            util.crop(image, 9.5, 9.5)
        with pytest.raises(TypeError):
            util.crop(image, -9.9, -4.5)
        with pytest.raises(TypeError):
            util.crop(image, "10", True)
        with pytest.raises(TypeError):
            util.crop("image.jpg", 10, 10)

    def test_crop_input_shape(self):
        '''
        Test that correct image has correct shape
        '''
        assert np.size(image.shape) == 3

class Test_compress():

    def test_compress_shape(self):
        '''
        Function to test that compressed image shape is the same
        '''
        assert util.compress(image, 7).shape == image.shape
        assert util.compress(image, 2).shape == image.shape

    def test_compress_type(self):
        '''
        Function to test that a TypeError is raised when an invalid type is
        passed in for image or b
        '''
        with pytest.raises(TypeError):
            util.compress("file/path/to/image.jpg/or/image.png", 6)
        with pytest.raises(TypeError):
            util.compress(image, 7.5)
        with pytest.raises(TypeError):
            util.compress("image.jpg", True)

    def test_compress_value(self):
        '''
        Function to test that a ValueError is raised
        when invalid values are passed in for b
        '''
        with pytest.raises(ValueError):
            util.compress(image, -1)
        with pytest.raises(ValueError):
            util.compress(image, 9)
        with pytest.raises(ValueError):
            util.compress(image, 0)
        with pytest.raises(ValueError):
            util.compress(image, 1000)
        with pytest.raises(ValueError):
            util.compress(image, -1000)

    def test_compress_input_shape(self):
        '''
        Test that correct image has correct shape
        '''
        assert np.size(image.shape) == 3

    def test_compress_size(self):
        '''
        Function to test that the size of the compressed image
        is correct
        '''
        assert util.image_size(util.compress(image, 7)) < 8 * np.prod(util.compress(image, 7).shape)/8
        assert util.image_size(util.compress(image, 1)) < 2 * np.prod(util.compress(image, 1).shape)/8
        assert util.image_size(util.compress(image, 3)) < 4 * np.prod(util.compress(image, 3).shape)/8

class Test_image_size():

    def test_size_output(self):
        '''
        Function to test that correct size is returned
        '''
        assert util.image_size(image) < 9 * np.prod(image.shape)/8

    def test_size_type(self):
        '''
        Function to test that a TypeError is raised when invalid type is passed in
        as image
        '''
        with pytest.raises(TypeError):
            util.image_size("image.jpg")

    def test_size_input_shape(self):
        '''
        Test that correct image has correct shape
        '''
        assert np.size(image.shape) == 3
