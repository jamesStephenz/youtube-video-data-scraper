thonimport requests
from bs4 import BeautifulSoup

def scrape_video_data(url):
    """Scrape YouTube video data."""
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch video page: {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract video details
    title = soup.find('h1', {'class': 'title'}).text.strip()
    views_count = soup.find('div', {'class': 'view-count'}).text.strip()
    likes_count = soup.find('button', {'title': 'I like this'}).text.strip()
    comments_count = soup.find('h2', {'id': 'comments'}).text.strip()
    description = soup.find('meta', {'name': 'description'})['content']
    
    # Extract channel details
    channel_name = soup.find('a', {'class': 'yt-simple-endpoint'}).text.strip()
    channel_id = soup.find('a', {'class': 'yt-simple-endpoint'}).get('href')
    
    return {
        "url": url,
        "title": title,
        "views_count": views_count,
        "likes_count": likes_count,
        "comments_count": comments_count,
        "description": description,
        "channel_name": channel_name,
        "channel_id": channel_id
    }