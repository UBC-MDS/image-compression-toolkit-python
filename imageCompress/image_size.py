import os

def image_size(img_path: str) -> int:
    """
    Function to estimate the size of an image in bytes. The function
    calculates and returns the size of the file which is provided
    in the input as the path.

    Parameters:
    ----------
    img_path : str (file path to the image)

    Returns:
    --------
    size, integer, estimated size of the image in number of bytes

    Example:
    >>> image_size(image_path)
    >>> 87546
    """
    if type(img_path) != str:
        raise TypeError("Image path is invalid, pass a valid PNG input image path (should be in string format)!")

    file_info = os.stat(img_path)
    size = file_info.st_size
    return size
