# Image SEO Optimization
## This python script helps optimize images for search engines by renaming all images in a given directory.

![Image SEO Optimizer Starmorph](https://i.imgur.com/px4LHGI.png)
Created by [Starmorph Web Design](https://starmorph.com)

## Features

- Renames all images in a given directory with a specified new filename and a counter.

## Future Features
- Generate alt text with AI.
- Image compression
- Image filetype conversion

## Usage

To use the script, call the `rename_images` function with the following arguments:

```
rename_images(directory, new_filename, alt_keyword)
```
`directory` is the path to the directory containing the images to be renamed and optimized.

`new_filename` is the new base filename to be used for the images. The counter will be appended to the end of the filename for each image.

For example, the following call will rename and optimize the images in the current directory:

```
rename_images('./', '3d-abstract-book')
```

## Supported Image Formats
The script currently supports .jpg, .png, and .webp image formats.

## Dependencies
The script requires the following libraries:
os
PIL (Python Imaging Library)
