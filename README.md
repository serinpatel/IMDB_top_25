Here's a simple README template you can use for your GitHub repository:

---

# IMDB Top Movies Scraper

This repository contains a Python script that scrapes the IMDB website for the top movies of a given year, starting from a user-defined year until the current year. The script collects movie titles, release year, and IMDb ratings, and saves the data as JSON files for each year.

## Features

- Scrapes IMDB for movies released between a user-defined starting year and the current year.
- Collects movie title, release year, and IMDb rating.
- Saves the results as a JSON file for each year.
- Supports saving results for **25 movies per year**.

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/serinpatel/IMDB_top_25.git
cd IMDB_top_25
```

### 2. Install required libraries:

Before running the script, you need to install the required Python packages. You can do this by running the following:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes the following dependencies:
- `requests`
- `beautifulsoup4`
- `pandas`
- `tqdm`

### 3. Run the Script:

To run the script, use the following command:

```bash
python IMDB_Top25.py
```

### 4. User Input:

The script will prompt you to enter a starting year(eg.2022). The script will then scrape data for that year and continue scraping up to the current year.

## Output

For each year, a JSON file will be saved in the `DataSets/` directory with the top 25 movies and their IMDb ratings. The JSON file format will look like this:

```json
[
    {
        "Rank": 1,
        "Movie Title": "Movie Name",
        "Year": "2021",
        "IMDB Rating": "8.5"
    },
    ...
]
```

## Notes

- The script retrieves data directly from IMDB's search results, so the number of movies retrieved may vary depending on the IMDB website structure or content availability.
- This script is for educational and personal use. Please respect IMDB's terms of service.


Feel free to modify or add any additional details specific to your project!
