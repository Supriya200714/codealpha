import os
import shutil

source_folder = "source"
destination_folder = "destination"

# Create destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Check all files in source folder
for file in os.listdir(source_folder):

    # Check if the file is a JPG image
    if file.lower().endswith(".jpg"):

        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        # Move the file
        shutil.move(source_path, destination_path)

        print(file, "moved successfully!")

print("All JPG files have been moved.")