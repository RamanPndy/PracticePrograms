class ApplicationState:
    instance = None

    def __init__(self) -> None:
        self.isLoggedIn = False

    @staticmethod
    def getAppState():
        if not ApplicationState.instance:
            ApplicationState.instance = ApplicationState()
        return ApplicationState.instance
    

appState1 = ApplicationState.getAppState()
appState1.isLoggedIn = True

appState2 = ApplicationState.getAppState()
print(appState1.isLoggedIn) #True
print(appState2.isLoggedIn) #True

'''
Ensures that a class has only one instance and provides a global point of access to it.
'''
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Usage
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
