from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO

search = raw_input("search for images: ")
params = {"q": search}
r = requests.get("http://wwww.bing.com/images/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
links = soup.findAll("a", {"class": "thumb"})

for items in links:
    img_obj = requests.get(items.attrs["href"])
    print "Getting: ", items.attrs["href"]
    title = items.attrs["href"].split("/")[-1]

    try:
        img = Image.open(BytesIO(img_obj.content))
        img.save("./scrapped_images/", img.format)
    except IOError:
        print IOError
