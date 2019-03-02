import os

def image_size(img_path):
    """
    Function to estimate the size of an image in bytes

    Parameters:
    ----------
    img_path : str (file path to the image)

    Returns:
    --------
    size, integer, estimated size of the image in number of bytes

    Example:
    image_size(image_path)
    """
    if type(img_path) != str:
        raise TypeError("Image path invalid, pass a correct path (string)!")

    file_info = os.stat(img_path)
    size = file_info.st_size
    print("The file size in bytes is:", size)
    return size
