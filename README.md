In this project, we have used beautiful soup-a python framework <br>to obtain obtain useful information that are inside HTML elements like div etc

import bs4
from bs4 import BeautifulSoup

from requests import get

#getting html from a website

url="https://viewincode.co.ke"

reply=get(url)

html=reply.text
