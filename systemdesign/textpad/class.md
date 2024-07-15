+-------------------+
|   ITextPad        |
+-------------------+
| +display()        |
| +display(n, m)    |
| +insert(n, text)  |
| +delete(n)        |
| +delete(n, m)     |
| +copy(n, m)       |
| +paste(n)         |
| +undo()           |
| +redo()           |
+-------------------+
         ^
         |
+-------------------+
|   TextPad         |
+-------------------+
| -content: list    |
| -clipboard: str   |
| -history: list    |
| -redo_stack: list |
+-------------------+
| +display()        |
| +display(n, m)    |
| +insert(n, text)  |
| +delete(n)        |
| +delete(n, m)     |
| +copy(n, m)       |
| +paste(n)         |
| +undo()           |
| +redo()           |
+-------------------+
