Government Tender Tracker & Bid-Match Recommender
Overview
This project is a web-based application built using Streamlit that allows companies to track government tenders across various portals, automatically match tenders with the company's capabilities, and receive notifications for high-match tenders. The application aggregates tender data from multiple e-procurement portals and matches the tender details with the company's profile.

Features
Tender Aggregation: Scrapes tenders from multiple government portals like CPPP (Central Public Procurement Portal) and GeM (Government e-Marketplace).

Company Profile Matching: Allows companies to upload their capability profiles and matches them with scraped tenders using Natural Language Processing (NLP).

Notification System: Sends email alerts for high-match tenders.

Streamlit Dashboard: Provides a user-friendly interface to visualize scraped tenders and profile match results.

Technologies Used
Streamlit: For creating the interactive web interface.

Requests and BeautifulSoup: For scraping tenders from e-procurement portals.

scikit-learn: For NLP-based matching of tenders and company profiles using TF-IDF and cosine similarity.

SMTP (Gmail): For sending email notifications for high-match tenders.

Project Structure

tender_bid_matcher/
├── app.py                      # Main Streamlit application
├── scraper/
│   ├── gem_scraper.py          # Scraping logic for GeM portal
│   └── cppp_scraper.py         # Scraping logic for CPPP portal
├── matching/
│   └── profile_matcher.py      # Matching logic for company profiles and tenders
├── notifications/
│   ├── email_notifier.py       # Email notification logic
├── data/
│   └── tenders.csv             # (Optional) Saved tenders data in CSV
├── sample_profile.txt          # Example company profile (for testing)
└── requirements.txt            # Python dependencies
Installation
Prerequisites
Make sure you have Python installed on your machine. If not, you can download it from python.org.

Steps to Set Up
Clone this repository:

git clone https://github.com/your-username/tender-bid-match-recommender.git
cd tender-bid-match-recommender
Install dependencies: Create a virtual environment (optional but recommended):
Install the required libraries:

pip install -r requirements.txt
Update your sample_profile.txt with your company details (see the "Sample Profile" section below).

Configure Gmail for sending email notifications:

Go to Google App Passwords and create an app password for Gmail.

Replace the placeholder in email_notifier.py with your Gmail app password.

Run the application:
streamlit run app.py
Open your browser and go to http://localhost:8501 to view the app.

Features in Detail
1. Scrape Tenders:
Click the "Scrape Tenders Now" button to scrape tenders from the GeM and CPPP portals. The tenders will be displayed in the app.

2. Upload Company Profile:
Upload a .txt file containing your company’s profile. The app will extract the text and use it to match with scraped tenders.

3. Profile Matching:
The uploaded company profile is compared with the tender titles using TF-IDF vectorization and cosine similarity to calculate a match score for each tender.

4. Notifications:
Enter your phone number (for SMS) and email address to receive notifications for high-match tenders (match score > 85%).

5. Streamlit Dashboard:
The results are displayed in an interactive dashboard. You can search for specific tenders, view match scores, and manage your profile.

Sample Profile
Here is an example of the content you can use for testing:

Company Name: BuildTech Solutions Pvt Ltd

Core Competencies:
- Civil Construction (School Buildings, Hospitals, Office Complexes)
- Interior Fit-Outs (Furniture Supply and Installation)
- Office Supplies (Stationery and Office Equipment)
- IT Hardware Procurement (Desktops, Laptops, Servers)

Previous Projects:
- Construction of Government Schools in Tamil Nadu (2022)
- Supply of Office Furniture to Karnataka State Offices (2023)
- Procurement of IT Equipment for Education Boards in Maharashtra (2024)

Financial Capacity:
- Annual Turnover: 25 Crores INR
- EMD Capacity: Up to 20 Lakhs INR

Certifications:
- ISO 9001:2015 (Quality Management Systems)
- MSME Registered Vendor

Contact Information:
- Email: tenders@buildtechsolutions.in
- Phone: +91-9876543210
Example Tender Data (Scraped from GeM and CPPP)

Title	Deadline	Match Score
Construction of School Building in Tamil Nadu	2025-05-20	92%
Supply of Office Stationery for Delhi Secretariat	2025-05-15	85%
Procurement of IT Equipment for Government Offices	2025-05-25	88%
Office Furniture Supply for New Office Building	2025-05-18	90%
Notes
Matching Accuracy: The matching of tenders to profiles is done using the TF-IDF (Term Frequency-Inverse Document Frequency) algorithm along with cosine similarity for scoring.

Notifications: Email notifications are sent for tenders with a match score greater than 85%. SMS notifications can also be enabled (if you configure Twilio).

Data Scraping: As scraping depends on external portals, be sure that these portals provide the data in a structured format. If there are any changes to their websites, the scraper may require modifications.

Future Enhancements
Scrape data from more e-procurement portals (state portals, etc.).

Add more advanced profile matching algorithms (e.g., word embeddings like Word2Vec or BERT).

Implement a front-end with login features for user management.
