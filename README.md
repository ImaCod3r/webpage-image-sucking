
# Webpage image downloader

This Python script allows you to download all images from a specified webpage. It parses the webpage's HTML, extracts the image URLs, and saves the images to a local directory.

## Features

- Fetch images from any webpage.
- Save images to a custom or default download directory.
- Error handling for HTTP request issues (timeouts, request errors).

## Prerequisites

Make sure you have Python installed, along with the following libraries:

- `argparse`
- `requests`
- `beautifulsoup4`

You can install the required libraries by running:
```bash
pip install -r requirements.txt
```

## Usage

To use the script, simply run the following command in your terminal:
```bash
python main.py <URL> [-d <DIRECTORY>]
```

### Arguments

- `<URL>`: The webpage URL from which to download the images.
- `-d <DIRECTORY>`: (Optional) The directory to save the downloaded images. If not specified, the default is Downloads.

### Example
```bash
python main.py https://example.com -d my_images
```

This will download all images from https://example.com and save them to the my_images folder.

## Error Handling
- The script will handle request timeouts and print a corresponding message.
- If an HTTP error occurs, the script will output the error details.


## Directory Structure
```bash
|-- main.py
|-- Downloads/
    |-- (Images saved here)
```


## License

This project is licensed under the MIT License.
[MIT](https://choosealicense.com/licenses/mit/)
