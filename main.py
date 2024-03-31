from PIL import Image
import os


# Set the input and output directories
input_directory = "/Users/omidshojaeianzanjani/Desktop/Mega2"
output_directory = "/Users/omidshojaeianzanjani/Desktop/Mega2/output_images"

# 6.7” :  1290 x 2796px or 2796 x 1290px

# 6.5” : 1242x2688 - 1284x2778

# 5.5” : 1242x2208
# Define the target sizes and corresponding output directories

# Screenshots dimensions should be: 2048 x 2732px or 2732 x 2048px
# Screenshots dimensions should be: 2048 x 2732px or 2732 x 2048px
target_sizes = {
    (1290, 2796): "output_images_6.7 inch - 1290 x 2796",
    (2796, 1290): "output_images_6.7 inch - 2 - 2796 x 1290",
    (1242, 2688): "output_images_6.5 inch - 1242x2688",
    (1284, 2778): "output_images_6.5 inch- 2 - 1284x2778",
    (1242, 2208): "output_images_5.5 inch - 1242x2208",

    (2048, 2732): "output_images_iPad 6 edition 12.9 inch - 2048 x 2732",
    (2732, 2048): "output_images_iPad 6 edition 12.9 inch - 2732 x 2048",
    (2048, 2732): "output_images_iPad 6 edition 12.9 inch - 2 edition 2048 x 2732",
    (2732, 2048): "output_images_iPad 6 edition 12.9 inch - 2 edition 2732 x 2048"
    # Add more target sizes and corresponding output directories as needed
}

# Ensure the output directories exist
for output_directory in target_sizes.values():
    os.makedirs(output_directory, exist_ok=True)

# Loop through all images in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Open the image
        image_path = os.path.join(input_directory, filename)
        img = Image.open(image_path)

        # Resize the image for each target size
        for target_size, output_dir in target_sizes.items():
            # Resize the image
            resized_img = img.resize(target_size, Image.ANTIALIAS)

            # Save the resized image to the corresponding output directory
            output_path = os.path.join(output_dir, filename)
            resized_img.save(output_path)

print("All images resized successfully!")