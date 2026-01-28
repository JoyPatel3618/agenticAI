from agents.planner_agent import PlannerAgent
from agents.executor_agent import ExecutorAgent
from agents.supervisor_agent import SupervisorAgent


planner = PlannerAgent("PlannerAgent")
executor = ExecutorAgent("ExecutorAgent")
supervisor = SupervisorAgent("SupervisorAgent")

task = planner.plan("Test agentic execution flow")
print("Before execution :",task)
executor.run(task)
print("After execution :",task)
supervisor.review(task)