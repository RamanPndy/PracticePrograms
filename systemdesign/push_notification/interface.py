from systemdesign.push_notification.models import Notification

class IPushService:
    def send_notification(self, notification: 'Notification') -> None:
        pass

class IDeviceToken:
    def get_device_token(self, recipient: str) -> str:
        pass

class IEmailService:
    def send_email(self, notification: 'Notification') -> None:
        pass