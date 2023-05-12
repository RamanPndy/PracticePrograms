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