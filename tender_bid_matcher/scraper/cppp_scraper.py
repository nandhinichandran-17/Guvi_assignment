# scraper/cppp_scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_cppp():
    url = "https://etenders.gov.in/eprocure/app"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to fetch CPPP page. Status code: {response.status_code}")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # As an example, let's scrape tenders from the "Latest Active Tenders" section
    tenders = []

    try:
        table = soup.find('table', {'class': 'table'})  # Usually tenders are shown in tables
        if table:
            rows = table.find_all('tr')
            for row in rows[1:]:  # Skip the header
                cols = row.find_all('td')
                if len(cols) >= 2:
                    title = cols[0].text.strip()
                    deadline = cols[1].text.strip()
                    tenders.append({'Title': title, 'Deadline': deadline})
    except Exception as e:
        print(f"Error while parsing CPPP page: {e}")

    return tenders
