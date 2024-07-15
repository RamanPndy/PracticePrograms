from systemdesign.truecaller.interface import SpamService

class SpamServiceSingleton:
    _instance = None

    @staticmethod
    def get_instance():
        if SpamServiceSingleton._instance is None:
            SpamServiceSingleton._instance = SpamService()
        return SpamServiceSingleton._instance
