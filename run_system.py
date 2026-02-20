from agents.planner_agent import PlannerAgent
from agents.executor_agent import ExecutorAgent
from agents.supervisor_agent import SupervisorAgent
from core.queue import TaskQueue
from core.scheduler import Scheduler

planner = PlannerAgent("Planner")
executor = ExecutorAgent("Executor")
supervisor = SupervisorAgent("Supervisor")

queue = TaskQueue()

tasks = planner.plan("Run autonomous agent system")
for task in tasks:
    queue.enqueue(task)

scheduler = Scheduler(queue, executor, supervisor)
scheduler.run()
