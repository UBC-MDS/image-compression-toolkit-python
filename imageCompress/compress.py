import numpy as np
import os
from sklearn import cluster
from skimage.io import imread, imsave
from imageCompress.image_size import image_size


def compression (img_path: str, b: int, out_path: str) -> str:
    """
    Compresses an image into a format with bits to
    represent each channel.

    Parameters:
    ----------
    img_path: str (file path to a .png image)
    b: int in [1, 8]
    out_path: str (file path to the compressed png image)

    Returns:
    -------
    compressed_img : str (file path to the image with each channel
                    compressed to b bits, same as out_path)
    """

    img = imread(img_path)

    H, W, C = img.shape
    model = cluster.KMeans(n_clusters = 2**b)

    img = img.reshape(H*W, C)
    model.fit(img)
    labels = np.array(model.labels_)
    quantized_img = labels.reshape(H, W)

    colours = model.cluster_centers_.astype('uint8')

    H, W = quantized_img.shape
    img = np.zeros((H,W,C), dtype='uint8')

    for i in range(H):
        for j in range(W):
            img[i, j, :] = colours[quantized_img[i, j], :]

    imsave(out_path, img)

    return out_path

def compress(img_path: str, b: int, out_path: str) -> str:

    """
    Compresses an image into a format with bits to
    represent each channel. Saves the image and returns
    the path to compressed output image specified by the out_path.

    Parameters:
    ----------
    img_path: str (file path to a .png image)
    b: int in [1, 8]
    out_path: str (file path to the compressed png image)

    Returns:
    -------
    compressed_img : str (file path to the image with each channel
                    compressed to b bits, same as out_path)

    Examples:
    -------
    >>> imageCompress.compress("..//image.png", b = 5, "..//compressed_image.png")
    >>> "..//compressed_image.png"
    """

    if type(img_path) != str:
        raise TypeError("Input image path type not correct, make sure you are passing a string!")
    if type(out_path) != str:
        raise TypeError("Output path type not correct, make sure you are passing a string!")
    if type(b) != int:
        raise TypeError("b should be a positive integer <= 8!")
    if b <= 0:
        raise ValueError("b should be a positive integer greater than 0 and less than 9!")
    if b > 8:
        raise ValueError("b should be a positive integer <= 8!")

    min_size_img = compression(img_path, 1, os.path.join((os.path.dirname(os.path.abspath(img_path))), "1.png"))
    desired_size_img = compression(img_path, b, os.path.join((os.path.dirname(os.path.abspath(img_path))), "2.png"))

    if image_size(min_size_img) > image_size(img_path):
        os.remove(min_size_img)
        os.remove(desired_size_img)
        raise Exception ("The image is already compressed")

    elif image_size(desired_size_img) > image_size(img_path):
        os.remove(min_size_img)
        os.remove(desired_size_img)
        raise Exception ("Choose a smaller b to compress the image.")

    else:
        os.remove(min_size_img)
        os.remove(desired_size_img)
        return compression(img_path, b, out_path)
