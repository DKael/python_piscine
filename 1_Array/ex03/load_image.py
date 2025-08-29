from PIL import Image

def ft_load(path: str) -> list:
	"""
    Load an image from the given file path and return its pixel values as a nested list.

    This function attempts to open an image file and prints its metadata
    (format, width, height, mode). If the file cannot be opened due to
    various errors (missing file, invalid format, permission issues, etc.),
    the error is caught and printed, and the function returns None.

    Parameters
    ----------
    path : str
        Path to the image file.

    Returns
    -------
    list of list
        A 2D list representing the pixel values of the image. Each inner list
        corresponds to one row of pixels. The content of each pixel depends
        on the image mode:
            - RGB: (R, G, B) tuples
            - RGBA: (R, G, B, A) tuples
            - L: grayscale values (int)

        Returns None if the image cannot be opened.

    Raises
    ------
    Prints error messages instead of raising exceptions directly:
        - FileNotFoundError : If the file path does not exist.
        - PIL.UnidentifiedImageError : If the file is not a valid image.
        - PermissionError : If the file cannot be opened due to permissions.
        - Exception : Any other unexpected error.

    Examples
    --------
    >>> pixels = ft_load("cat.png")
    image format:    PNG
    image width:     256
    image height:    256
    image mode:      RGB
    >>> pixels[0][0]
    (123, 45, 67)
    """
	try:
		img = Image.open(fp=path)
	except FileNotFoundError as e:
		print(f"Cannot find the fild: {e}")
	except Image.UnidentifiedImageError as e:
		print(f"Not valid fild format: {e}")
	except PermissionError as e:
		print(f"No permission to open the file: {e}")
	except Exception as e:
		print(f"Error: {e}")
	else:
		print("image format:\t",img.format_description)
		print("image width:\t", img.width)
		print("image height:\t", img.height)
		print("image mode:\t", img.mode)
		pixels_1d = list(img.getdata())
		w, h = img.size
		pixels = [pixels_1d[i * w:(i+1) * w] for i in range(h)]
		return pixels