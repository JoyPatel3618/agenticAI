from agents.base_agent import BaseAgent
from core.task import Task

class PlannerAgent(BaseAgent):
    def plan(self, goal):
        self.logger.info(f"Planning Tasks for goal : {goal}")
        t1 = Task(description=f"{goal} - Step 1")
        t2 = Task(description=f"{goal} - Step 2")
        t3 = Task(description=f"{goal} - Step 3")

        t2.context["depends_on"]=[t1.id]
        t3.context["depends_on"]=[t2.id]
        
        return [t1,t2,t3]
    def run(self, task):
        raise NotImplementedError("PlannerAgent doest not execute tasks. Use plan() instead")