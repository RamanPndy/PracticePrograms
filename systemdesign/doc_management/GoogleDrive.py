'''
Components
User: Represents a user with unique credentials.
File: Represents a file with metadata like name, size, owner, and collaborators.
Folder: Represents a folder that can contain files and other folders.
GoogleDriveSystem: Manages users, files, folders, permissions, and sharing.
'''

import uuid
from datetime import datetime
from typing import List, Dict

# Step 1: Define the User, File, and Folder
class User:
    def __init__(self, username: str, email: str):
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.email = email

class File:
    def __init__(self, name: str, owner: User):
        self.file_id = str(uuid.uuid4())
        self.name = name
        self.owner = owner
        self.created_at = datetime.now()
        self.modified_at = datetime.now()
        self.collaborators = []

    def add_collaborator(self, user: User):
        if user not in self.collaborators:
            self.collaborators.append(user)
            self.modified_at = datetime.now()

class Folder:
    def __init__(self, name: str, owner: User):
        self.folder_id = str(uuid.uuid4())
        self.name = name
        self.owner = owner
        self.created_at = datetime.now()
        self.modified_at = datetime.now()
        self.files = {}
        self.folders = {}
        self.collaborators = []

    def add_file(self, file: File):
        self.files[file.file_id] = file
        self.modified_at = datetime.now()

    def add_folder(self, folder: 'Folder'):
        self.folders[folder.folder_id] = folder
        self.modified_at = datetime.now()

    def add_collaborator(self, user: User):
        if user not in self.collaborators:
            self.collaborators.append(user)
            self.modified_at = datetime.now()

# Step 2: Define the GoogleDriveSystem
class GoogleDriveSystem:
    def __init__(self):
        self.users = {}
        self.files = {}
        self.folders = {}
        self.root_folders = {}

    def create_user(self, username: str, email: str) -> User:
        user = User(username, email)
        self.users[user.user_id] = user
        return user

    def create_file(self, name: str, owner_id: str) -> File:
        owner = self.users.get(owner_id)
        if not owner:
            raise ValueError("Owner not found")

        file = File(name, owner)
        self.files[file.file_id] = file
        return file

    def create_folder(self, name: str, owner_id: str) -> Folder:
        owner = self.users.get(owner_id)
        if not owner:
            raise ValueError("Owner not found")

        folder = Folder(name, owner)
        self.folders[folder.folder_id] = folder
        self.root_folders[folder.folder_id] = folder  # Add to root for simplicity
        return folder

    def add_file_to_folder(self, file_id: str, folder_id: str):
        file = self.files.get(file_id)
        folder = self.folders.get(folder_id)
        if not file or not folder:
            raise ValueError("File or Folder not found")

        folder.add_file(file)

    def add_folder_to_folder(self, child_folder_id: str, parent_folder_id: str):
        child_folder = self.folders.get(child_folder_id)
        parent_folder = self.folders.get(parent_folder_id)
        if not child_folder or not parent_folder:
            raise ValueError("Child Folder or Parent Folder not found")

        parent_folder.add_folder(child_folder)

    def add_collaborator_to_file(self, file_id: str, user_id: str):
        file = self.files.get(file_id)
        user = self.users.get(user_id)
        if not file or not user:
            raise ValueError("File or User not found")

        file.add_collaborator(user)

    def add_collaborator_to_folder(self, folder_id: str, user_id: str):
        folder = self.folders.get(folder_id)
        user = self.users.get(user_id)
        if not folder or not user:
            raise ValueError("Folder or User not found")

        folder.add_collaborator(user)

    def get_user_files(self, user_id: str) -> List[File]:
        user_files = []
        for file in self.files.values():
            if file.owner.user_id == user_id or user_id in [u.user_id for u in file.collaborators]:
                user_files.append(file)
        return user_files

    def get_user_folders(self, user_id: str) -> List[Folder]:
        user_folders = []
        for folder in self.folders.values():
            if folder.owner.user_id == user_id or user_id in [u.user_id for u in folder.collaborators]:
                user_folders.append(folder)
        return user_folders

# Create the Google Drive system
google_drive = GoogleDriveSystem()

# Create users
user1 = google_drive.create_user("Alice", "alice@example.com")
user2 = google_drive.create_user("Bob", "bob@example.com")

# Create files
file1 = google_drive.create_file("document1.txt", user1.user_id)
file2 = google_drive.create_file("image.jpg", user1.user_id)

# Create folders
folder1 = google_drive.create_folder("Work", user1.user_id)
folder2 = google_drive.create_folder("Photos", user1.user_id)

# Add files to folders
google_drive.add_file_to_folder(file1.file_id, folder1.folder_id)
google_drive.add_file_to_folder(file2.file_id, folder2.folder_id)

# Add folder to folder
folder3 = google_drive.create_folder("SubFolder", user1.user_id)
google_drive.add_folder_to_folder(folder3.folder_id, folder1.folder_id)

# Add collaborators
google_drive.add_collaborator_to_file(file1.file_id, user2.user_id)
google_drive.add_collaborator_to_folder(folder1.folder_id, user2.user_id)

# Get user files and folders
user1_files = google_drive.get_user_files(user1.user_id)
user1_folders = google_drive.get_user_folders(user1.user_id)

user2_files = google_drive.get_user_files(user2.user_id)
user2_folders = google_drive.get_user_folders(user2.user_id)

print("User1 Files:")
for file in user1_files:
    print(f"File: {file.name}")

print("\nUser1 Folders:")
for folder in user1_folders:
    print(f"Folder: {folder.name}")

print("\nUser2 Files:")
for file in user2_files:
    print(f"File: {file.name}")

print("\nUser2 Folders:")
for folder in user2_folders:
    print(f"Folder: {folder.name}")
