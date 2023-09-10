from langchain.document_loaders import JSONLoader
import json
from pathlib import Path
from pprint import pprint

class ArticleLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.loader = JSONLoader(
            file_path=self.file_path,
            jq_schema='.[].text',
            #metadata_func=self.metadata_func
        )

    # Define the metadata extraction function.
    @staticmethod
    def metadata_func(record: dict, metadata: dict) -> dict:
        metadata["title"] = record.get("title")
        metadata["author"] = ", ".join(record.get("author", []))  # Joining authors if it's a list
        return metadata

    def load(self):
        data = self.loader.load()
        return data

if __name__ == "__main__":
    FILE_PATH = './data/raw/articles.json'
    article_loader = ArticleLoader(FILE_PATH)
    data = article_loader.load()
    pprint(data)
