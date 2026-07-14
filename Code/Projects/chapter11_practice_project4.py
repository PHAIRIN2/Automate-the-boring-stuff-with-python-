# Project: Link Verification.
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

start_url = sys.argv[1]

response = requests.get(start_url)
soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a", href=True)

print(f"All links found: {len(links)} links currently checking...")

broken_links = []

for link in links:
    href = link["href"]
    full_url = urljoin(start_url, href)
    if full_url.startswith("mailto:") or full_url.startswith("tel:"):
        continue
    try:
        r = requests.head(full_url, timeout=5, allow_redirects=True)
        if r.status_code == 404:
            broken_links.appand(full_url)
            print(f"[BROKEN 404] {full_url}")
    except requests.RequestException as e:
        print(f"[ERROR] {full_url}")

print("\n---summary---")
if broken_links:
    print(f"found broken link {len(broken_links)} link:")
    for link in broken_links:
        print(f" - {link}")
else:
    print("not found broken link")