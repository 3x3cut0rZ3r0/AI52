from PIL import Image
import numpy as np

# Load the image
img = Image.open("char.png").convert("L")  # "L" = grayscale

# Convert to NumPy array
pixels = np.array(img)

np.set_printoptions(threshold=np.inf)

print("Shape of image:", pixels.shape)  # (height, width)
print("Pixel values:\n", pixels)
