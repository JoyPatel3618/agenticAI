from core.task import TaskState
from core.retry import retry
from agents.base_agent import BaseAgent

class ExecutorAgent(BaseAgent):
    def run(self,task):
        if task.state != TaskState.PENDING :
            self.logger.error(
                f"Cannot execute task {task.id} in state {task.state.value}"
            )
            return
        self.logger.info("Starting Execution ...")
        task.state=TaskState.RUNNING
        def execute():
            self.logger.info("Executing Task!!!")
            task.context["result"]="done"
            return True
        try:
            retry(execute)
            task.state=TaskState.COMPLETED
            self.logger.info(
                f"Task {task.id} completed successfully"
                )
            
        except Exception as e:
            task.state=TaskState.FAILED
            self.logger.error(
                f"Task {task.id} failed with error {e}"
                )

