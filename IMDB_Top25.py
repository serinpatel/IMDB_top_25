import os
import datetime
import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm

# Set up data storage
dataset_location = os.path.join(os.getcwd(), "DataSets")
if not os.path.exists(dataset_location):
    os.makedirs(dataset_location)

# Define headers to avoid being blocked
headers = {'User-agent': 'Mozilla/5.0'}

# Get user input for the starting year
current_year = datetime.datetime.now().year
input_year = int(input("Please enter start year (e.g., 2016): "))


if input_year > current_year:
    print(f"No movie is recorded in year {input_year} yet!!")
else:
    for year in tqdm(range(input_year, current_year + 1)):
        url = f"https://www.imdb.com/search/title?release_date={year},{year}&title_type=feature"
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            print(f"Failed to fetch data for {year}: HTTP {response.status_code}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        movie_data = []
        lister_list = soup.find_all('li', class_='ipc-metadata-list-summary-item')
        
        for i, movie in enumerate(lister_list, start=1): 

            movie_title_text = movie.find('h3', class_="ipc-title__text")
            movie_title = movie_title_text.get_text(strip=True) if movie_title_text else "N/A"
            movie_title = movie_title.split('. ', 1)[-1]

            year_text = movie.find('span', class_='sc-d5ea4b9d-7 URyjV dli-title-metadata-item')
            movie_year = year_text.get_text(strip=True) if year_text else "N/A"

            rating_tag = movie.find('span', class_='ipc-rating-star--rating')
            imdb_rating = rating_tag.get_text(strip=True) if rating_tag else "N/A"

            movie_data.append([i, movie_title, movie_year, imdb_rating])


        # Convert to DataFrame
        df = pd.DataFrame(movie_data, columns=["Rank", "Movie Title", "Year", "IMDB Rating"])

        # File path for saving results
        file_path = os.path.join(dataset_location, f"IMDB_Top25_{year}.json")
        
        # Save to Excel
        df.to_json(file_path,  orient="records", indent=4)
        print(f"Saved IMDB Top 25 movies for {year} in {file_path}")

            




