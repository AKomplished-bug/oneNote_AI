from langchain.tools import tool
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import WikipediaQueryRun

class WikipediaSearchTool:
    def __init__(self):
        self.wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

    @tool("Search Wikipedia")
    def search_wikipedia(self, query):
        """Useful to search Wikipedia for information about a given topic."""
        try:
            result = self.wikipedia.run(query)
            return result
        except Exception as e:
            return f"Sorry, I couldn't find anything about '{query}' on Wikipedia. Error: {str(e)}"