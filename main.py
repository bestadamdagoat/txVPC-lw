from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen as ureq
import time

queryfile = open('query.txt')

while True:
    query = queryfile.readline()
    if not query:
        quit(print("end of file"))
    page = Soup(ureq('https://www.myplates.com/api/licenseplates/passenger/classic-black-silver/' + query).read(), "html.parser").get_text()
    if "incapsula" in page:
        quit(print("incapsula"))
    else:
        if '"available' in page:
            print(query)
    time.sleep(1)
