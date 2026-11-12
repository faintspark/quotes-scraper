import requests
import json
import os
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

print(f"Status code: {response.status_code}")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    print(f"Page title: {soup.title.text}")
    quotes = soup.find_all("div", class_="quote")

    print(f"\nFound {len(quotes)} quotes on the page.")

    scraped_data = []

    for quote in quotes:

        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text

        quote_dict = {
            "quote": text,
            "author": author
        }

        scraped_data.append(quote_dict)



        print(f"Quote: {text}")
        print(f"Author: {author}")
        print("-" * 20)

    file_path = os.path.join(os.path.dirname(__file__), "quotes.json")
            
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(scraped_data, f, indent=2, ensure_ascii=False)

    print("Data successfully saved to quotes.json!")
else:
    print("Still blocked.")