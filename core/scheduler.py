from core.task import TaskState
import time

class Scheduler:
    def __init__(self,task_queue,executor,supervisor,poll_interval=1):
        self.task_queue=task_queue
        self.executor=executor
        self.supervisor=supervisor
        self.poll_interval=poll_interval
        self.completed_tasks=set()
    
    def dependency_resolved(self,task):
        deps = task.context.get("depends_on",[])
        if not deps:
            return True
        return all(dep_id in self.completed_tasks for dep_id in deps)

    def run(self):
        while True:
            task=self.task_queue.dequeue()
            if task is None:
                time.sleep(self.poll_interval)
                continue
            if not self.dependency_resolved(task):
                self.task_queue.enqueue(task)
                time.sleep(self.poll_interval)
                continue

            self.executor.run(task)
            self.supervisor.run(task)
            
            if task.state == TaskState.COMPLETED:
                self.completed_tasks.add(task.id)

            if task.state == TaskState.PENDING:
                self.task_queue.enqueue(task)