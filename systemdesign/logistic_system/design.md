Location, Stakeholder, Container, Shipment, and Order classes represent the core entities.
IObserver, ISubject, and ITrackingService interfaces define the contract for observers, subjects, and the tracking service.
LogisticService manages shipments and orders, and notifies observers of updates.
TrackingService provides real-time location tracking for containers.
ETAService calculates the estimated time of arrival for shipments.
NotificationService sends notifications to stakeholders about important events.