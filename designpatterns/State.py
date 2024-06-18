'''
Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.
'''
class State:
    def handle(self, context):
        pass

class ConcreteStateA(State):
    def handle(self, context):
        context.state = ConcreteStateB()

class ConcreteStateB(State):
    def handle(self, context):
        context.state = ConcreteStateA()

class Context:
    def __init__(self, state):
        self.state = state

    def request(self):
        self.state.handle(self)

# Usage
context = Context(ConcreteStateA())
context.request()  # Switch to State B
context.request()  # Switch to State A
