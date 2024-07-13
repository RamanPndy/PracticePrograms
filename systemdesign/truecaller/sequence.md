User          CallerIDService           CallLogger           CallBlocker
 |                 |                         |                   |
 |---identifyCaller()--->|                   |                   |
 |                 |--notifySubscribers(info)--->|                   |
 |                 |                         |                   |
 |                 |<------------------------|---update(info)----|
 |                 |                         |                   |
 |                 |                         |                   |
 |                 |<--------------------------------update(info)|
 |                 |                         |                   |
