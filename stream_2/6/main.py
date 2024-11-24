import requests
from bs4 import BeautifulSoup
import json


def scrape_bbc_sport():
    url = "https://www.bbc.com/sport"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error in the HTTP request: {e}")
        return

    soup = BeautifulSoup(response.text, 'lxml')

    # Search the articlec
    articles = soup.find_all('a', class_='ssrcss-vdnb7q-PromoLink', limit=5)
    data = []

    for article in articles:
        # Absolute link of the article
        link = article.get('href')
        if not link.startswith("https"):
            link = "https://www.bbc.com" + link

        # Search Related Topics
        metadata = article.find_next('ul', class_='ssrcss-1ik71mx-MetadataStripContainer')
        if metadata:
            topics = []
            for topic in metadata.find_all('span', class_='ssrcss-1if1g9v-MetadataText'):
                text = topic.text.strip()
                # time & IDs
                if (
                    "hour ago" not in text and
                    "hours ago" not in text and
                    "minute ago" not in text and
                    not text.isdigit()
                ):
                    topics.append(text)
        else:
            topics = []

        # Data_save
        data.append({
            "Link": link,
            "Topics": topics
        })

    # JSON_save
    with open('bbc_sport_topics.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"{len(data)} Articles have been saved in 'bbc_sport_topics.json' gespeichert.")


if __name__ == '__main__':
    scrape_bbc_sport()