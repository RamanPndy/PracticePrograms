from systemdesign.textpad.interface import ITextPad

class TextPad(ITextPad):
    def __init__(self):
        self.content = []
        self.clipboard = ""
        self.history = []
        self.redo_stack = []

    def display(self, n: int = None, m: int = None):
        try:
            if n is not None and m is not None:
                for i in range(n-1, m):
                    print(self.content[i])
            else:
                for line in self.content:
                    print(line)
        except IndexError:
            print("Invalid line range")

    def insert(self, n: int, text: str):
        try:
            self.content.insert(n-1, text)
            self.history.append(('insert', n-1, text))
            self.redo_stack.clear()
        except IndexError:
            print("Invalid line number")

    def delete(self, n: int, m: int = None):
        try:
            if m is not None:
                deleted = self.content[n-1:m]
                del self.content[n-1:m]
                self.history.append(('delete', n-1, deleted))
            else:
                deleted = self.content.pop(n-1)
                self.history.append(('delete', n-1, [deleted]))
            self.redo_stack.clear()
        except IndexError:
            print("Invalid line range")

    def copy(self, n: int, m: int):
        try:
            self.clipboard = "\n".join(self.content[n-1:m])
        except IndexError:
            print("Invalid line range")

    def paste(self, n: int):
        try:
            lines = self.clipboard.split("\n")
            for i, line in enumerate(lines):
                self.content.insert(n-1+i, line)
            self.history.append(('paste', n-1, lines))
            self.redo_stack.clear()
        except IndexError:
            print("Invalid line number")

    def undo(self):
        if not self.history:
            print("No actions to undo")
            return
        action = self.history.pop()
        self.redo_stack.append(action)
        action_type, n, data = action
        if action_type == 'insert':
            del self.content[n]
        elif action_type == 'delete':
            for i, line in enumerate(data):
                self.content.insert(n+i, line)
        elif action_type == 'paste':
            del self.content[n:n+len(data)]

    def redo(self):
        if not self.redo_stack:
            print("No actions to redo")
            return
        action = self.redo_stack.pop()
        self.history.append(action)
        action_type, n, data = action
        if action_type == 'insert':
            self.content.insert(n, data)
        elif action_type == 'delete':
            del self.content[n:n+len(data)]
        elif action_type == 'paste':
            for i, line in enumerate(data):
                self.content.insert(n+i, line)
