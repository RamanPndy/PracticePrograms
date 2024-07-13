class User:
    def __init__(self, user_id: str, name: str, phone_number: str, password: str, email: str = None):
        self.user_id = user_id
        self.name = name
        self.phone_number = phone_number
        self.password = password
        self.email = email

class CallerInfo:
    def __init__(self, phone_number: str, name: str, spam_score: int = 0):
        self.phone_number = phone_number
        self.name = name
        self.spam_score = spam_score

class CallInfo:
    def __init__(self, callerInfo: CallerInfo, time, duration: int):
        self.callerInfo = callerInfo
        self.time = time
        self.duration = duration