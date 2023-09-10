from modules.url_list_manager.manager import URLListManager



# List of URLs to add
URLS = [
    "https://www.theinformation.com/",
    "https://techcrunch.com/category/artificial-intelligence/",
    "https://www.wired.com/tag/artificial-intelligence/",
    "https://news.mit.edu/topic/artificial-intelligence2",
    "https://www.artificialintelligence-news.com/",
    "https://www.technologyreview.com/topic/artificial-intelligence",
    "https://www.nytimes.com/spotlight/artificial-intelligence",
    "https://magazine.sebastianraschka.com/?utm_source=homepage_recommendations&utm_campaign=1084089",
    "https://www.latent.space/",
    "https://lastweekin.ai/",
    "https://www.startuphub.ai/"
]

# Initialize the URL List Manager with the URLs
manager = URLListManager(URLS)

# Save the URLs to a file
manager.save_urls_to_file()

print("URLs added and saved to initial_urls.txt!")
