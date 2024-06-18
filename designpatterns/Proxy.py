'''
Provides a surrogate or placeholder for another object to control access to it.
'''
class RealSubject:
    def request(self):
        return "RealSubject request"

class Proxy:
    def __init__(self, real_subject):
        self.real_subject = real_subject

    def request(self):
        return f"Proxy: {self.real_subject.request()}"

real_subject = RealSubject()
proxy = Proxy(real_subject)
print(proxy.request())  # Output: Proxy: RealSubject request
