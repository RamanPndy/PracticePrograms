'''
Given a company's hierarchy graph with Employees and departments, find the closest department between a list of employees.
Problem Assumptions

You have:

A hierarchy graph (tree or general graph) where nodes = employees, and some nodes are departments.

Given a list of employees, find the closest department for each.

“Closest” = minimum number of edges between employee → department.

Approach (Optimal)

Use multi-source BFS starting from all department nodes, then compute the shortest distance to each employee.

This is optimal because:

BFS gives shortest path in an unweighted graph.

Multi-source BFS gives shortest dept for all employees in one pass, O(N + E).
'''
from collections import deque, defaultdict

def closest_departments(employees, departments, edges):
    """
    employees: list of employee IDs we need to find closest dept for
    departments: list of department node IDs
    edges: list of (u, v) relations forming the hierarchy graph
    """

    # Build graph adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Multi-source BFS from all departments
    queue = deque()
    distance = {}
    nearest_dept = {}

    # Initialize BFS queue
    for dept in departments:
        queue.append(dept)
        distance[dept] = 0
        nearest_dept[dept] = dept  # dept's nearest dept is itself

    # BFS
    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in distance:
                distance[neighbor] = distance[node] + 1
                nearest_dept[neighbor] = nearest_dept[node]
                queue.append(neighbor)

    # Return closest department for each employee
    result = {}
    for emp in employees:
        if emp in nearest_dept:
            result[emp] = nearest_dept[emp]
        else:
            result[emp] = None  # unreachable?

    return result

'''
variation #1: if the employee didn't exist
If an employee ID does not exist in the hierarchy graph, you should return None (or raise an exception if you prefer).
'''

def closest_departments(employees, departments, edges):
    """
    employees: list of employee IDs
    departments: list of department node IDs
    edges: list of (u, v) relations representing hierarchy
    """

    # Build graph adjacency list
    graph = defaultdict(list)
    all_nodes = set()

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        all_nodes.add(u)
        all_nodes.add(v)

    # Multi-source BFS from all departments
    queue = deque()
    distance = {}
    nearest_dept = {}

    for dept in departments:
        if dept in all_nodes:          # Only enqueue valid departments
            queue.append(dept)
            distance[dept] = 0
            nearest_dept[dept] = dept

    # BFS
    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in distance:
                distance[neighbor] = distance[node] + 1
                nearest_dept[neighbor] = nearest_dept[node]
                queue.append(neighbor)

    # Prepare results
    result = {}

    for emp in employees:
        if emp not in all_nodes:
            result[emp] = None              # Employee does not exist
        else:
            result[emp] = nearest_dept.get(emp)  # May still be None if unreachable

    return result