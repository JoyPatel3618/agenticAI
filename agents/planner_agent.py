from agents.base_agent import BaseAgent
from core.task import Task

class PlannerAgent(BaseAgent):
    def plan(self, goal):
        self.logger.info(
            f"Planning Task for goal : {goal}"
            )
        task = Task(description=goal)
        return task
    def run(self, task):
        raise NotImplementedError("PlannerAgent doest not execute tasks. Use plan() instead.")