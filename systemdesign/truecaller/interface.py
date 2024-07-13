from abc import ABC, abstractmethod
from systemdesign.truecaller.models import CallerInfo, User

class UserService:
    def register_user(self, user_details: dict) -> User:
        pass

    def login_user(self, phone_number: str, password: str) -> User:
        pass

    def update_profile(self, user_id: str, profile_data: dict) -> bool:
        pass

class ContactService:
    def sync_contacts(self, user_id: str, contacts: list) -> bool:
        pass

    def get_contacts(self, user_id: str) -> list:
        pass

class CallerIdService:
    def identify_caller(self, phone_number: str) -> CallerInfo:
        pass

    def report_spam(self, phone_number: str) -> bool:
        pass

class SpamService:
    def block_number(self, user_id: str, phone_number: str) -> bool:
        pass

    def is_spam(self, phone_number: str) -> bool:
        pass

class SearchService:
    def search_number(self, phone_number: str) -> CallerInfo:
        pass

class ICallerIDService(ABC):
    @abstractmethod
    def identifyCaller(self, phoneNumber: str):
        pass

class ISubscriber(ABC):
    @abstractmethod
    def update(self, info):
        pass

class ISpamDetectionStrategy(ABC):
    @abstractmethod
    def isSpam(self, call):
        pass