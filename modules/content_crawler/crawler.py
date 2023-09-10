# modules/content_crawler/crawler.py
import hashlib
from apify_client import ApifyClient

def generate_article_id(article_url):
    """Generate a unique ID for an article based on its URL."""
    return hashlib.md5(article_url.encode()).hexdigest()

class ContentCrawler:
    def __init__(self, api_key):
        self.client = ApifyClient(api_key)
        self.actor_id = "hy5TYiCBwQ9o8uRKG"  # This is the actor ID for the specific Apify actor

    def extract_articles(self, urls):
        # Prepare the Actor input
        run_input = {
            "startUrls": [{"url": url} for url in urls],
            # ... (rest of the configuration remains the same as provided)
            "onlyNewArticles": False,
            "onlyNewArticlesPerDomain": False,
            "onlyInsideArticles": True,
            "enqueueFromArticles": False,
            "crawlWholeSubdomain": False,
            "onlySubdomainArticles": False,
            "scanSitemaps": False,
            "saveSnapshots": False,
            "useGoogleBotHeaders": False,
            "onlyArticlesForLastDays": 7,
            "minWords": 150,
            "mustHaveDate": True,
            "isUrlArticleDefinition": {
                "minDashes": 4,
                "hasDate": True,
                "linkIncludes": [
                    "article",
                    "storyid",
                    "?p=",
                    "id=",
                    "/fpss/track",
                    ".html",
                    "/content/",
                ],
            },
            "proxyConfiguration": { "useApifyProxy": True },
            "useBrowser": False,
            "extendOutputFunction": """($) => {
                const result = {};
                // Uncomment to add a title to the output
                // result.pageTitle = $('title').text().trim();
                return result;
            }""",
        }

        # Run the Actor and wait for it to finish
        run = self.client.actor(self.actor_id).call(run_input=run_input)

        # Fetch Actor results from the run's dataset
        articles = list(self.client.dataset(run["defaultDatasetId"]).iterate_items())

        # Assign a unique ID to each article
        for article in articles:
            article['id'] = generate_article_id(article['url'])

        return articles
