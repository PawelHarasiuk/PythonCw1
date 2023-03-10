import webbrowser
import requests

pageurl = input("Podaj adres strony: ")
date = input("Podaj date: ")
url = 'http://archive.org/wayback/available?url=' + pageurl + '&timestamp=' + date

response = requests.get(url)
d = response.json()
page = d['archived_snapshots']['closest']['url']

webbrowser.open(page)
pageurl = input("\nPodaj adres strony: ")
date = input("Podaj date: ")
url = 'http://archive.org/wayback/available?url=' + pageurl + '&timestamp=' + date

response = requests.get(url)
d = response.json()
page = d['archived_snapshots']['closest']['url']

webbrowser.open(page)
pageurl = input("\nPodaj adres strony: ")
date = input("Podaj date: ")
url = 'http://archive.org/wayback/available?url=' + pageurl + '&timestamp=' + date

response = requests.get(url)
d = response.json()
page = d['archived_snapshots']['closest']['url']

webbrowser.open(page)