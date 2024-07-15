Interfaces:

ITextPad: Defines methods for displaying, inserting, deleting, copying, pasting, undoing, and redoing text operations.

Models:
TextPad: Implements the ITextPad interface and manages the text content, clipboard, history for undo/redo, and provides error handling.

Implementation of Design Patterns
Command Pattern for Undo/Redo:
Implement the command pattern to handle undo/redo operations by storing actions in a history list and a redo stack.

Factory Pattern for Command Creation:
Use the factory pattern to create different command objects for each text operation (insert, delete, etc.).


Interface (ITextPad)
Defines methods to display, insert, delete, copy, paste, undo, and redo operations on text.
Manages content in memory using a list of strings.

Implementation (TextPad):
Implements undo/redo functionality using a command history stack.

Command Pattern:
Each operation (insert, delete, paste) records its action in a history stack.
Undo and redo operations modify the content based on the command history.

Error Handling:
Gracefully handles errors such as invalid line numbers or ranges.

Menu-Driven Interface:
Provides a user-friendly text menu for interacting with the TextPad.