import requests
from langchain.tools import tool
from io import BytesIO

class ImageDownloadTool:
    @tool("Download Images")
    def download_images(self, image_urls):
        """Downloads images from the given URLs and returns their contents."""
        try:
            downloaded_images = []
            for url in image_urls:
                response = requests.get(url, stream=True)
                if response.status_code == 200:
                    image_data = BytesIO(response.content)
                    downloaded_images.append(image_data)

            return downloaded_images
        except Exception as e:
            return f"Error downloading images: {str(e)}"