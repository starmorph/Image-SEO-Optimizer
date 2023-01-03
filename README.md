# Image SEO Optimization
## This python script helps optimize images for search engines by renaming and updating the alt text of images in a given directory.

## Features

- Renames all images in a given directory with a specified new filename and a counter.
- Updates the alt text of all images in the directory with a specified keyword.

## Usage

To use the script, call the `rename_images` function with the following arguments:

`python`
rename_images(directory, new_filename, alt_keyword)
directory is the path to the directory containing the images to be renamed and optimized.

`new_filename` is the new base filename to be used for the images. The counter will be appended to the end of the filename for each image.

`alt_keyword` is the keyword to be used for the alt text of the images.

For example, the following call will rename and optimize the images in the current directory:

Copy code
rename_images('./', '3d-abstract-book', 'alt_keyword')

## Supported Image Formats
The script currently supports .jpg, .png, and .webp image formats.

## Dependencies
The script requires the following libraries:
os
PIL (Python Imaging Library)

## Note
The script uses the show method of the Image class from the PIL library to update the alt text of the images. This method will open the images in the default image viewer of the operating system, allowing you to edit the alt text of the images manually. After editing the alt text, you will need to save the images and close the image viewer for the changes to take effect.
