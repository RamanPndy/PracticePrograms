from systemdesign.textpad.impl import TextPad

def menu():
    textpad = TextPad()
    while True:
        print("\nTextPad Menu")
        print("1. Display content")
        print("2. Display from line n to m")
        print("3. Insert text at line n")
        print("4. Delete line n")
        print("5. Delete from line n to m")
        print("6. Copy from line n to m")
        print("7. Paste at line n")
        print("8. Undo last command")
        print("9. Redo last command")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            textpad.display()
        elif choice == '2':
            n = int(input("Enter line n: "))
            m = int(input("Enter line m: "))
            textpad.display(n, m)
        elif choice == '3':
            n = int(input("Enter line n: "))
            text = input("Enter text: ")
            textpad.insert(n, text)
        elif choice == '4':
            n = int(input("Enter line n: "))
            textpad.delete(n)
        elif choice == '5':
            n = int(input("Enter line n: "))
            m = int(input("Enter line m: "))
            textpad.delete(n, m)
        elif choice == '6':
            n = int(input("Enter line n: "))
            m = int(input("Enter line m: "))
            textpad.copy(n, m)
        elif choice == '7':
            n = int(input("Enter line n: "))
            textpad.paste(n)
        elif choice == '8':
            textpad.undo()
        elif choice == '9':
            textpad.redo()
        elif choice == '0':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()
