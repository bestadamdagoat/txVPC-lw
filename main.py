from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen as ureq

queryfile = open('query.txt')

while True:
    query = queryfile.readline()
    page = Soup(ureq('https://www.myplates.com/api/licenseplates/passenger/classic-black-silver/' + query).read(), "html.parser").get_text()
    if '"available' in page:
        print(query)
