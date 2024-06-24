from designpatterns.SOLID.dependency_inversion.impl import ConsoleLogger, FileLogger
from designpatterns.SOLID.dependency_inversion.service import UserService

'''
The Dependency Inversion Principle (DIP) is one of the SOLID principles of object-oriented design. 
It states that high-level modules should not depend on low-level modules but both should depend on abstractions. 
Also, abstractions should not depend on details; details should depend on abstractions.

Explanation
Abstraction: We created an ILogger interface that declares the log method.
Details: We implemented the ILogger interface in ConsoleLogger and FileLogger classes.
High-level Module: The UserService class depends on the ILogger interface instead of concrete implementations. 
This makes it flexible and allows us to change the logging mechanism without modifying the UserService class.

By following the Dependency Inversion Principle, the high-level UserService module does not depend on low-level Logger modules. 
Both depend on the abstraction ILogger, making the design more flexible and maintainable.
'''
if __name__ == "__main__":
    console_logger = ConsoleLogger()
    file_logger = FileLogger("log.txt")

    user_service_console = UserService(console_logger)
    user_service_file = UserService(file_logger)

    user_service_console.add_user("JohnDoe")
    user_service_file.add_user("JaneDoe")
