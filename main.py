from urllib.request import urlopen as ureq
import time

queryfile = open('query.txt')

while True:
    query = queryfile.readline()
    if not query:
        quit(print("end of file"))
    page = ureq('https://www.myplates.com/api/licenseplates/passenger/classic-black-silver/' + query).read()
    if b"incapsula" in page:
        quit(print("incapsula"))
    elif b'"available' in page:
        print(query)
    time.sleep(1)
