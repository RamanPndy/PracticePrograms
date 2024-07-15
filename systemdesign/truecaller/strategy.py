from systemdesign.truecaller.interface import ISpamDetectionStrategy

class BasicSpamDetection(ISpamDetectionStrategy):
    def isSpam(self, call):
        # Basic spam detection logic
        return call.callerInfo.spamScore > 5

class AdvancedSpamDetection(ISpamDetectionStrategy):
    def isSpam(self, call):
        # Advanced spam detection logic
        return call.callerInfo.spamScore > 3