import os
import argparse
from PIL import Image
import shutil

# Configurable extensions
SUPPORTED_EXTENSIONS = [".jpg", ".jpeg", ".png"]

def is_bw(image):
    if image.mode not in ("L", "RGB"):
        image = image.convert("RGB")
    if image.mode == "L":
        return True
    rgb = image.convert("RGB")
    for pixel in rgb.getdata():
        r, g, b = pixel
        if r != g or g != b:
            return False
    return True

def copy_images_by_type(source, destination, image_type):
    os.makedirs(destination, exist_ok=True)
    for file in os.listdir(source):
        path = os.path.join(source, file)
        if os.path.isfile(path) and any(file.lower().endswith(ext) for ext in SUPPORTED_EXTENSIONS):
            try:
                img = Image.open(path)
                bw = is_bw(img)
                if (image_type == "bw" and bw) or (image_type == "colour" and not bw):
                    shutil.copy(path, os.path.join(destination, file))
            except Exception as e:
                print(f"Error processing {file}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy images by type: black and white or colour.")
    parser.add_argument("--source", required=True, help="Path to the source directory containing images.")
    parser.add_argument("--destination", required=True, help="Path to the destination directory.")
    parser.add_argument("--type", required=True, choices=["bw", "colour"], help="Type of images to copy: 'bw' or 'colour'.")
    args = parser.parse_args()

    copy_images_by_type(args.source, args.destination, args.type)
