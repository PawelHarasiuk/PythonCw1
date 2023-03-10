import requests

dates = ['20070501', '20150219', '20210701']
responds = []

for d in dates:
    url ="http://archive.org/wayback/available?url=onet.pl&timestamp="+d
    response = requests.get(url)
    responds.append(response.json())
for e in responds:
    print(e)
    print()


