from designpatterns.SOLID.dependency_inversion.interface import ILogger

class ConsoleLogger(ILogger):
    def log(self, message):
        print(f"Log message: {message}")

class FileLogger(ILogger):
    def __init__(self, filename):
        self.filename = filename

    def log(self, message):
        with open(self.filename, 'a') as f:
            f.write(f"Log message: {message}\n")
