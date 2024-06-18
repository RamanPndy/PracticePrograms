'''
Encapsulates a request as an object, thereby allowing for parameterization of clients with different requests, queuing of 
requests, and logging the requests.
'''
class Command:
    def execute(self):
        pass

class Light:
    def on(self):
        print("Light is on")

    def off(self):
        print("Light is off")

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

# Usage
light = Light()
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

remote = RemoteControl()
remote.set_command(light_on)
remote.press_button()  # Light is on

remote.set_command(light_off)
remote.press_button()  # Light is off
