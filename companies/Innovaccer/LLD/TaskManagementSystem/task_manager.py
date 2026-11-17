import heapq
from uuid import UUID
from datetime import datetime
import models
'''
A simple implementation could use:
- Dictionary: Store tasks using task ID.
- Heap: Retrieve the highest-priority task efficiently.

Why a heap?
Suppose we have 10,000 tasks and want to retrieve the highest-priority task.
Using a dictionary alone would require scanning all tasks, resulting in O(n) time complexity.
A heap allows us to get the highest-priority task in O(1) time and maintain 
the heap in O(log n) time when adding or removing tasks.
A heap provides O(log n) insertion and O(1) access to the highest-priority element.

'''
class TaskManager:

    def __init__(self):
        self.tasks = {}
        self.priority_queue = []
        self.sequence = 0 # Sequence number to maintain insertion order in the heap

    def create_task(self, task: models.Task):
        self.tasks[task.id] = task

        heapq.heappush(
            self.priority_queue,
            (
                -task.priority.value, # Use negative value to simulate max-heap with min-heap
                self.sequence,
                task.id
            )
        )

        self.sequence += 1

        return task.id

    def get_highest_priority_task(self):

        while self.priority_queue:
            priority, seq, task_id = self.priority_queue[0]

            task = self.tasks.get(task_id)

            if task is None or task.status == models.TaskStatus.COMPLETED:
                heapq.heappop(self.priority_queue)
                continue

            return task

        return None

    def complete_task(self, task_id: UUID):

        task = self.tasks.get(task_id)

        if task is None:
            raise ValueError("Task not found")

        task.status = models.TaskStatus.COMPLETED

    def delete_task(self, task_id: UUID):

        if task_id not in self.tasks:
            raise ValueError("Task not found")

        del self.tasks[task_id]

    def get_task(self, task_id: UUID):
        return self.tasks.get(task_id)

    def get_overdue_tasks(self):
        now = datetime.now()

        return [
            task
            for task in self.tasks.values()
            if task.due_date
            and task.due_date < now
            and task.status != models.TaskStatus.COMPLETED
        ]

manager = TaskManager()

t1 = models.Task("Write API", "", models.Priority.MEDIUM)
t2 = models.Task("Fix production bug", "", models.Priority.CRITICAL)
t3 = models.Task("Write documentation", "", models.Priority.LOW)

manager.create_task(t1)
manager.create_task(t2)
manager.create_task(t3)

task = manager.get_highest_priority_task()

print(task.title)

'''
What if two tasks have the same priority?
In our implementation, we use a sequence number to maintain the insertion order in the heap.
This ensures that if two tasks have the same priority, the one that was added first will be retrieved first.

What if the priority changes?
In our current implementation, changing the priority of a task does not automatically update its position in the heap.
To handle this, we would need to remove the task from the heap and re-insert it with the new priority.

What if a task is deleted while it is still in the heap?
In our implementation, when a task is deleted, it is removed from the `tasks` dictionary but not from the heap.
This means that the task may still exist in the heap temporarily.
However, when we try to retrieve the highest priority task, we check if the task exists in the `tasks` dictionary.
If it does not exist, we pop it from the heap and continue to the next task.

How would you make this thread-safe?
In a multi-threaded environment, we would need to use locks to ensure that operations on the `tasks` dictionary and the `priority_queue` heap are atomic.
This would prevent race conditions where multiple threads try to create, complete, or delete tasks simultaneously.

How would you support recurring tasks?
In our implementation, tasks are one-time by default.
To support recurring tasks, we could add a recurrence rule to the task model (e.g., daily, weekly, monthly).
When a recurring task is completed, we would automatically create a new instance of the task with the next due date based on the recurrence rule.

How would you support multiple users?
In our implementation, tasks are not associated with any specific user.
To support multiple users, we could add a `user_id` attribute to the task model.
We would then filter tasks based on the user when retrieving, updating, or deleting tasks.
This would allow each user to have their own set of tasks while still using the same task management system.

How would you efficiently retrieve tasks by due date?
In our current implementation, we iterate over all tasks to find overdue tasks.
To efficiently retrieve tasks by due date, we could maintain a separate data structure, such as a sorted list or a priority queue, keyed by due date.
This would allow us to quickly find tasks that are due soon or overdue without scanning the entire task list.
'''