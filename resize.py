from PIL import Image
import os

input_folder = "training/Normal"
output_folder = "output/Normal"
new_size = (512, 512)  # specify the new size of the photos

# loop through all the photos in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg"):  # check if the file is a JPEG image
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # open the image and resize it
        with Image.open(input_path) as im:
            im_resized = im.resize(new_size)
            im_resized.save(output_path)
