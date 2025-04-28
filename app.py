# app.py

import streamlit as st
import pandas as pd
from matching.profile_matcher import match_profile
from notifications.email_notifier import send_email_notification
from scraper.tender_scraper import scrape_tenders

# Title
st.title("🚀 Government Tender Tracker & Bid-Match Recommender")

# Initialize tenders_df
tenders_df = pd.DataFrame()

# Tender scraping button
if st.button("Scrape Tenders Now"):
    tenders_df = scrape_tenders()
    st.success("✅ Tenders scraped successfully!")

    st.subheader("Preview of Scraped Tenders:")
    st.write("Columns:", tenders_df.columns.tolist())
    st.dataframe(tenders_df)

# Upload company profile
uploaded_file = st.file_uploader("📄 Upload your company capability profile (.txt)", type=["txt"])

if uploaded_file:
    profile_text = uploaded_file.read().decode("utf-8")
    st.success("✅ Profile uploaded successfully!")

    if not tenders_df.empty:
        if 'Title' in tenders_df.columns:
            # Match profile to tenders
            match_scores = match_profile(profile_text, tenders_df['Title'])
            tenders_df['Match Score'] = match_scores

            # Show matched tenders
            st.subheader("🔍 Matched Tenders")
            st.dataframe(tenders_df[['Title', 'Match Score']])

            # Notifications option
            if st.checkbox("📬 Send Email notifications for high match tenders (>85%)"):
                email_address = st.text_input("Enter your Email Address:")

                if email_address:
                    for idx, tender in tenders_df.iterrows():
                        if tender['Match Score'] > 0.85:
                            email_subject = "High Match Tender Alert! 🚀"
                            email_body = f"Tender: {tender['Title']}\nMatch Score: {round(tender['Match Score']*100)}%"

                            send_email_notification(email_address, email_subject, email_body)

                    st.success("✅ Email notifications sent for high-match tenders!")

        else:
            st.error("❌ 'Title' column missing in scraped tenders. Please check your scraper.")
    else:
        st.error("❌ Please scrape tenders first by clicking 'Scrape Tenders Now'.")
