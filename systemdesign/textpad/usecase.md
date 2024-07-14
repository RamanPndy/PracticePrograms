Display Content:
Use Case: Display the entire content or a specific range of lines.
Flow: display() or display(n, m) methods are called to show the content.

Insert Text:
Use Case: Insert text at a specific line.
Flow: insert(n, text) method is called to insert text at line n.

Delete Line(s):
Use Case: Delete a specific line or a range of lines.
Flow: delete(n) or delete(n, m) methods are called to delete lines.

Copy and Paste:
Use Case: Copy content to the clipboard and paste it at a specific line.
Flow: copy(n, m) copies content, and paste(n) pastes content at line n.

Undo and Redo:
Use Case: Undo the last command or redo the last undone command.
Flow: undo() and redo() methods handle these operations using the command pattern.
