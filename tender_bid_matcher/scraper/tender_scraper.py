# scraper/tender_scraper.py

import pandas as pd
from scraper.cppp_scraper import scrape_cppp
from scraper.gem_scraper import scrape_gem

def scrape_tenders():
    # Scrape from different portals
    cppp_tenders = scrape_cppp()
    gem_tenders = scrape_gem()

    # Combine all tenders
    all_tenders = cppp_tenders + gem_tenders

    if all_tenders:
        # Create a DataFrame
        tenders_df = pd.DataFrame(all_tenders)

        # Save to CSV for records
        tenders_df.to_csv('data/tenders.csv', index=False)

        return tenders_df
    else:
        print("No tenders found during scraping.")
        return pd.DataFrame()  # Return empty DataFrame if no data
