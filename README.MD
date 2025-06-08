# Copy Images by Type

This Python script copies images from a source folder to a destination folder based on their type: **black and white** (BW) or **colour**. It supports common image formats such as `.jpg`, `.jpeg`, and `.png`.






# Features

- Automatically detects colour vs black and white images
- Supports JPG, JPEG, and PNG formats
- Preserves original files (copies rather than moves)

## Requirements

- Python 3.6 or higher
- [Pillow](https://python-pillow.org/) (for image processing)
- tqdm (for progress bar)

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

### Copy black and white images

Windows:
  ```python
  python images_sorter.py --source "C:\Users\YourName\Pictures" --destination "D:\SortedPhotos" --type bw
  ```
Linux/Mac:
  ```python
  python images_sorter.py --source "/home/yourname/Pictures" --destination "/home/yourname/SortedPhotos" --type bw
  ```

### Copy colour images

Windows:
  ```python
  python images_sorter.py --source "C:\Users\YourName\Pictures" --destination "D:\SortedPhotos" --type colour
  ```


Linux/Mac:
  ```python
  python images_sorter.py --source "/home/yourname/Pictures" --destination "/home/yourname/SortedPhotos" --type colour
  ```

You can also use relative paths if the script is in the same directory as your source and destination folders :
  ```python
  python images_sorter.py --source "./source_folder" --destination "./destination_folder" --type bw
  ```

## License
This script is open source and free to use for personal or commercial purposes.



