import requests
import os
import urllib.request
from bs4 import BeautifulSoup

Name = "Priyanka Chopra"


Name_list = Name.split()
file_number = 1
mypath = "E:\Python downloads\Images " + str(Name)

print(mypath)
if not os.path.exists(mypath):
    os.makedirs(mypath)
os.chdir(mypath)

def download_image(img_src):
    global file_number
    name = "Name"+str(file_number)+".jpg"
    file_number+=1
    urllib.request.urlretrieve(img_src,name)


def crawl(max_pages):
    page = 1
    while(page <= max_pages):
        url = "http://www.santabanta.com/wallpapers/"+Name_list[0].lower()+"-"+Name_list[1].lower()+"/?page="+str(page)
        source_code = requests.get(url)
        source_code = source_code.text
        soup = BeautifulSoup(source_code, 'html.parser')

        for link in soup.findAll('a',{'title':Name}):
            source = link.get("href")
            if(".htm" in source):
                source = "http://www.santabanta.com" + source
                crawl_image(source)
        page+=1


def crawl_image(wall_url):
    source_code = requests.get(wall_url)
    source_code = source_code.text
    soup = BeautifulSoup(source_code,'html.parser')

    for link in soup.findAll('img',{'id':'wall'}):
        image_src = link.get("src")
        download_image(image_src)

crawl(10)




