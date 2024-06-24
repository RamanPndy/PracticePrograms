from systemdesign.jira.interface import Issue, User, Project, Workflow

class ConcreteUser(User):
    def __init__(self, user_id, user_role):
        self.user_id = user_id
        self.user_role = user_role

    def get_user_id(self):
        return self.user_id

    def get_user_role(self):
        return self.user_role

    def create_issue(self, issue):
        # logic to create an issue
        pass

    def assign_issue(self, issue, user):
        issue.assign_to_user(user)

    def change_issue_status(self, issue, status):
        issue.set_issue_status(status)

class ConcreteProject(Project):
    def __init__(self, project_id, project_name):
        self.project_id = project_id
        self.project_name = project_name
        self.issues = []

    def get_project_id(self):
        return self.project_id

    def get_project_name(self):
        return self.project_name

    def add_issue(self, issue):
        self.issues.append(issue)

    def get_issues(self):
        return self.issues

class ConcreteIssue(Issue):
    def __init__(self, issue_id, title, description):
        self.issue_id = issue_id
        self.title = title
        self.description = description
        self.status = "Open"
        self.assigned_user = None

    def get_issue_id(self):
        return self.issue_id

    def get_issue_title(self):
        return self.title

    def get_issue_description(self):
        return self.description

    def get_issue_status(self):
        return self.status

    def set_issue_status(self, status):
        self.status = status

    def assign_to_user(self, user):
        self.assigned_user = user

class ConcreteWorkflow(Workflow):
    def __init__(self):
        self.transitions = {
            "Open": ["In Progress", "Closed"],
            "In Progress": ["Closed", "Open"],
            "Closed": ["Open"]
        }

    def get_possible_transitions(self, current_status):
        return self.transitions.get(current_status, [])

