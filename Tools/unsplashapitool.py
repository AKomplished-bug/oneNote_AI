import os
from langchain.tools import tool
from unsplash import UnsplashClient

class UnsplashAPITool:
    def __init__(self, num_results=5):
        self.client = UnsplashClient(access_key=os.environ["UNSPLASH_ACCESS_KEY"])
        self.num_results = num_results

    @tool("Search Unsplash for Images")
    def search_unsplash(self, query):
        """Searches Unsplash for images related to the given query."""
        try:
            response = self.client.search.photos(query, per_page=self.num_results)
            image_urls = []
            for photo in response.photos:
                image_urls.append(photo.urls.full)

            return image_urls
        except Exception as e:
            return f"Error searching Unsplash: {str(e)}"