# football_stats.py
# This script scrapes NFL player stats for touchdowns from CBS Sports website

# Step 1: Import required libraries
import requests  # Helps us fetch the webpage
from bs4 import BeautifulSoup  # Helps us extract data from the webpage


# Step 2: Function to scrape football stats
def scrape_football_stats():
    # URL to fetch player stats
    url = "https://www.cbssports.com/nfl/stats/player/regular/touchdowns"

    # Get the webpage content
    response = requests.get(url)

    # Check if the webpage was fetched successfully
    if response.status_code == 200:  # 200 means "OK"
        # Parse the webpage content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Look for the table with stats
        stats_table = soup.find("table", class_="data-table")  # Find the table with stats
        rows = stats_table.find_all("tr")  # Get all rows in the table

        print("Top 20 NFL Players by Touchdowns")
        print(f"{'Player':<20} {'Position':<10} {'Team':<10} {'Touchdowns':<10}")
        print("-" * 50)

        # Loop through the top 20 rows (skip the header row)
        for row in rows[1:21]:  # Start at row 1 to skip the header
            columns = row.find_all("td")  # Get all columns in the row
            player = columns[0].text.strip()  # Extract player name
            position = columns[1].text.strip()  # Extract player position
            team = columns[2].text.strip()  # Extract player team
            touchdowns = columns[3].text.strip()  # Extract number of touchdowns

            # Print the stats neatly
            print(f"{player:<20} {position:<10} {team:<10} {touchdowns:<10}")
    else:
        print("Failed to load the webpage. Please check the URL or your internet connection.")


# Step 3: Run the function
if __name__ == "__main__":
    scrape_football_stats()
