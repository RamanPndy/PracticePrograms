from systemdesign.jira.impl import ConcreteIssue, ConcreteProject, ConcreteUser, ConcreteWorkflow

'''
Design Patterns Used
Factory Pattern: To create instances of users, projects, and issues.
Observer Pattern: To notify users when an issue status changes (not implemented in this basic example).
Strategy Pattern: For different workflows or issue handling strategies.
Singleton Pattern: For managing global configurations or workflows.
'''
if __name__ == "__main__":
    user1 = ConcreteUser("U1", "Developer")
    user2 = ConcreteUser("U2", "Manager")

    project = ConcreteProject("P1", "Project A")

    issue1 = ConcreteIssue("I1", "Fix Bug", "Bug description")
    issue2 = ConcreteIssue("I2", "Add Feature", "Feature description")

    project.add_issue(issue1)
    project.add_issue(issue2)

    user2.assign_issue(issue1, user1)
    user1.change_issue_status(issue1, "In Progress")

    workflow = ConcreteWorkflow()
    print(workflow.get_possible_transitions(issue1.get_issue_status()))

    user1.change_issue_status(issue1, "Closed")
    print(issue1.get_issue_status())
