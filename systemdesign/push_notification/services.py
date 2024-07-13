from typing import List
from systemdesign.push_notification.interface import IDeviceToken, IEmailService, IPushService
from systemdesign.push_notification.models import Notification


class NotificationService:
    def __init__(self, push_service: IPushService, email_service: IEmailService):
        self.push_service = push_service
        self.email_service = email_service
        self.registered_users: List[str] = []

    def register_user(self, user_id: str) -> None:
        if user_id not in self.registered_users:
            self.registered_users.append(user_id)

    def unregister_user(self, user_id: str) -> None:
        if user_id in self.registered_users:
            self.registered_users.remove(user_id)

    def send_notification(self, notification: Notification) -> None:
        if notification.platform == 'iOS' or notification.platform == 'Android':
            device_token = IDeviceToken().get_device_token(notification.recipient)
            # Logic to send push notification using push_service
            self.push_service.send_notification(notification)
        elif notification.platform == 'Email':
            # Logic to send email notification using email_service
            self.email_service.send_email(notification)

    def process_event(self, event: dict) -> None:
        # Example event handling logic
        title = event['title']
        message = event['message']
        platform = event['platform']
        recipient = event['recipient']
        
        notification = Notification(title, message, platform, recipient)
        self.send_notification(notification)

class iOSPushService(IPushService):
    def send_notification(self, notification: Notification) -> None:
        # Logic to send iOS push notification
        print(f"Sending iOS push notification to {notification.recipient}")

class AndroidPushService(IPushService):
    def send_notification(self, notification: Notification) -> None:
        # Logic to send Android push notification
        print(f"Sending Android push notification to {notification.recipient}")

class EmailService(IEmailService):
    def send_email(self, notification: Notification) -> None:
        # Logic to send email notification
        print(f"Sending email notification to {notification.recipient}")
