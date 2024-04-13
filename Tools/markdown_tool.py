import markdown
from langchain.tools import tool

class MarkdownTool:
    @tool("Convert Markdown to HTML")
    def convert_markdown_to_html(self, markdown_text):
        """Converts Markdown text to HTML."""
        try:
            html = markdown.markdown(markdown_text)
            return html
        except Exception as e:
            return f"Error converting Markdown to HTML: {str(e)}"

    @tool("Convert Markdown to Plain Text")
    def convert_markdown_to_text(self, markdown_text):
        """Converts Markdown text to plain text."""
        try:
            plain_text = markdown.markdown(markdown_text, output_format="plain")
            return plain_text
        except Exception as e:
            return f"Error converting Markdown to plain text: {str(e)}"