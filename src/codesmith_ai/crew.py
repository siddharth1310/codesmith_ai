# In-built packages (Standard Library modules)
from typing import List

# External packages
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent

# Our Own Imports
from .schemas import CodeResult

@CrewBase
class CodeSmith_AI():
    """
    The main Crew class that defines:
      - Agents (who perform the tasks)
      - Tasks (what needs to be done)
      - Crew (how agents and tasks are coordinated)
    
    This Crew uses a single agent `coder` and one task `coding_task`.
    """
    
    # These will be automatically populated based on your agents.yaml and tasks.yaml
    agents : List[BaseAgent]
    tasks : List[Task]
    
    # 🧑‍💻 Agent Definition
    @agent
    def coder(self) -> Agent:
        """
        Defines the coding agent responsible for generating and executing code.
        The agent is configured via agents.yaml file.
        """
        return Agent(config = self.agents_config["coder"],  # Load configuration from agents.yaml
                     verbose = True,  # Enable detailed logs for transparency
                     allow_code_execution = True,  # Allow the agent to run code safely
                     code_execution_mode = "safe",  # Prevents risky operations (isolated execution)
                     max_execution_time = 300,  # Max allowed runtime (in seconds)
                     max_retry_limit = 5  # Retry limit in case of transient errors
                     )
    
    # 🧩 Task Definition
    @task
    def coding_task(self) -> Task:
        """
        Defines the main task — writing and executing code for the given assignment.
        The task is configured via tasks.yaml and expects structured output defined by CodeResult.
        """
        return Task(config = self.tasks_config["coding_task"],  # Load description & metadata from tasks.yaml
                    output_pydantic = CodeResult  # Structured output format (Pydantic schema)
                    )
    
    # ⚙️ Crew Definition
    @crew
    def crew(self) -> Crew:
        """
        Creates and returns the Crew object which runs the workflow.
        Here, we have:
          - A list of agents (only 'coder' for now)
          - A list of tasks (only 'coding_task')
          - A sequential process (each task runs in order)
        """
        return Crew(agents = self.agents,  # Use agents defined above
                    tasks = self.tasks,  # Use tasks defined above
                    process = Process.sequential,  # Tasks execute one after another
                    verbose = True  # Show detailed logs during execution
                    )
