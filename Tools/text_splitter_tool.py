from langchain.tools import tool
from langchain.text_splitter import CharacterTextSplitter

class TextSplitterTool:
    def __init__(self, chunk_size=1000, chunk_overlap=200):
        self.text_splitter = CharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    @tool("Split Text into Chunks")
    def split_text(self, text):
        """Split a large text into smaller, more manageable chunks."""
        try:
            chunks = self.text_splitter.split_text(text)
            return chunks
        except Exception as e:
            return f"Error splitting text: {str(e)}"