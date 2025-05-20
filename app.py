import requests
from bs4 import BeautifulSoup


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


if __name__ == '__main__':
    fetch_tech_news()
