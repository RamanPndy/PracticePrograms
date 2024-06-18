'''
Provides an interface for creating families of related or dependent objects without specifying their concrete classes.
'''
class Button:
    def render(self):
        pass

class Checkbox:
    def render(self):
        pass

class WindowsButton(Button):
    def render(self):
        return "Render a Windows button"

class WindowsCheckbox(Checkbox):
    def render(self):
        return "Render a Windows checkbox"

class MacButton(Button):
    def render(self):
        return "Render a Mac button"

class MacCheckbox(Checkbox):
    def render(self):
        return "Render a Mac checkbox"

class GUIFactory:
    def create_button(self):
        pass

    def create_checkbox(self):
        pass

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()
