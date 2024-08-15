from PIL import Image, ImageFilter
import os

# other features like crop , filters , cutting , pasting and merging images
# Define the path to the image
image_path = r'.\images\img1.jpg'

# Check if the file exists
if not os.path.exists(image_path):
    raise FileNotFoundError(f"File not found: {os.path.abspath(image_path)}")

# Open the image
img = Image.open(image_path)

# Apply image filters and save the results

# 1. Apply a blur filter to the image
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", 'png')
# rotate the image
filtered_img.rotate(80)
# display the image
# filtered_img.show()

# 2. Apply a smooth filter to the image
filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save("smooth.png", 'png')


# 3. Convert the image to grayscale
convert_img = img.convert('L')
convert_img.save("grey.png", 'png')
# resize the image
convert_img.resize((100,100))
print("Resize" , convert_img.size)
# Print image attributes for reference
print("Image Object:", img)
print("Format:", img.format)
print("Size:", img.size)
print("Mode:", img.mode)
