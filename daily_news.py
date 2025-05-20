import schedule
import time
from app import fetch_verge_news, fetch_tech_news

# Schedule the fetch_tech_news function to run daily at 15:30
schedule.every().day.at("15:30").do(fetch_tech_news)

# Schedule the fetch_verge_news function to run daily at 15:30
schedule.every().day.at("15:30").do(fetch_verge_news)

# Infinite loop to keep the scheduler running continuously
while True:
    schedule.run_pending()  # Run any scheduled tasks that are due
    time.sleep(60)          # Wait 60 seconds before checking again
