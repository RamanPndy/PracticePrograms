class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f"File: {self.name} (Size: {self.size} bytes)"


class Directory:
    def __init__(self, name):
        self.name = name
        self.contents = []

    def add_item(self, item):
        self.contents.append(item)

    def remove_item(self, item):
        if item in self.contents:
            self.contents.remove(item)

    def get_total_size(self):
        total_size = 0
        for item in self.contents:
            if isinstance(item, File):
                total_size += item.size
            elif isinstance(item, Directory):
                total_size += item.get_total_size()
        return total_size

    def __str__(self):
        return f"Directory: {self.name}\nContents: {', '.join(str(item) for item in self.contents)}"


# Usage example
file1 = File("file1.txt", 1024)
file2 = File("file2.jpg", 2048)
file3 = File("file3.docx", 512)

directory1 = Directory("Folder 1")
directory1.add_item(file1)
directory1.add_item(file2)

directory2 = Directory("Folder 2")
directory2.add_item(file3)

root = Directory("Root")
root.add_item(directory1)
root.add_item(directory2)

print(root.get_total_size())
print(directory1)
