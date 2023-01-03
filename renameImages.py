import os
from PIL import Image
imagetype = ".webp"
def rename_images(directory, new_filename, alt_keyword):
    # get a list of all the image filenames in the directory
    image_filenames = [f for f in os.listdir(directory) if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.webp')]

    # rename the images
    for i, filename in enumerate(image_filenames):
        # construct the new filename with the counter
        new_filename_with_counter = f"{new_filename}_{i+1}"

        # rename the image file
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename_with_counter + imagetype))

        # open the image and update the alt text
        with Image.open(os.path.join(directory, new_filename_with_counter + imagetype)) as img:
            img.show()
            img.close()

# example usage
rename_images('./', '3d-abstract-book', 'alt_keyword')
