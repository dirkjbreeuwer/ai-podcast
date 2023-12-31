import os
import json
from dotenv import load_dotenv
from modules.content_crawler.crawler import ContentCrawler
from modules.url_list_manager.manager import URLListManager


def save_articles_to_file(articles, filename="data/raw/articles.json"):
    """Append articles to a JSON file."""
    
    # Check if the file already exists
    if os.path.exists(filename):
        # If it exists, load the current content
        with open(filename, 'r') as file:
            existing_articles = json.load(file)
    else:
        # If it doesn't exist, initialize an empty list
        existing_articles = []

    # Append the new articles to the existing ones
    existing_articles.extend(articles)

    # Write the combined articles back to the file
    with open(filename, 'w') as file:
        json.dump(existing_articles, file, indent=4)

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Retrieve API key from environment variables
    API_KEY = os.getenv("APIFY_API_KEY")

    # Initialize the URLListManager
    url_manager = URLListManager('data/raw/initial_urls.txt')  # Assuming this is the path where the URLs are stored
    urls = url_manager.load_urls_from_file()

    # Initialize and run the ContentCrawler
    crawler = ContentCrawler(API_KEY)
    articles = crawler.extract_articles(urls)

    # Save articles to a file
    save_articles_to_file(articles)

    print(f"Successfully crawled and saved {len(articles)} articles.")

if __name__ == "__main__":
    main()
