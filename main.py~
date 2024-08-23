from bs4 import BeautifulSoup
import requests
import validators
import sys
import os

url = sys.argv[1]

DOWNLOAD_FOLDER = os.path.join(ps.getcwd(), 'Downloads')
os.makedirs(DOWNLOAD_FOLDER, exist_ok = True)

def validate_url(url):
    if not validators.url(url):
        print('Invalid url')
        return False
    return True

def getSoup(url):
    if validate_url(url):
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
    try:
        img_tags = soup.find_all('img')
    except Exception as e:
        print(e)
    else:
        for img in img_tags:
            yield img.get('src')

def downloadImage(image_url, index):
    if not image_url.startswith(('http://', 'https://')):
        image_url = requests.compat.urljoin(url, image_url)

    img_response = requests.get(image_url)
    
    if img_response.status_code == 200:
        img_name = f'image-{index}.jpg'
        
        with open(os.path.join('Downloads', img_name), 'wb') as file:
            file.write(img_response.content)
        print(f'{img_name} successfully downloaded')
    else:
        print(f'{image_url} cant be downloaded')

if __name__ == '__main__':
    soup = getSoup(url)
    if soup:
        index = 0
        for image in getImages(soup):
            index += 1
            downloadImage(image, index)



            

