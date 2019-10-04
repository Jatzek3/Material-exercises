"""Decode A Web Page(that was so rough. Spend really too much time on it, becouse indeed it wasnt all that difficult
had some problems with NYT, so change the site to python ecersises. Still need more practice with BS"""
from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.practicepython.org/")
r_html = r.content


string_with_txt = ""
soup = BeautifulSoup(r_html)
for something in soup.find_all("li"):
    if something.a:
        print(something.a.text)
        string_with_txt += something.a.text +"\n"
    else:
        print(something)

with open("headlines.txt", "w") as open_file:
    open_file.write(string_with_txt)
