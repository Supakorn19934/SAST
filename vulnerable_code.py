from PIL import Image
import os,sys

def convert_png_to_jpeg(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            # Build the file paths
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpeg")
            print("input_path:"+input_path+" output_path:"+output_path)
            # Open the PNG image
            with Image.open(input_path) as img:
                # Convert and save as JPEG with the best quality
                img.convert("RGB").save(output_path, "JPEG", quality=95)

if __name__ == "__main__":
    # Replace 'input_folder' and 'output_folder' with your actual folder paths
    print("Input folder:"+sys.argv[1])
    print("Output folder:"+sys.argv[2])
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    convert_png_to_jpeg(input_folder, output_folder)
