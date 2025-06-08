# Copy Images by Type

This Python script copies images from a source folder to a destination folder based on their type: **black and white** (BW) or **colour**. It supports common image formats such as `.jpg`, `.jpeg`, and `.png`.






# Features

- Automatically detects colour vs black and white images
- Supports JPG, JPEG, and PNG formats
- Preserves original files (copies rather than moves)

## Requirements

- Python 3.6 or higher
- [Pillow](https://python-pillow.org/) (for image processing)

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

Run the script with the appropriate arguments:
  ```python
  python images_sorter.py --source <source_folder> --destination <destination_folder> --type <bw|colour>
```

## Use Case

Imagine you have a folder with hundreds of photos, where each image has both a **colour version** and a **black and white version**, all mixed together in the same directory. Manually sorting them would be time-consuming and error-prone.

With this script, you can automatically separate the two types into different folders

## Examples

Copy black and white images:
  ```python
  python images_sorter.py --source ./images --destination ./sorted_images --type bw
  ```

Copy colour images:
  ```python
  python images_sorter.py --source ./images --destination ./sorted_images --type colour
  ```

## License
This script is open source and free to use for personal or commercial purposes.