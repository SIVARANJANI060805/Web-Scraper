import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    # You can change this URL to any news site
    url = "https://www.bbc.com/news"

    # Step 1: Fetch the webpage
    response = requests.get(url)
    html_content = response.text

    # Step 2: Parse HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Step 3: Extract headlines (BBC uses <h2> tags a lot)
    headlines = []

    for h in soup.find_all("h2"):
        text = h.get_text(strip=True)
        if text:  # avoid empty text
            headlines.append(text)

    # Step 4: Save headlines to a .txt file
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for line in headlines:
            file.write(line + "\n")

    print("Scraping completed! Headlines saved to headlines.txt")


# Run the function
if __name__ == "__main__":
    scrape_headlines()
