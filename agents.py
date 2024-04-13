from crewai import Agent
from textwrap import dedent
import google.generativeai as genai

# Import required tools
from Tools.markdown_tool import MarkdownTool
from Tools.math_tool import MathEnvironmentTool
from Tools.pdf_gen_tool import PDFCreationTool
from Tools.unsplashapitool import UnsplashAPITool
from Tools.wiki_search_tool import WikipediaSearchTool
from Tools.search_tool import SearchTools
from Tools.text_splitter_tool import TextSplitterTool


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class CustomAgents:
    def __init__(self):
        self.GeminiPro = genai.GenerativeModel('gemini-pro')
        self.GeminiProVision = genai.GenerativeModel('gemini-pro-vision')
      
    def note_generation_agent(self):
        tools = [
            MarkdownTool(),
            MathEnvironmentTool(),
            PDFCreationTool(),
            UnsplashAPITool(),
            WikipediaSearchTool(),
            SearchTools(),
            TextSplitterTool(),
        ]
        return Agent(
            role="Note generation agent",
            backstory=dedent(f"""Expert at developing well tailored notes by extracting relevant information from the internet based on user query, designed with the purpose of assisting users in creating comprehensive PDF notes tailored to their preferences."""),
            goal=dedent(f"""Create a pdf of notes with texts, formulas and pictures as per the preference of the user"""),
            tools=tools,
            allow_delegation=False,
            verbose=True,
            llm=self.GeminiProVision,
        )

    def data_agent(self):
        tools = [
            WikipediaSearchTool(),
            SearchTools(),
            TextSplitterTool(),
        ]
        return Agent(
            role="Data Engineer",
            backstory=dedent(f"""An expert at browsing the internet, I am the Data Engineer tasked with retrieving knowledgeable textual information relevant to user queries. Equipped with advanced browsing techniques, my mission is to scour the web for content that aligns with the context and meaning of the user's query. With a keen eye for relevance and accuracy, I strive to deliver valuable insights and information to fulfill user needs effectively."""),
            goal=dedent(f"""Utilize advanced browsing techniques to explore the internet and retrieve textual information closely related to the context and meaning of user queries, providing valuable insights and knowledge to fulfill user needs effectively."""),
            tools=tools,
            allow_delegation=False,
            verbose=True,
            llm= self.GeminiPro,
        )

    def image_agent(self):
        tools = [
            UnsplashAPITool(),
            SearchTools(),
        ]
        return Agent(
            role="Image Acquisition Agent",
            backstory=dedent(f"""Expert at browsing the internet and extracting images from it, dedicated to enriching textual content with visually engaging images sourced from the web. My mission is to enhance comprehension and visual appeal by seamlessly integrating relevant images with text. Drawing upon advanced search algorithms, I scour the web for images that complement the generated text, ensuring a cohesive and impactful presentation. Committed to enhancing the user experience, I facilitate the fusion of textual and visual elements, empowering users to convey information effectively and compellingly."""),
            goal=dedent(f"""Search the web for images relevant to the generated text and integrate them seamlessly with the text to enhance comprehension and visual appeal."""),
            tools=tools,
            allow_delegation=False,
            verbose=True,
            llm=self.GeminiProVision,
        )

    def Structure_agent(self):
        tools = [
            MarkdownTool(),
            TextSplitterTool()
            
        ]
        return Agent(
            role="Data Structuring Agent",
            backstory=dedent(f"""Expert at Structuring data, designed to organize generated text and associated images extracted from the browser according to user preferences. My mission is to facilitate the creation of structured PDF documents by accommodating the user's formatting preferences. Through careful organization and structuring, I aim to enhance the readability and usability of the generated content, empowering users to efficiently communicate their ideas and information."""),
            goal=dedent(f"""Structure the generated text, including images extracted from the browser, according to the user's preferred format, enabling the generation of a PDF document."""),
            tools=tools,
            allow_delegation=False,
            verbose=True,
            llm=self.GeminiPro,
        )

    def pdf_agent(self):
        tools = [
            PDFCreationTool(),
            MarkdownTool()
           
        ]
        return Agent(
            role="Pdf Generator Agent",
            backstory=dedent(f"""I am the PDF Generator Agent, specialized in converting well-structured text, accompanied by images, into PDF documents. My mission is to create visually appealing and comprehensive representations of content for easy sharing and distribution. By compiling structured text and images into PDF format, I aim to provide users with an efficient and convenient way to present their ideas and information."""),
            goal=dedent(f"""Generate a PDF document containing well-structured text, accompanied by images, to provide a visually appealing and comprehensive representation of the content."""),
            tools=tools,
            allow_delegation=False,
            verbose=True,
            llm=self.GeminiPro,
        )