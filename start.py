import requests as req
import arrow
from bs4 import BeautifulSoup as bs

source = req.get("https://itc.ua")
soup = bs(source.text, "lxml")

sites = [tag.get("href") for tag in soup.main.find_all("a", rel="bookmark")]

def getnws(site):
    s = req.get(site)
    body = bs(s.text, "lxml")
    title = body.find("div", class_="h1 text-uppercase entry-title").text
    time = arrow.get(body.find("time", class_="published").get("datetime"))
    new = body.find("div", class_="post-txt").text
    return title, time, new

for site in sites:
    title, time, new = getnws(site)
    print("{} \n{} \n{}".format(title, time, new))