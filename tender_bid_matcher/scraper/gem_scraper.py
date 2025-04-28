# scraper/gem_scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_gem():
    url = "https://bidplus.gem.gov.in/all-bids"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch GeM bids page. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    tenders = []

    try:
        cards = soup.find_all('div', class_='bid')
        for card in cards:
            title_tag = card.find('span', class_='bid-title')
            deadline_tag = card.find('span', class_='bid-closing-date')

            title = title_tag.text.strip() if title_tag else 'No Title'
            deadline = deadline_tag.text.strip() if deadline_tag else 'No Deadline'

            tenders.append({'Title': title, 'Deadline': deadline})

    except Exception as e:
        print(f"Error while parsing GeM bids page: {e}")

    return tenders
