+-------------------+         +---------------------+
| UserService       |         | ContactService      |
|-------------------|         |---------------------|
| +register_user()  |         | +sync_contacts()    |
| +login_user()     |         | +get_contacts()     |
| +update_profile() |         +---------------------+
+-------------------+                  |
        |                               |
        |                               |
+-----------------------+         +-----------------+
| UserServiceImpl       |         | ContactServiceImpl |
|-----------------------|         |-----------------|
| +register_user()      |         | +sync_contacts()|
| +login_user()         |         | +get_contacts() |
| +update_profile()     |         +-----------------+
+-----------------------+                  |
        |                               |
        |                               |
+-----------------+             +---------------+
| User            |             | Contact       |
|-----------------|             |---------------|
| user_id: str    |             | user_id: str  |
| name: str       |             | contacts: list|
| phone_number: str|             +---------------+
| password: str   |
| email: str      |
+-----------------+

+---------------------------------+
|           ICallerIDService      |
|---------------------------------|
| +identifyCaller(phoneNumber: String): CallerInfo |
+---------------------------------+

+---------------------------------+
|           CallerIDService       |
|---------------------------------|
| -subscribers: List<ISubscriber> |
|---------------------------------|
| +identifyCaller(phoneNumber: String): CallerInfo |
| +subscribe(subscriber: ISubscriber): void |
| +unsubscribe(subscriber: ISubscriber): void |
| +notifySubscribers(info: CallerInfo): void |
+---------------------------------+

+---------------------------------+
|           ISubscriber           |
|---------------------------------|
| +update(info: CallerInfo): void |
+---------------------------------+

+---------------------------------+
|           CallLogger            |
|---------------------------------|
| +update(info: CallerInfo): void |
+---------------------------------+

+---------------------------------+
|           CallBlocker           |
|---------------------------------|
| +update(info: CallerInfo): void |
+---------------------------------+

+---------------------------------+
|           ISpamDetectionStrategy|
|---------------------------------|
| +isSpam(call: CallInfo): Boolean |
+---------------------------------+

+---------------------------------+
|           BasicSpamDetection    |
|---------------------------------|
| +isSpam(call: CallInfo): Boolean |
+---------------------------------+

+---------------------------------+
|           AdvancedSpamDetection |
|---------------------------------|
| +isSpam(call: CallInfo): Boolean |
+---------------------------------+

+---------------------------------+
|           CallerInfo            |
|---------------------------------|
| -phoneNumber: String            |
| -name: String                   |
| -spamScore: int                 |
|---------------------------------|
| +getPhoneNumber(): String       |
| +getName(): String              |
| +getSpamScore(): int            |
+---------------------------------+

+---------------------------------+
|           CallInfo              |
|---------------------------------|
| -callerInfo: CallerInfo         |
| -time: Date                     |
| -duration: int                  |
+---------------------------------+
