import numpy as np
import pytest
import os
from imageCompress.compress import compress
from imageCompress.image_size import image_size
from imageCompress.crop import crop
from skimage.io import imread

# images for testing
test_images = ["data/test_image_1717.png", "data/test_image_1718.png", "data/test_image_1816.png", "data/test_image_1819.png" ]
img_path = "data/test_image_1819.png"
small_img = "data/image_1.png"
big_img = "data/bigger_test.png"
outpath = os.path.join((os.path.dirname(os.path.abspath(img_path))), "test.png")

class Test_crop():

    def test_crop_shape(self):
        '''
        Function to test that the crop() function returns an image
        of the correct shape for different input shapes
        '''

        for image in test_images:

            cropped_image = crop(image, 15, 10, outpath)
            assert imread(cropped_image).shape[0:2] == (15, 10)

            cropped_image = crop(image, 10, 5, outpath)
            assert imread(cropped_image).shape[0:2] == (10, 5)

            cropped_image = crop(image, 6, 6, outpath)
            assert imread(cropped_image).shape[0:2] == (6, 6)

            cropped_image = crop(image, 5, 5, outpath)
            assert imread(cropped_image).shape[0:2] == (5, 5)

            cropped_image = crop(image, 1, 1, outpath)
            assert imread(cropped_image).shape [0:2]== (1, 1)

            cropped_image = crop(image, imread(image).shape[0], imread(image).shape[1], outpath)
            assert imread(cropped_image).shape == imread(image).shape

    def test_crop_value(self):
        '''
        Function to test that ValueErrors are raised when invalid width and
        height are entered
        '''
        with pytest.raises(ValueError):
            crop(img_path, -1, 10, outpath)
        with pytest.raises(ValueError):
            crop(img_path, 10, -1, outpath)
        with pytest.raises(ValueError):
            crop(img_path, 0, 0, outpath)
        with pytest.raises(ValueError):
            crop(img_path, 0, 10, outpath)
        with pytest.raises(ValueError):
            crop(img_path, 10, 0, outpath)
        with pytest.raises(ValueError):
            crop(img_path, imread(img_path).shape[0] + 1, 10, outpath)
        with pytest.raises(ValueError):
            crop(img_path, 10, imread(img_path).shape[1] + 1, outpath)
        with pytest.raises(ValueError):
            crop(img_path, int(-1e30), 10, outpath)
        with pytest.raises(ValueError):
            crop(img_path, 10, int(-1e30), outpath)

    def test_crop_type(self):
        '''
        Function to test that a TypeError is raised when the
        wrong type of input is passed into the function.
        '''
        with pytest.raises(TypeError):
            crop(img_path, 9.5, 10, outpath)
        with pytest.raises(TypeError):
            crop(img_path, 10, 9.5, outpath)
        with pytest.raises(TypeError):
            crop(img_path, 9.5, 9.5, outpath)
        with pytest.raises(TypeError):
            crop(img_path, -9.9, -4.5, outpath)
        with pytest.raises(TypeError):
            crop(5, "10", True, outpath)
        with pytest.raises(TypeError):
            crop(np.random.randint(0,255,(18,19,3)).astype("uint8"), 10, 10, outpath)
        with pytest.raises(TypeError):
            crop(img_path, 5, 5, 5)

    def test_crop_input_shape(self):
        '''
        Test that input image has correct shape
        '''
        assert np.size(imread(img_path).shape) in [2, 3]


class Test_compress():

    def test_compress_shape(self):
        '''
        Function to test that compressed image shape is the same
        '''
        com_path = compress(img_path, 3, outpath)
        assert imread(com_path).shape == imread(img_path).shape

        com_path = compress(img_path, 1, outpath)
        assert imread(com_path).shape == imread(img_path).shape

        com_path = compress(img_path, 6, outpath)
        assert imread(com_path).shape == imread(img_path).shape

    def test_compress_type(self):
        '''
        Function to test that a TypeError is raised when an invalid type is
        passed in for image or b
        '''
        with pytest.raises(TypeError):
            compress(img_path, 6.5, outpath)
        with pytest.raises(TypeError):
            compress(imread(img_path), 2, outpath)
        with pytest.raises(TypeError):
            compress(5, True, outpath)
        with pytest.raises(TypeError):
            compress(img_path, 3, 5)

    def test_compress_value(self):
        '''
        Function to test that a ValueError is raised
        when invalid values are passed in for b
        '''
        with pytest.raises(ValueError):
            compress(img_path, -1, outpath)
        with pytest.raises(ValueError):
            compress(img_path, 9, outpath)
        with pytest.raises(ValueError):
            compress(img_path, 0, outpath)
        with pytest.raises(ValueError):
            compress(img_path, 1000, outpath)
        with pytest.raises(ValueError):
            compress(img_path, -1000, outpath)

    def test_compress_input_shape(self):
        '''
        Test that input image has correct shape
        '''
        assert np.size(imread(img_path).shape) in [2,3]

    def test_compress_size(self):
        '''
        Function to test that the size of the compressed image
        is correct
        '''
        compressed_img = compress(img_path, 3, outpath)
        assert image_size(compressed_img) < 7/8 * image_size(img_path)
        
        compressed_img = compress(img_path, 1, outpath)
        assert image_size(compressed_img) < 5/8 * image_size(img_path)

        compressed_img = compress(img_path, 6, outpath)
        assert image_size(compressed_img) <= 8/8 * image_size(img_path)

        compressed_img = compress(img_path, 8, outpath)
        assert image_size(compressed_img) <= image_size(img_path)

    def test_compress_already_compressed(self):
        '''
        Function to test that the function raises exceptions when
        images that cannot be compressed further are passed in
        '''
        with pytest.raises(Exception):
            compress(small_img, 8, outpath)
        with pytest.raises(Exception):
            compress(small_img, 1, outpath)

    def test_compress_smaller_b(self):
        '''
        Function to test that an exception gets raised when a smaller b
        needs to be chosen in order to compress the image
        '''
        with pytest.raises(Exception):
            compress(big_img, 4, outpath)

class Test_image_size():

    def test_size_output(self):
        '''
        Function to test that correct size is returned
        '''
        assert image_size(img_path) <= 1.1 * imread(img_path).nbytes 

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
        Test that input image has correct shape
        '''
        assert np.size(imread(img_path).shape) in [2, 3]
