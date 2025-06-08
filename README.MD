# Image Sorter

A simple Python script to sort images into colour and black & white categories. This script scans a specified directory for image files and copies them into separate folders based on their colour type.

# User case

A folder with a mix of colour and black & white images, and you want to organize them into two separate folders for better organization.

# Features

- Automatically detects colour vs black and white images
- Supports JPG, JPEG, and PNG formats
- Preserves original files (copies rather than moves)

## Requirements

- Python 3.6 or higher
- Pillow library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/image-sorter.git
   cd image-sorter
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Edit the configuration in both scripts:
   - Set the `source` path to the directory containing your images
   - Set the `destination` path to the directory where you want the sorted images to be stored.

2. To copy colour images from the source folder to the destination folder, run:
   ```
   python copy_colour_pictures.py
   ```
3. To copy black and white images from the source folder to the destination folder, run:
   ```
   python copy_bw_pictures.py
   ```
