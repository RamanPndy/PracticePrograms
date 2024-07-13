class Notification:
    def __init__(self, title: str, message: str, platform: str, recipient: str):
        self.title = title
        self.message = message
        self.platform = platform
        self.recipient = recipient