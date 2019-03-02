import numpy as np
import os
from sklearn import cluster
from skimage.io import imread, imsave

def compress(img_path, b):
    """
    Compresses an image into a format with bits to
    represent each channel.

    Parameters:
    ----------
    img_path : str (file path to the image)
    b   : int

    Returns:
    -------
    compressed_img : str (file path to the image with each channel
                    compressed to b bits)
    """

    if type(img_path) != str:
        raise TypeError("Image path not correct, make sure you are passing a string!")

    if type(b) != int:
        raise TypeError("b should be a positive integer <= 8!")

    if b <= 0 or b > 8:
        raise ValueError("b should be a positive integer <= 8!")

    img = imread(img_path)

    H, W, C = img.shape
    print(img.shape)
    model = cluster.KMeans(n_clusters=2**b)

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

    path = os.path.dirname(os.path.abspath(img_path))
    compressed_img_path = os.path.join(path, "compressed_img.png")
    imsave(compressed_img_path, img)

    print("The compressed image is saved at the path:", compressed_img_path)
    return compressed_img_path
