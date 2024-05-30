import os
import sys
from PIL import Image

def is_safe_path(basedir, path):
    return os.path.abspath(path).startswith(basedir)

def convert_png_to_jpeg(input_folder, output_folder):
    # Ensure the output folder exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            # Build the file paths
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpeg")
            print("input_path:" + input_path + " output_path:" + output_path)
            # Open the PNG image
            with Image.open(input_path) as img:
                # Convert and save as JPEG with the best quality
                img.convert("RGB").save(output_path, "JPEG", quality=95)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_folder> <output_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    base_dir = os.path.abspath(os.getcwd())

    if not is_safe_path(base_dir, input_folder) or not is_safe_path(base_dir, output_folder):
        print("Error: One or both of the provided paths are not safe.")
        sys.exit(1)

    convert_png_to_jpeg(input_folder, output_folder)
