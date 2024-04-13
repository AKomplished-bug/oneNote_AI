from crewai import Crew
from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks

from dotenv import load_dotenv
load_dotenv()



# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py
class CustomCrew:
    def __init__(self, topic):
        self.topic = topic

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
        data_task = tasks.data_gathering_task(data_agent, self.topic)
        image_task = tasks.image_gathering_task(image_agent, self.topic)
        structuring_task = tasks.structuring_task(structure_agent, data_task, image_task)
        pdf_task = tasks.pdf_generation_task(pdf_agent, structuring_task)

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
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    topic = input(dedent("""Enter the topic for which you want to generate notes: """))
    custom_crew = CustomCrew(topic)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is your custom crew run result:")
    print("########################\n")
    print(result)