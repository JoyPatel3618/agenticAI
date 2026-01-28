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
            retry_count = task.context.get("retry_count",0)
            max_retries = task.context.get("max_retries",3)
            self.logger.info(
                f"Task failed. Retry attempt {retry_count}/{max_retries}"
            )
            if retry_count < max_retries:
                retry_count+=1
                task.context["retry_count"]=retry_count
                task.state= TaskState.PENDING
                self.logger.info(
                    f"Retry approved. Re-queuing task (attempt {retry_count})"
                )
            else:
                self.logger.error(
                    "Retry limit exceeded. Task marked as terminal failure"
                )