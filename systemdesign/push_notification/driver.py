from systemdesign.push_notification.services import EmailService, NotificationService, iOSPushService

push_service = iOSPushService()  # Initialize appropriate push service
email_service = EmailService()
notification_service = NotificationService(push_service, email_service)

# Register users
notification_service.register_user("user1")
notification_service.register_user("user2")

# Simulate receiving an event
event = {
    'title': 'New Promotion',
    'message': 'Check out our latest deals!',
    'platform': 'iOS',
    'recipient': 'user1'
}

# Process the event and send notifications
notification_service.process_event(event)