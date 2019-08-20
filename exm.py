from bs4 import BeautifulSoup
import requests
import os
import urllib

search = raw_input("search for images: ")
params = {"q": search}
r = requests.get("http://wwww.bing.com/images/search", params=params)
dir_name = search.replace(" ", "_").lower()

if not os.path.isdir(dir_name):
    os.makedirs(dir_name)

soup = BeautifulSoup(r.text, "html.parser")
links = soup.findAll("a", {"class": "thumb"})

for items in links:
    img_obj = requests.get(items.attrs["href"])
    print "Getting: ", items.attrs["href"]
    title = items.attrs["href"].split("/")[-1]
    urllib.urlretrieve(items.attrs["href"], os.path.join("./scrapped_images/", title))
