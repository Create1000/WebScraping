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

    # Find articles
    articles = soup.find_all('a', class_='ssrcss-vdnb7q-PromoLink', limit=5)

    if not articles:
        print("No articles found. Please check the class name or HTML structure.")
        return

    data = []

    for article in articles:
        # Get the link
        link = article.get('href')
        if not link:
            print("Article link not found.")
            continue

        # Manually ensure the link
        if link.startswith('/'):
            link = "https://www.bbc.com" + link

        # contains 'undefined' or is malformed
        if 'undefined' in link or not link.startswith('https://'):
            print(f"Skipping invalid article URL: {link}")
            continue

        print(f"Processing article: {link}")

        # Fetch the article page to get related topics
        try:
            article_response = requests.get(link, headers=headers)
            article_response.raise_for_status()
            article_soup = BeautifulSoup(article_response.text, 'lxml')

            # Locate the Related Topics section
            related_topics_section = article_soup.find('div', class_='ssrcss-113c0cq-StyledTagContainer')
            topics = []

            if related_topics_section:
                topic_links = related_topics_section.find_all('a', class_='ssrcss-1ef12hb-StyledLink')
                for topic in topic_links:
                    topics.append(topic.text.strip())
            else:
                print(f"No related topics found for article: {link}")

            # Add_data
            data.append({
                "Link": link,
                "Topics": topics
            })
        except Exception as e:
            print(f"Error while processing article {link}: {e}")
            data.append({
                "Link": link,
                "Topics": []
            })

    # Save data_JSON
    with open('bbc_sport_topics.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"{len(data)} Articles have been saved in 'bbc_sport_topics.json'.")


if __name__ == '__main__':
    scrape_bbc_sport()