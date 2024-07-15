Log and LogType models represent the core log entries and their types.
IObserver, ISubject, ILogFilterStrategy, and ILogSearchStrategy interfaces define the contract for observers, subjects, and different filtering/searching strategies.
LogTrackerService manages logs and notifies observers of new logs.
LogFilterService and LogSearchService use different strategies to filter and search logs respectively.