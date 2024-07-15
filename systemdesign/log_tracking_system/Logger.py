import datetime

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file

    def log(self, level, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level.upper()}] {message}\n"
        with open(self.log_file, 'a') as f:
            f.write(log_entry)

    def debug(self, message):
        self.log('debug', message)

    def info(self, message):
        self.log('info', message)

    def warning(self, message):
        self.log('warning', message)

    def error(self, message):
        self.log('error', message)

    def critical(self, message):
        self.log('critical', message)

# Example usage:
logger = Logger("app.log")
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
