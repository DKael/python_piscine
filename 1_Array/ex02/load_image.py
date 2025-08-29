from PIL import Image

def ft_load(path: str) -> list:
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
		pixel_values = []
		for h in range(img.height):
			row = []
			for w in range(img.width):
				row.append(img.getpixel((w, h)))
			pixel_values.append(row)
		return pixel_values