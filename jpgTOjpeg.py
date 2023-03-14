import os

# specify the path to the directory containing the JPEG files
jpeg_dir = 'training/Normal/'

# specify the path to the output directory for the converted JPG files
jpg_dir = 'Jpg/Normal/'

# iterate over all files in the directory
for filename in os.listdir(jpeg_dir):
    # check if the file has a .jpeg extension
    if filename.endswith('.jpeg'):
        # construct the new filename with a .jpg extension
        new_filename = os.path.splitext(filename)[0] + '.jpg'
        # rename the file
        os.rename(os.path.join(jpeg_dir, filename), os.path.join(jpg_dir, new_filename))
