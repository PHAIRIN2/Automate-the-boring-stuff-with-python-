# Project: "I'm feeling lucky" Google Search

import webbrowser, requests, bs4, sys

print("Googling.....")
res = requests.get("http://google.com/search?q=" + " ".join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
Linkelem = soup.select("a")
numOpen = min(5, len(Linkelem))
for i in range(numOpen):
    webbrowser.open("http://google.com" + Linkelem[i].get("href"))
