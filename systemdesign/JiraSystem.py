import uuid
from datetime import datetime
from enum import Enum

class IssueStatus(Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
    CLOSED = "Closed"

class User:
    def __init__(self, name):
        self.user_id = str(uuid.uuid4())
        self.name = name

class Issue:
    def __init__(self, summary, description, reporter, assignee=None):
        self.issue_id = str(uuid.uuid4())
        self.summary = summary
        self.description = description
        self.reporter = reporter
        self.assignee = assignee
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        self.status = IssueStatus.OPEN

    def assign(self, assignee):
        self.assignee = assignee
        self.status = IssueStatus.IN_PROGRESS
        self.updated_at = datetime.now()

    def resolve(self):
        self.status = IssueStatus.RESOLVED
        self.updated_at = datetime.now()

    def reopen(self):
        self.status = IssueStatus.OPEN
        self.updated_at = datetime.now()

    def close(self):
        self.status = IssueStatus.CLOSED
        self.updated_at = datetime.now()

class Project:
    def __init__(self, name, description):
        self.project_id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.issues = []

    def create_issue(self, summary, description, reporter, assignee=None):
        issue = Issue(summary, description, reporter, assignee)
        self.issues.append(issue)
        return issue

class JiraSystem:
    def __init__(self):
        self.users = {}
        self.projects = {}

    def create_user(self, name):
        user = User(name)
        self.users[user.user_id] = user
        return user

    def create_project(self, name, description):
        project = Project(name, description)
        self.projects[project.project_id] = project
        return project
    
    def get_issue(self, issue_id):
        for project in self.projects.values():
            for issue in project.issues:
                if issue.issue_id == issue_id:
                    return issue
        return None
    
    def create_issue(self, project_id, summary, description, assignee_id=None):
        project = self.projects.get(project_id)
        if project:
            assignee = self.users.get(assignee_id) if assignee_id else None
            issue = Issue(summary, description, assignee)
            project.issues.append(issue)
            return issue
        else:
            print("Project not found.")
    
    def get_issues_by_project(self, project_id):
        project = self.projects.get(project_id)
        if project:
            return project.issues
        else:
            print("Project not found.")

# Example usage
if __name__ == "__main__":
    jira_system = JiraSystem()

    # Create users
    user1 = jira_system.create_user("Alice")
    user2 = jira_system.create_user("Bob")

    # Create project
    project1 = jira_system.create_project("Project 1", "Description for Project 1")

    # Create issues
    issue1 = project1.create_issue("Bug 1", "Description of Bug 1", user1)
    issue2 = project1.create_issue("Feature 1", "Description of Feature 1", user2)

    # Assign issue
    issue1.assign(user2)

    # Resolve issue
    issue1.resolve()

    # Reopen issue
    issue1.reopen()

    # Display issue details
    print("Issue ID:", issue1.issue_id)
    print("Summary:", issue1.summary)
    print("Description:", issue1.description)
    print("Reporter:", issue1.reporter.name)
    print("Assignee:", issue1.assignee.name if issue1.assignee else "Unassigned")
    print("Status:", issue1.status)
    print("Created At:", issue1.created_at)
    print("Updated At:", issue1.updated_at)
