from langchain.tools import tool
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import WikipediaQueryRun

class WikipediaSearchTool:
    @tool("Search Wikipedia")
    def search_wikipedia(self, query):
        """
        Search Wikipedia for information about a given topic.

        Args:
            query (str): The query to search for on Wikipedia.

        Returns:
            str: The search result from Wikipedia, or an error message if no results were found.
        """
        self.wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
        try:
            result = self.wikipedia.run(query)
            return result
        except Exception as e:
            return f"Sorry, I couldn't find anything about '{query}' on Wikipedia. Error: {str(e)}"