# Modules
from datetime import datetime
from PIL import Image
import filter as filter

# Time duration
start = datetime.now()

# Import image
print("Please enter the image file (e.g. image.png)")

# Open image
while True:
    path = input("File name: ")
    try:
        img = Image.open(path)
        break
    except FileNotFoundError:
        print(f"File '{path}' was not found")
    except NameError:
        print(f"Name '{path}' is not found")

# Current fitlering: grayscale conversion
img = filter.filter(img=img,
                    rgb_r=144,
                    rgb_g=234,
                    rgb_b=122)


# Save image
img.save("new_image.jpg")

end = datetime.now()

# Output
print(f"Image {img} created")
print(f"Process duration: {end-start}")
