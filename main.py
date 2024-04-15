from crewai import Crew
from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks
from fpdf import FPDF
import os

from dotenv import load_dotenv
load_dotenv()



# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py
class CustomCrew:
    def __init__(self, topic,preference):
        self.topic = topic
        self.preference=preference
      

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents
        note_generation_agent = agents.note_generation_agent()
        data_agent = agents.data_agent()
        image_agent = agents.image_agent()
        structure_agent = agents.Structure_agent()
        pdf_agent = agents.pdf_agent()

        # Define your custom tasks
        data_task = tasks.generate_notes_task(data_agent, self.topic,self.preference)
        image_task = tasks.search_images_task(image_agent, self.topic,data_task)
        structuring_task = tasks.structure_content_task(structure_agent, data_task, image_task)
        pdf_task = tasks.generate_pdf_task(pdf_agent, structuring_task)

        # Define your custom crew
        crew = Crew(
            agents=[note_generation_agent, data_agent, image_agent, structure_agent, pdf_agent],
            tasks=[data_task, image_task, structuring_task, pdf_task],
            verbose=True,
        )
        result = crew.kickoff()
        return result

# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print(f"\n{'#' * 50}")
    print(f"\033[1;34m{'## Welcome to OneNote AI':^50}\033[0m")
    print(f"{'#' * 50}\n")
    print("\033[1;33m-------------------------------\033[0m")

    topic = input(dedent("""Enter the topic for which you want to generate notes: """))
    preference = input(dedent("""Enter the prefered length of notes(short or long): """))
    custom_crew = CustomCrew(topic,preference)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is your custom crew run result:")
    print("########################\n")
    print(result)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add the result to the PDF
    for line in result.split("\n"):
        pdf.multi_cell(0, 10, txt=line)

    # Create the 'pdf' directory if it doesn't exist
    pdf_dir = "pdf"
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)

    # Save the PDF file
    pdf_file_path = os.path.join(pdf_dir, f"notes_{topic.replace(' ', '_')}.pdf")
    pdf.output(pdf_file_path, 'F')
    print(f"\n\033[1;34mPDF file created: {pdf_file_path}\033[0m")