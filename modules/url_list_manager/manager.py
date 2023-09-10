class URLListManager:
    def __init__(self, initial_urls=None):
        self.urls = initial_urls if initial_urls else []

    def add_url(self, url):
        """Add a new URL to the list."""
        if url not in self.urls:
            self.urls.append(url)
            return f"URL {url} added successfully!"
        return f"URL {url} already exists in the list."

    def remove_url(self, url):
        """Remove a URL from the list."""
        if url in self.urls:
            self.urls.remove(url)
            return f"URL {url} removed successfully!"
        return f"URL {url} does not exist in the list."

    def get_urls(self):
        """Retrieve the list of URLs."""
        return self.urls

    def load_urls_from_file(self, file_path):
        """Load URLs from a file."""
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                self.add_url(line.strip())

    def save_urls_to_file(self, file_path="data/raw/initial_urls.txt"):
        """Save URLs to a file."""
        with open(file_path, 'w') as file:
            for url in self.urls:
                file.write(url + '\n')

