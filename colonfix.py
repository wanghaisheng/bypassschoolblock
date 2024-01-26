import os

folder_path = "images"

for filename in os.listdir(folder_path):
    if ":" in filename:
        new_filename = filename.replace(":", "")
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
