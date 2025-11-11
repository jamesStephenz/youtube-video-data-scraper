thonfrom scraper import scrape_video_data

def parse_video_info(url):
    """Parse the YouTube video and return the detailed data."""
    video_data = scrape_video_data(url)
    return video_data