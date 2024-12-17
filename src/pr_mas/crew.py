from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class PrimitiveReflexesCrew():
    """Primitive Reflexes Health Blog Crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def medical_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['medical_researcher'],
            verbose=True
        )

    @agent
    def health_content_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['health_content_writer'],
            verbose=True
        )

    @agent
    def medical_editor(self) -> Agent:
        return Agent(
            config=self.agents_config['medical_editor'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def blog_drafting_task(self) -> Task:
        return Task(
            config=self.tasks_config['blog_drafting_task'],
        )

    @task
    def medical_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['medical_review_task'],
            output_file='primitive_reflexes_blog.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Primitive Reflexes Health Blog crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )