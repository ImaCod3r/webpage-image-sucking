import argparse
import os
from bs4 import BeautifulSoup
import requests

DOWNLOAD_FOLDER = 'Downloads'
os.makedirs(DOWNLOAD_FOLDER, exist_ok = True)

def parse_args():
    parser = argparse.ArgumentParser(description="Download images from a webpage")
    parser.add_argument("url", help="Webpage URL")
    parser.add_argument("-d", "--directory", default="Downloads", help="Directory to save images")
    return parser.parse_args()

def getSoup(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # raise exception for http error code
    except requests.exceptions.Timeout:
        print('The request timed out')
        return False
    except requets.exceptions.RequestException as e:
        print(f'An error occured: {e}')
        return False
    else:
        if response.status_code == 200:
            return BeautifulSoup(response.text, 'html.parser')

def getImages(soup):
    return [img.get('src') for img in soup.find_all('img')]

def downloadImage(base_url, image_url, directory, index):
    if not image_url.startswith(('http://', 'https://')):
        image_url = requests.compat.urljoin(base_url, image_url)

    img_response = requests.get(image_url)
    
    if img_response.status_code == 200:
        extension = os.path.splitext(image_url)[1] # Get the file extension
        if not extension:
            extension = '.jpg' # If there is no extension, assume it as JPG
        
        img_name = f'image-{index}{extension}'
        img_path = os.path.join(directory, img_name)
        
        with open(img_path, 'wb') as file:
            file.write(img_response.content)
        print(f'{img_name} successfully downloaded')
    else:
        print(f'{image_url} cant be downloaded')

def main():
    args = parse_args()
    soup = getSoup(args.url)
    if soup:
        images = getImages(soup)
        index = 1
        for image in images:
            downloadImage(args.url, image, args.directory, index)
            index += 1

if __name__ == '__main__':
    main()
