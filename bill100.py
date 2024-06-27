import requests
from bs4 import BeautifulSoup
import csv

# URL for the Billboard Hot 100 chart page
url = "https://www.billboard.com/charts/hot-100/"

# Request the page with SSL verification turned off
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.content, "html.parser")

# Function to get the top 100 songs from Billboard Hot 100
def get_billboard_hot_100(soup):
    # Extract song titles and artists
    hot_100 = []
    chart_list = soup.find_all("li", class_="o-chart-results-list__item")
    for item in chart_list:
        title = item.find("h3", id="title-of-a-story")
        artist = item.find("span", class_="c-label")
        if title and artist:
            hot_100.append({"title": title.get_text(strip=True), "artist": artist.get_text(strip=True)})
    return hot_100

# Get the Billboard Hot 100 list
hot_100_list = get_billboard_hot_100(soup)

# Specify the file name
file_name = "billboard_hot_100.csv"

# Write the data to a CSV file
with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Rank", "Title", "Artist"])
    for i, song in enumerate(hot_100_list, start=1):
        writer.writerow([i, song['title'], song['artist']])

print(f"Billboard Hot 100 list has been written to {file_name}")
