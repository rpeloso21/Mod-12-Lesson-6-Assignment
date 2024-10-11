import time

tasks = [
    {
        "id": 1,
        "name": "Complete Project Proposal",
        "subtasks": [
            {"id": 1, "name": "Research background information", "subtasks": [], "priority": 2},
            {"id": 2, "name": "Draft initial outline", "subtasks": [], "priority": 3},
            {"id": 3, "name": "Review with team", "subtasks": [], "priority": 1}
        ],
        "priority": 3
    },
    {
        "id": 2,
        "name": "Develop Website",
        "subtasks": [],
        "priority": 4
    },
    {
        "id": 3,
        "name": "Prepare for Presentation",
        "subtasks": [
            {"id": 1, "name": "Create slides", "subtasks": [
                {"id": 1, "name": "Open PowerPoint", "subtasks": [], "priority": 1},
                {"id": 2, "name": "Build each slide", "subtasks": [], "priority": 2}
            ], "priority": 2},
            {"id": 2, "name": "Practice speech", "subtasks": [], "priority": 2},
            {"id": 3, "name": "Gather feedback", "subtasks": [], "priority": 3}
        ],
        "priority": 5
    },
    {
        "id": 4,
        "name": "Organize Team Meeting",
        "subtasks": [],
        "priority": 2
    },
    {
        "id": 5,
        "name": "Conduct Market Research",
        "subtasks": [],
        "priority": 1
    }
]


def schedule_tasks(task_hierarchy):
    scheduled_tasks = []

    sorted_tasks = sorted(task_hierarchy, key=lambda task: task['priority'])

    for task in sorted_tasks:
        if len(task['subtasks']) == 0:
            scheduled_tasks.append(f"Id: {task['id']} Name: {task['name']}")
        else:
            scheduled_tasks.append(f"Id: {task['id']} Name: {task['name']}")
            for task in schedule_tasks(task['subtasks']):
                scheduled_tasks.append(f"--sub-- {task}")
    return scheduled_tasks


start_time = time.time()
schedule_tasks(tasks)
end_time = time.time()
time_to_completion = end_time - start_time

for task in schedule_tasks(tasks):
    print(task)

print(f"\nOperation completed in {time_to_completion:.7f} seconds")
            

        