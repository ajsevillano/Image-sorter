import os
from PIL import Image
import shutil

# Configuration array
config = {
    "source": "",  # Path to the source directory containing images
    "destination": "",  # Path to the destination directory for colour images
    "supported_extensions": [".jpg", ".jpeg", ".png"]  # Supported file extensions
}

os.makedirs(config["destination"], exist_ok=True)

def is_bw(image):
    if image.mode not in ("L", "RGB"):
        image = image.convert("RGB")
    if image.mode == "L":
        return True
    else:
        rgb = image.convert("RGB")
        for pixel in rgb.getdata():
            r, g, b = pixel
            if r != g or g != b:
                return False
        return True

for file in os.listdir(config["source"]):
    path = os.path.join(config["source"], file)
    if os.path.isfile(path) and any(file.lower().endswith(ext) for ext in config["supported_extensions"]):
        try:
            img = Image.open(path)
            if not is_bw(img):
                shutil.copy(path, os.path.join(config["destination"], file))
        except Exception as e:
            print(f"Error with {file}: {e}")