"""Decode A Web Page(that was so rough. Spend really too much time on it, becouse indeed it wasnt all that difficult
had some problems with NYT, so change the site to python ecersises. Still need more practice with BS"""
from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.practicepython.org/")
r_html = r.content

soup = BeautifulSoup(r_html)
for something in soup.find_all("li"):
    if something.a:
        print(something.a.text)
    else:
        print(something)
