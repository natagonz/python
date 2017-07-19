import requests

from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"

r = requests.get(url)

soup = BeautifulSoup(r.content)

titles = soup.find_all("h2")

for title in titles :
	print "<p>Judul : %s </p>"%(title.text)