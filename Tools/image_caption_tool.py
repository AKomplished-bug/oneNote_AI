import replicate
from langchain.tools import tool

class ImageCaptionTool:
    def __init__(self, model="cog/caption-image"):
        self.model = replicate.models.get(model)

    @tool("Generate Image Caption")
    def generate_caption(self, image_url):
        """Generates a caption for the image at the given URL."""
        try:
            output = self.model.predict(image=image_url)
            return output["caption"]
        except Exception as e:
            return f"Error generating image caption: {str(e)}"