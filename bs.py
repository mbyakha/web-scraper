import bs4
from bs4 import BeautifulSoup

from requests import get

#getting html from a website

url="https://viewincode.co.ke"

reply=get(url)

html=reply.text


soup=BeautifulSoup(html, features='html.parser')


#finding text in html <b> tags:
a=soup.find_all('b')
for tag in a:
    text=tag.text
    #print(text)

#finding links in html text:
links=soup.find_all("a")

for link in links:
    l=link.get('href')
    print(l)
