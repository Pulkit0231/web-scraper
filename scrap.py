import requests
from bs4 import BeautifulSoup
import pandas as pd


base_url = "https://www.businesswire.com/portal/site/home/news/industry/?vnsId=31249&page="
keywords_to_search = ['Energy', 'Electric Vehicle']
headlines = []
dates = []
hrefs = []

for page_num in range(1, 51):  
    url = base_url + str(page_num)
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve page {page_num}")
        continue

    soup = BeautifulSoup(response.content, "html.parser")
    news_items = soup.find_all("li")

    for item in news_items:
        headline_tag = item.find("span", itemprop="headline")
        href_tag = item.find("a", class_="bwTitleLink")
        date_tag = item.find("time", itemprop="dateModified")
        
        if headline_tag and href_tag and date_tag:
            headline = headline_tag.get_text(strip=True)
            href = href_tag["href"]
            full_href = "https://www.businesswire.com" + href
            date = date_tag.get_text(strip=True)
            
            if any(keyword.lower() in headline.lower() for keyword in keywords_to_search):
                headlines.append(headline)
                dates.append(date)
                hrefs.append(full_href)
    
    print(f"Page {page_num} scraped successfully.")

df = pd.DataFrame({
    "Headline": headlines,
    "Date": dates,
    "Link": hrefs
})

df.to_csv("businesswire_news_filtered.csv", index=False)

print("Scraping complete. Filtered data saved to 'businesswire_news_filtered.csv'.")
