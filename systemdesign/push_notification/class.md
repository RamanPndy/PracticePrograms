+---------------------+        +---------------------+         +-------------------------+
|      IPushService   |        |    Notification     |         |    NotificationService  |
+---------------------+        +---------------------+         +-------------------------+
| +send_notification()|  1     | -title: str         |         | +register_user()         |
+---------------------+ ------>| -message: str       |         | +unregister_user()       |
                                | -platform: str      | 1..*    | +send_notification()     |
                                | -recipient: str     +-------->| +process_event()         |
                                +---------------------+         +-------------------------+
          ^                               ^
          |                               |
          | implements                    | 1
+---------------------+        +---------------------+
|    IDeviceToken     |        |    IEmailService    |
+---------------------+        +---------------------+
| +get_device_token() |        | +send_email()       |
+---------------------+        +---------------------+
