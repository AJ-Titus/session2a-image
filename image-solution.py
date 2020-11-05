from PIL import Image
import os

# Assignment:
# Create a new folder called "processed" where all images from "raw" are stored in .png.
# They are all cropped to ratio 4:3 (or 3:4) and resized to be all the same size.

# Notice:
# 1. There are different extensions
# 2. They are all different sizes
# 3. We have portrait and landscape orientated images

# Define a cropping ratio
ratio = (4, 3)

# Where are the images?
img_folder = "C:\\Users\\sopsla\\Desktop\\session2a-image\\raw"

# 0. Create a new folder
new_folder = "C:\\Users\\sopsla\\Desktop\\processed"

# This is optional; ensures you can run the script multiple times w/o making new folders
if not os.path.isdir(new_folder):
    os.mkdir(new_folder)

img_list = os.listdir(img_folder)
for file in img_list:
    img = Image.open(os.path.join(img_folder, file))

    # 1. Define portrait and landscape images
    # 2. Figure out on which side you have to crop the image

    if img.height > img.width:
        # this is what defines a portrait picture
        new_width = img.width
        new_height = img.width * ratio[0] / ratio[1]

        if new_height > img.height:
            # sometimes, the ratio may be smaller than 4:3.
            # this would cause black sides to be added to the image.
            # this statement makes sure the image is cropped on the other side instead.
            # It's totally fine if you didn't do this.
            new_height = img.height
            new_width = img.height * ratio[1] / ratio[0]

        offset = (img.height - new_height) / 2  # this is how much we must cut off on each side
        box = (0, offset, new_width, img.height - offset)
        new_size = (300, 400)

    else:
        # this encompasses landscape images and square images.
        new_height = img.height
        new_width = img.height * ratio[0] / ratio[1]

        if new_width > img.width:
            # see above
            new_width = img.width
            new_height = img.width * ratio[1] / ratio[0]

        offset = (img.width - new_width) / 2
        box = (offset, 0, new_width + offset, new_height)
        new_size = (400, 300)

    # 3. Crop the image
    img_crop = img.crop(box)

    # 4. Resize the image
    img_rsz = img_crop.resize(new_size)

    # split the extension
    filename, extension = os.path.splitext(file)
    outfile = filename + ".png"

    # 5. Save it to your new folder with the new extension
    img_rsz.save(os.path.join(new_folder, outfile), "PNG")

    # That's it!
