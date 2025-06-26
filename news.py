import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"

def get_headlines(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = set()

    # <h3> tags with class
    for h in soup.find_all("h3", class_="gs-c-promo-heading__title"):
        text = h.get_text(strip=True)
        if text:
            headlines.add(text)

    # <h2> tags
    for h in soup.find_all("h2"):
        text = h.get_text(strip=True)
        if text:
            headlines.add(text)

    # <title> tag
    title = soup.title
    if title:
        text = title.get_text(strip=True)
        if text:
            headlines.add(text)

    return list(headlines)

def save_headlines(headlines, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for i, headline in enumerate(headlines, 1):
            f.write(f"{i}. {headline}\n")

if __name__ == "__main__":
    headlines = get_headlines(URL)
    save_headlines(headlines, "headlines.txt")
    print(f"Saved {len(headlines)} headlines to headlines.txt")