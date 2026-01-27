from agents.base_agent import BaseAgent
from core.task import TaskState

class SupervisorAgent(BaseAgent):
    def run(self,task):
        self.review(task)
    def review(self, task):
        if task.state == TaskState.PENDING:
            self.logger.info("Task pending, no action required")
        elif task.state == TaskState.RUNNING:
            self.logger.info("Task already in execution, monitoring")
        elif task.state == TaskState.COMPLETED:
            self.logger.info("Task completed successfully")
        elif task.state == TaskState.FAILED:
            self.logger.info("Task failed, requires a decision to be made")
