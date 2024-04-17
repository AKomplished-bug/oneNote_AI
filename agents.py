from crewai import Agent
from textwrap import dedent
from langchain_google_genai import ChatGoogleGenerativeAI
import os
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
        google_api_key = os.getenv("GOOGLE_API_KEY")
        self.llm = ChatGoogleGenerativeAI(
        model="gemini-pro", verbose=True, temperature=0.9, google_api_key=google_api_key
    )
      
    def note_generation_agent(self):
        tools = [
           
            MathEnvironmentTool.render_math,
            PDFCreationTool.create_pdf,
            WikipediaSearchTool.search_wikipedia,
            TextSplitterTool.split_text,
            SearchTools.search_internet,
            SearchTools.search_browser
        ]
        return Agent(
            role="Note generation agent",
            backstory=dedent(f"""Expert at developing well tailored notes by extracting relevant information from the internet based on user query, designed with the purpose of assisting users in creating comprehensive PDF notes tailored to their preferences."""),
            goal=dedent(f"""Create a long or short pdf of notes with texts, formulas, code, etc as per the preference of the user"""),
            tools=tools,
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
        )

    def data_agent(self):
        tools = [
             WikipediaSearchTool.search_wikipedia,
             SearchTools.search_internet,
             TextSplitterTool.split_text,
             SearchTools.search_browser
        ]
        return Agent(
            role="Data Engineer",
            backstory=dedent(f"""An expert at browsing the internet, I am the Data Engineer tasked with retrieving knowledgeable textual information relevant to user queries. Equipped with advanced browsing techniques, my mission is to scour the web for content that aligns with the context and meaning of the user's query. With a keen eye for relevance and accuracy, I strive to deliver valuable insights and information to fulfill user needs effectively."""),
            goal=dedent(f"""Utilize advanced browsing techniques to explore the internet and retrieve textual information closely related to the context and meaning of user queries, providing valuable insights and knowledge to fulfill user needs effectively."""),
            tools=tools,
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
        )

    # def image_agent(self):
    #     tools = [
            
    #         SearchTools.search_internet,
    #     ]
    #     return Agent(
    #         role="Image Acquisition Agent",
    #         backstory=dedent(f"""Expert at browsing the internet and extracting images from it, dedicated to enriching textual content with visually engaging images sourced from the web. My mission is to enhance comprehension and visual appeal by seamlessly integrating relevant images with text. Drawing upon advanced search algorithms, I scour the web for images that complement the generated text, ensuring a cohesive and impactful presentation. Committed to enhancing the user experience, I facilitate the fusion of textual and visual elements, empowering users to convey information effectively and compellingly."""),
    #         goal=dedent(f"""Search the web for images relevant to the generated text and integrate them seamlessly with the text to enhance comprehension and visual appeal."""),
    #         tools=tools,
    #         allow_delegation=False,
    #         verbose=True,
    #         llm=self.llm,
    #     )

    def Structure_agent(self):
        tools = [
            
            TextSplitterTool.split_text,
            
        ]
        return Agent(
            role="Data Structuring Agent",
            backstory=dedent(f"""Expert at Structuring data, designed to organize generated text  from the browser according to user preferences. My mission is to facilitate the creation of structured PDF documents by accommodating the user's formatting preferences. Through careful organization and structuring, I aim to enhance the readability and usability of the generated content, empowering users to efficiently communicate their ideas and information."""),
            goal=dedent(f"""Structure the generated text, according to the user's preferred format, enabling the generation of a PDF document."""),
            tools=tools,
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
        )

    def pdf_agent(self):
        tools = [
            PDFCreationTool.create_pdf,
            TextSplitterTool.split_text,
           
        ]
        return Agent(
            role="Pdf Generator Agent",
            backstory=dedent(f""" I am the PDF Content Structuring Agent, specialized in organizing and formatting text into a well-structured, visually appealing format suitable for inclusion in a PDF document. My mission is to create comprehensive, easy-to-consume representations of content that can be efficiently shared and presented. By structuring the text in a way that is readable, visually engaging, and follows formatting guidelines, I aim to help users convey their ideas and information effectively through PDF documents."""),
            goal=dedent(f"""Organize the provided text into a well-structured, visually appealing format that would look good in a PDF document. Ensure the content is readable, follows proper formatting guidelines, and enhances the overall presentation."""),
            tools=tools,
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
        )