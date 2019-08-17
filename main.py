from bs4 import BeautifulSoup
import requests

search = input("type the thing you want to search")
par = {"q": search}
r = requests.get("https://www.bing.com/search", params=par)

soup = BeautifulSoup(r.text)
print(soup.prettify())