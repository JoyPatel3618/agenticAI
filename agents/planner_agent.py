from agents.base_agent import BaseAgent
from core.task import Task

class PlannerAgent(BaseAgent):
    def plan(self, goal):
        self.logger.info(
            f"Planning Tasks for goal : {goal}"
            )
        tasks =[ 
            Task(description=f"{goal} - Step 1"),
            Task(description=f"{goal} - Step 2"),
            Task(description=f"{goal} - Step 3"),            
        ]
        return tasks
    def run(self, task):
        raise NotImplementedError("PlannerAgent doest not execute tasks. Use plan() instead")