Design push notification :

Which sends the notification to the registered users
Which receives an event from promotions team
Sends notification to iOS, android or sends an email or all three

Interfaces:
IPushService: Defines methods like send_notification() to send notifications to devices.
IDeviceToken: Provides methods like get_device_token() to retrieve device tokens for push notifications.
IEmailService: Offers methods like send_email() to send notifications via email.

Models:
Notification: Represents a notification with attributes such as title, message, platform, and recipient.

Services and Design Patterns
NotificationService:
Manages user registration, notification sending, and event processing.
Implements register_user() and unregister_user() for managing user subscriptions.
Implements send_notification() to handle notifications based on the recipient's platform.
Implements process_event() to receive events from the promotions team and trigger notifications.

Observer Pattern for Event Handling:
Implement observer pattern to notify NotificationService when new events are received.

Factory Pattern for Notification Creation:
Use factory pattern (NotificationFactory) to create different types of notifications (iOS, Android, email).
