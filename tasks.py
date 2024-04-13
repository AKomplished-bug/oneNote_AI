from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def generate_notes_task(self, agent, topic, preferences):
     return Task(
        description=dedent(f"""
            Based on the given topic '{topic}' and the user's preferences '{preferences}', 
            generate a comprehensive set of notes in the form of text, formulas, and relevant images.
            {self.__tip_section()}
            Make sure to cover all the important aspects of the topic and present the information in a well-structured and visually appealing manner.
        """),
        agent=agent,
    )

    def gather_information_task(self, agent, topic):
     return Task(
        description=dedent(f"""
            Use advanced browsing techniques to explore the internet and retrieve valuable textual information closely related to the topic '{topic}'.
            {self.__tip_section()}
            Ensure the information is relevant, accurate, and up-to-date.
        """),
        agent=agent,
    )

    def search_images_task(self, agent, topic, text):
     return Task(
        description=dedent(f"""
            Based on the topic '{topic}' and the generated text:
            {text}
            Search the web for relevant images that complement and enhance the textual content.
            {self.__tip_section()}
            Make sure the images are visually engaging and help convey the information more effectively.
        """),
        agent=agent,
    )

    def structure_content_task(self, agent, text, images):
     return Task(
        description=dedent(f"""
            Using the generated text:
            {text}
            And the associated images:
            {images}
            Structure the content according to the user's preferred format, enabling the generation of a well-organized PDF document.
            {self.__tip_section()}
            Ensure the structured content is readable, visually appealing, and follows the specified formatting guidelines.
        """),
        agent=agent,
    )

    def generate_pdf_task(self, agent, structured_content):
     return Task(
        description=dedent(f"""
            Using the well-structured content:
            {structured_content}
            Generate a PDF document that combines the text and images in a visually appealing and comprehensive representation.
            {self.__tip_section()}
            Make sure the PDF is suitable for easy sharing and distribution, providing users with an efficient way to present their ideas and information.
        """),
        agent=agent,
    )