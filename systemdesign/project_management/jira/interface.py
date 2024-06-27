from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def get_user_id(self):
        pass

    @abstractmethod
    def get_user_role(self):
        pass

    @abstractmethod
    def create_issue(self, issue):
        pass

    @abstractmethod
    def assign_issue(self, issue, user):
        pass

    @abstractmethod
    def change_issue_status(self, issue, status):
        pass

class Project(ABC):
    @abstractmethod
    def get_project_id(self):
        pass

    @abstractmethod
    def get_project_name(self):
        pass

    @abstractmethod
    def add_issue(self, issue):
        pass

    @abstractmethod
    def get_issues(self):
        pass

class Issue(ABC):
    @abstractmethod
    def get_issue_id(self):
        pass

    @abstractmethod
    def get_issue_title(self):
        pass

    @abstractmethod
    def get_issue_description(self):
        pass

    @abstractmethod
    def get_issue_status(self):
        pass

    @abstractmethod
    def set_issue_status(self, status):
        pass

    @abstractmethod
    def assign_to_user(self, user):
        pass

class Workflow(ABC):
    @abstractmethod
    def get_possible_transitions(self, current_status):
        pass
