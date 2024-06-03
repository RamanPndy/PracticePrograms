'''
Components
User: Represents a user with a unique identifier, username, email, and storage quota.
File: Represents a file with a unique identifier, name, size, owner, and storage location.
Folder: Represents a folder that can contain files and other folders.
DropboxSystem: Manages users, files, folders, storage allocation, and sharing.
'''

import uuid

# Step 1: Define the User, File, and Folder
class User:
    def __init__(self, user_id, username, email, storage_quota):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.storage_quota = storage_quota
        self.files = {}
        self.folders = {}

class File:
    def __init__(self, file_id, name, size, owner_id, location):
        self.file_id = file_id
        self.name = name
        self.size = size
        self.owner_id = owner_id
        self.location = location

class Folder:
    def __init__(self, folder_id, name, owner_id):
        self.folder_id = folder_id
        self.name = name
        self.owner_id = owner_id
        self.files = {}
        self.folders = {}

# Step 2: Define the DropboxSystem
class DropboxSystem:
    def __init__(self):
        self.users = {}
        self.files = {}
        self.folders = {}
        self.next_user_id = 1
        self.next_file_id = 1
        self.next_folder_id = 1

    def create_user(self, username, email, storage_quota):
        user_id = self.next_user_id
        user = User(user_id, username, email, storage_quota)
        self.users[user_id] = user
        self.next_user_id += 1
        return user

    def create_file(self, name, size, owner_id):
        file_id = self.next_file_id
        file_location = f"/{owner_id}/{name}"  # Example location path
        file = File(file_id, name, size, owner_id, file_location)
        self.files[file_id] = file
        owner = self.users.get(owner_id)
        if owner:
            owner.files[file_id] = file
        self.next_file_id += 1
        return file

    def create_folder(self, name, owner_id):
        folder_id = self.next_folder_id
        folder = Folder(folder_id, name, owner_id)
        self.folders[folder_id] = folder
        owner = self.users.get(owner_id)
        if owner:
            owner.folders[folder_id] = folder
        self.next_folder_id += 1
        return folder

    def upload_file_to_folder(self, file_id, folder_id):
        file = self.files.get(file_id)
        folder = self.folders.get(folder_id)
        if file and folder:
            folder.files[file_id] = file

    def get_user_files(self, user_id):
        user = self.users.get(user_id)
        if user:
            return user.files.values()
        return []

    def get_user_folders(self, user_id):
        user = self.users.get(user_id)
        if user:
            return user.folders.values()
        return []

dropbox_system = DropboxSystem()

# Create users
user1 = dropbox_system.create_user("Alice", "alice@example.com", 1024)  # 1024 MB storage quota
user2 = dropbox_system.create_user("Bob", "bob@example.com", 2048)  # 2048 MB storage quota

# Create files
file1 = dropbox_system.create_file("document1.txt", 50, user1.user_id)  # Size in MB
file2 = dropbox_system.create_file("image.jpg", 100, user1.user_id)

# Create folders
folder1 = dropbox_system.create_folder("Work", user1.user_id)
folder2 = dropbox_system.create_folder("Photos", user1.user_id)

# Upload files to folders
dropbox_system.upload_file_to_folder(file1.file_id, folder1.folder_id)
dropbox_system.upload_file_to_folder(file2.file_id, folder2.folder_id)

# Get user's files and folders
user1_files = dropbox_system.get_user_files(user1.user_id)
user1_folders = dropbox_system.get_user_folders(user1.user_id)

for file in user1_files:
    print(f"User {user1.username} has file: {file.name}")

for folder in user1_folders:
    print(f"User {user1.username} has folder: {folder.name}")
