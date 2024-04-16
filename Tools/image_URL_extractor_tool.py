import os
from langchain.tools import tool
import os, requests, re
import json

class UnsplashAPITool:
    
    @tool("Search Unsplash for Images")
    def search_unsplash(self, query):
        """Searches Unsplash for images related to the given query."""
        
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        image_url = response.data[0].url
        words = query.split()[:5] 
        safe_words = [re.sub(r'[^a-zA-Z0-9_]', '', word) for word in words]  
        filename = "_".join(safe_words).lower() + ".png"
        filepath = os.path.join(os.getcwd(), filename)

    # Download the image from the URL
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            with open(filepath, 'wb') as file:
             file.write(image_response.content)
        else:
            print("Failed to download the image.")
            return ""

        return filepath
