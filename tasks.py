from crewai import Task
from textwrap import dedent



class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def generate_notes_task(self, agent, topic, preferences):
        if preferences.lower() == 'large':
            detail_level = "Generate an extensive and in-depth set of notes."
        else:
            detail_level = "Generate a concise set of notes."

        return Task(
            description=dedent(f"""
            Based on the given topic '{topic}' and generate larger or shorter content based on '{preferences}', {detail_level}
            {self.__tip_section()}
            Make sure to cover all aspects of the topic and present the information in a well-structured and visually appealing manner.
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

    def structure_content_task(self, agent, text):
     return Task(
        description=dedent(f"""
            Using the generated text:
            {text}
            Structure the content according to the user's preferred format, enabling the generation of a well-organized PDF document.
            {self.__tip_section()}
            Ensure the structured content is readable, visually appealing, and follows the specified formatting guidelines.
        """),
        agent=agent,
    )

    def generate_pdf_task(self, agent, structured_content):
     return Task(
        description=dedent(f"""
            Using the provided {structured_content}, structure the content in a way that would look good in a PDF document.
            {self.__tip_section()}
            Ensure the structured content is visually appealing, readable, and follows best practices for PDF formatting and layout. The goal is to create a comprehensive representation of the information that can be easily shared and presented.
            {self.__tip_section()}
            Make sure the output atleast contains {structured_content} and is suitable for easy sharing and distribution, providing users with an efficient way to present their ideas and information.
        """),
        agent=agent,
        
    )