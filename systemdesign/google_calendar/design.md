User, Event, Notification, and TimeSlot classes represent the core entities.
IObserver, ISubject, and IOverlapStrategy interfaces define the contract for observers, subjects, and the overlap strategy.
CalendarService manages events, notifies observers, and handles event creation and modification.
NotificationService sends notifications to users about important events.
AlarmService sets alarms for events.
OverlapService finds non-overlapping time slots using different strategies.
