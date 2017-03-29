import requests
from BeautifulSoup import BeautifulSoup

url = https://bestfightodds.com/
response = requests.get(url, verify=False)
html = response.content

soup = BeautifulSoup(html)

print soup.prettify()
