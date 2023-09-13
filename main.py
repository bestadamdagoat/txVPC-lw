from urllib.request import urlopen as ureq

queryfile = open('query.txt')

while True:
    query = queryfile.readline()
    page = ureq('https://www.myplates.com/api/licenseplates/passenger/classic-black-silver/' + query).read()
    if '"available' in page:
        print(query)
