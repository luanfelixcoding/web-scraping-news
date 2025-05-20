import requests
from bs4 import BeautifulSoup


def fetch_tech_news() -> None:
    url = "https://techcrunch.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("a", class_="loop-card__title-link")
    print("\nLatest Tech News from TechCrunch:\n")
    for idx, headline in enumerate(headlines[:10], 1):
        print(f"{idx}. {headline.text.strip()}")


if __name__ == '__main__':
    fetch_tech_news()
