import numpy as np
import pytest
from imageCompress.compress import compress
from imageCompress.image_size import image_size
from imageCompress.crop import crop
from skimage.io import imread

# add the random image path here
#img_path = "data/sample.png"

# class Test_crop():
#
#     def test_crop_shape(self):
#         '''
#         Function to test that the crop() function returns an image
#         of the correct shape
#         '''
#         # Test for correct shape
#         assert util.crop(image, 15, 10).shape == (15, 10, 3)
#         assert util.crop(image, 10, 5).shape == (10, 5, 3)
#         assert util.crop(image, 6, 6).shape == (6, 6, 3)
#         assert util.crop(image, 5, 5).shape == (5, 5, 3)
#         assert util.crop(image, 1, 1).shape == (1, 1, 3)
#         assert util.crop(image, image.shape[0], image.shape[1]).shape == image.shape
#
#     def test_crop_value(self):
#         '''
#         Function to test that ValueErrors are raised when invalid width and
#         height are entered
#         '''
#         with pytest.raises(ValueError):
#             util.crop(image, -1, 10)
#         with pytest.raises(ValueError):
#             util.crop(image, 10, -1)
#         with pytest.raises(ValueError):
#             util.crop(image, 0, 0)
#         with pytest.raises(ValueError):
#             util.crop(image, 0, 10)
#         with pytest.raises(ValueError):
#             util.crop(image, 10, 0)
#         with pytest.raises(ValueError):
#             util.crop(image, image.shape[0] + 1, 10)
#         with pytest.raises(ValueError):
#             util.crop(image, 10, image.shape[1] + 1)
#         with pytest.raises(ValueError):
#             util.crop(image, int(-1e30), 10)
#         with pytest.raises(ValueError):
#             util.crop(image, 10, int(-1e30))
#
#     def test_crop_type(self):
#         '''
#         Function to test that a TypeError is raised when the
#         wrong type of input is passed into the function.
#         '''
#         with pytest.raises(TypeError):
#             util.crop(image, 9.5, 10)
#         with pytest.raises(TypeError):
#             util.crop(image, 10, 9.5)
#         with pytest.raises(TypeError):
#             util.crop(image, 9.5, 9.5)
#         with pytest.raises(TypeError):
#             util.crop(image, -9.9, -4.5)
#         with pytest.raises(TypeError):
#             util.crop(image, "10", True)
#         with pytest.raises(TypeError):
#             util.crop("image.jpg", 10, 10)
#
#     def test_crop_input_shape(self):
#         '''
#         Test that correct image has correct shape
#         '''
#         assert np.size(image.shape) == 3


class Test_compress():

    def test_compress_shape(self):
        '''
        Function to test that compressed image shape is the same
        '''
        com_path = compress(img_path, 3)
        assert imread(com_path).shape == imread(img_path).shape
        com_path = compress(img_path, 1)
        assert imread(com_path).shape == imread(img_path).shape

    def test_compress_type(self):
        '''
        Function to test that a TypeError is raised when an invalid type is
        passed in for image or b
        '''
        with pytest.raises(TypeError):
            compress("file/path/to/image.jpg/or/image.png", 6.5)
        with pytest.raises(TypeError):
            compress(imread(img_path), 2)
        with pytest.raises(TypeError):
            compress("image.jpg", True)

    def test_compress_value(self):
        '''
        Function to test that a ValueError is raised
        when invalid values are passed in for b
        '''
        with pytest.raises(ValueError):
            compress(img_path, -1)
        with pytest.raises(ValueError):
            compress(img_path, 9)
        with pytest.raises(ValueError):
            compress(img_path, 0)
        with pytest.raises(ValueError):
            compress(img_path, 1000)
        with pytest.raises(ValueError):
            compress(img_path, -1000)

    def test_compress_input_shape(self):
        '''
        Test that correct image has correct shape
        '''
        assert np.size(
            imread(img_path).shape) == 3, "The image should not have more than 3 dimensions!"

    def test_compress_size(self):
        '''
        Function to test that the size of the compressed image
        is correct
        '''
        compressed_img = compress(img_path, 3)
        assert image_size(compressed_img) < 4/8 * image_size(img_path)
        compressed_img = compress(img_path, 1)
        assert image_size(compressed_img) < 2/8 * image_size(img_path)

class Test_image_size():

    def test_size_output(self):
        '''
        Function to test that correct size is returned
        '''
        assert image_size(img_path) <= imread(img_path).nbytes

    def test_size_type(self):
        '''
        Function to test that a TypeError is raised when invalid type is passed in
        as image
        '''
        with pytest.raises(TypeError):
            image_size(imread(img_path))
        with pytest.raises(TypeError):
            image_size(True)
        with pytest.raises(TypeError):
            image_size(123)
        with pytest.raises(TypeError):
            image_size(12.2)

    def test_size_input_shape(self):
        '''
        Test that correct image has correct shape
        '''
        assert np.size(imread(img_path).shape) == 3
