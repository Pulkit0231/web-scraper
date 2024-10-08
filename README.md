# BusinessWire News Scraper


## Features

- Scrapes news headlines, publication dates, and URLs from BusinessWire.
- Filters the news based on specified keywords.
- Extracts data from multiple pages (configurable for 50 pages).
- Outputs the filtered results to a CSV file.

## Requirements
- Python 3.x
- requests library
- beautifulsoup4 library
- pandas library


You can install the required libraries using the following command:
```bash
pip install requests beautifulsoup4 pandas
```

## How to Use

1. Clone the repository:
```bash
git clone https://github.com/yourusername/businesswire-news-scraper.git
cd businesswire-news-scraper

```

2. Run the script:
```bash
python scraper.py

```

3. Modify the list of keywords you want to search for in the script:
```bash
keywords_to_search = ['Energy', 'Electric Vehicle']

```
The script will:

- Scrape headlines, dates, and links from BusinessWire's industry news pages.
- Filter the news items based on your keywords (case-insensitive).
- Save the results into a CSV file named businesswire_news_filtered.csv.

## Code Overview
- base_url: The base URL of BusinessWire's industry news section, with pagination support.
- keywords_to_search: A list of keywords used to filter the news headlines.
- Pagination: The script loops through multiple pages (1-50), allowing you to scrape a larger dataset.
- Filtering: The script filters headlines that contain any of the keywords in keywords_to_search.
