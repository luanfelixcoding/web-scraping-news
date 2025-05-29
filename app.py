import requests
from bs4 import BeautifulSoup


def save_to_file(source: str, headlines: str) -> None:
    with open("tech_news.txt", "a", encoding="utf-8") as f:
        f.write(f"\n--- {source} ---\n")
        for idx, line in enumerate(headlines[:10], 1):
            f.write(f"{idx}. {line.text.strip()}\n")
            # title = headline.text.strip()
            # link = headline['href']
            # f.write(f"{idx}. {title}\n   Link: {link}\n")


def fetch_tech_news() -> None:
    """
    Fetches and displays the 10 latest tech news headlines from the TechCrunch homepage.

    Args:
        None

    Returns:
        None
    """
    url = "https://techcrunch.com"  # Base URL of the TechCrunch homepage
    response = requests.get(url)  # Perform an HTTP GET request
    # Parse the HTML response with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all <a> tags with class 'loop-card__title-link' inside article cards
    headlines = soup.find_all("a", class_="loop-card__title-link")

    print("\nLatest Tech News from TechCrunch:\n")

    # Print the first 10 unique headlines
    for idx, headline in enumerate(headlines[:10], 1):
        print(f"{idx}. {headline.text.strip()}")

    save_to_file("TechCrunch", headlines[:10])


def fetch_verge_news() -> None:
    """
    Fetches and displays the 10 latest tech news headlines from the TheVerge homepage.

    Args:
        None

    Returns:
        None
    """
    url = "https://theverge.com/tech"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("div", class_="_1xwtict9 _1pm20r55 _1pm20r52")

    print("\nLatest Tech News from The Verge:\n")

    # Print the first 10 unique headlines
    for idx, headline in enumerate(headlines[:10], 1):
        print(f"{idx}. {headline.text.strip()}")

    save_to_file("TheVerge", headlines[:10])


if __name__ == '__main__':
    fetch_tech_news()
    fetch_verge_news()
