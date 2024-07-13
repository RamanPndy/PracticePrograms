from systemdesign.dropbox.impl import FileSystemManager

manager = FileSystemManager()
    
manager.add_folder("Documents", "ROOT")
manager.add_folder("Photos", "ROOT")
manager.add_file("resume.pdf", "Documents")
manager.add_file("vacation.jpg", "Photos")

manager.get_item("resume.pdf")  # Output: ROOT/Documents/resume.pdf
manager.get_item("vacation.jpg")  # Output: ROOT/Photos/vacation.jpg

manager.add_folder("Work", "Documents")
manager.move_item("resume.pdf", "Work")

manager.get_item("resume.pdf")  # Output: ROOT/Documents/Work/resume.pdf