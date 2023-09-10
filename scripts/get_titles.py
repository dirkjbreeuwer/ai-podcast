import json

# Load the articles from the JSON file
with open('./data/raw/articles.json', 'r') as file:
    data = json.load(file)

# Check if the data is a list
if isinstance(data, list):
    # Print the titles of the articles
    for article in data:
        title = article.get('title')
        if title:
            print(title)
else:
    print("The JSON structure is not as expected. Please ensure it's a list of articles.")

