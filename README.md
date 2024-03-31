Image Resizer
This Python script resizes images to fit various device screen sizes and saves the resized images in their respective output directories.

Prerequisites
Python 3.x
Pillow library (PIL fork)
Installation
Install Python 3.x from the official website: https://www.python.org/downloads/
Install Pillow using pip:
Copy code
pip install pillow
Usage
Prepare your input images in a single directory.
Set the input_directory variable in the script to the path of the input images directory.
Set the output_directory variable in the script to the path where you want to save the resized images.
Run the script:
bash
Copy code
python image_resizer.py
Configuration
The script uses a list of tuples named target_sizes to define the target sizes and corresponding output directories. Each tuple contains a tuple of width and height, and a string representing the output directory name.

For example, to add a new target size of 1080x1920 and the corresponding output directory "output_images_1080x1920", modify the target_sizes list as follows:

python
Copy code
target_sizes = [
    #...
    ((1080, 1920), "output_images_1080x1920"),
    #...
]
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This script is based on the Pillow library (https://pillow.readthedocs.io/en/stable/) and the Python Standard Library (https://docs.python.org/3/library/index.html).

