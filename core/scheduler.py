from core.task import TaskState
import time

class Scheduler:
    def __init__(self,task_queue,executor,supervisor,poll_interval=1):
        self.task_queue=task_queue
        self.executor=executor
        self.supervisor=supervisor
        self.poll_interval=poll_interval

    def run(self):
        while True:
            task=self.task_queue.dequeue()
            if task is None:
                time.sleep(self.poll_interval)
                continue
            self.executor.run(task)
            self.supervisor.run(task)
            if task.state == TaskState.PENDING:
                self.task_queue.enqueue(task)