from crewai import Crew, Process
from agents import researcher, writer
from tasks import research_task, writing_task

hospitality_crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    process=Process.sequential,   # Researcher runs first, then Writer
    verbose=True
)
