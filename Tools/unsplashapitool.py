import os
from langchain.tools import tool
from unsplash.api import Api
from unsplash.auth import Auth

class UnsplashAPITool:
    def __init__(self, num_results=5):
        access_key = os.getenv("UNSPLASH_ACCESS_KEY")
        secret_key = os.getenv("UNSPLASH_SECRET_KEY")
        self.client = Api(Auth(access_key, secret_key))
        self.num_results = num_results
        
    @tool("Search Unsplash for Images")
    def search_unsplash(self, query):
        """Searches Unsplash for images related to the given query."""
        try:
            response = self.client.search.photos.get(query=query, per_page=self.num_results)
            image_urls = [photo.urls.full for photo in response]
            return image_urls
        except Exception as e:
            return f"Error searching Unsplash: {str(e)}"