# Example usage
from systemdesign.log_tracking_system.interface import IObserver
from systemdesign.log_tracking_system.models import Log, LogType
from systemdesign.log_tracking_system.services import LogFilterService, LogSearchService, LogTrackerService
from systemdesign.log_tracking_system.strategy import LogMessageSearchStrategy, LogTypeFilterStrategy

log_tracker_service = LogTrackerService()

# Register observers (in this case, just printing logs to console)
class PrintObserver(IObserver):
    def update(self, log: Log):
        print(log)

print_observer = PrintObserver()
log_tracker_service.register_observer(print_observer)

# Add logs
log_tracker_service.add_log(Log("System started", LogType.INFO))
log_tracker_service.add_log(Log("An error occurred", LogType.ERROR))
log_tracker_service.add_log(Log("Debugging info", LogType.DEBUG))

# Filter logs by type
filter_service = LogFilterService(LogTypeFilterStrategy(LogType.ERROR))
filtered_logs = filter_service.filter_logs(log_tracker_service.get_logs())
print("Filtered Logs:", filtered_logs)

# Search logs by message
search_service = LogSearchService(LogMessageSearchStrategy())
searched_logs = search_service.search_logs(log_tracker_service.get_logs(), "error")
print("Searched Logs:", searched_logs)
