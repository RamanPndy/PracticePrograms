'''
Avoids coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. 
Chain the receiving objects and pass the request along the chain until an object handles it.
'''
class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        if self.successor:
            self.successor.handle(request)

class ConcreteHandler1(Handler):
    def handle(self, request):
        if request == "R1":
            print("ConcreteHandler1 handled request")
        else:
            super().handle(request)

class ConcreteHandler2(Handler):
    def handle(self, request):
        if request == "R2":
            print("ConcreteHandler2 handled request")
        else:
            super().handle(request)
