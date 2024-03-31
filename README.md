### Image Resizer Readme

This Python script is designed to resize images to specific dimensions using the Python Imaging Library (PIL). Below is an explanation of the script's functionality and how to use it effectively.

### Prerequisites

Before using this script, ensure you have Python installed on your system. Additionally, install the Python Imaging Library (PIL) by running:

pip install pillow


### Usage

1. **Input and Output Directories:**
   - Set the `input_directory` variable to the path of the directory containing the input images.
   - Set the `output_directory` variable to the path where you want to save the resized images.

2. **Target Sizes:**
   - Define the target sizes for the resized images along with the corresponding output directories in the `target_sizes` list.
   - Each item in the list should be a tuple containing the target size (width, height) and the output directory name.
   - Ensure to add all desired target sizes and output directories to the list.

3. **Execution:**
   - Run the script using Python.
   - The script will resize each image in the input directory to the specified target sizes and save the resized images in the corresponding output directories.

### Example

```python
python resize_images.py

Notes
Ensure that the input directory contains the images you want to resize.
The script currently supports JPEG and PNG image formats.
If any target size directories don't exist, the script will create them automatically.
The resized images will be saved with the same filenames as the original images in their respective output directories.
Author
Omid Shojaeian

License
This script is released under the [License Name] license. See the LICENSE file for details.

Feel free to copy and paste this content into your README file as needed. Let me know if you need further assistance!
