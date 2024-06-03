'''
Components
User: Represents a user of the system with unique credentials.
File: Represents a file with metadata such as name, size, owner, and access permissions.
Folder: Represents a folder that can contain files and other folders.
FileSharingSystem: Manages users, files, folders, permissions, and sharing.
'''

import uuid
from datetime import datetime
from typing import List, Dict, Optional

# Step 1: Define the User, File, and Folder
class User:
    def __init__(self, username: str, email: str):
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.email = email

class File:
    def __init__(self, name: str, owner: User, size: int, content: str):
        self.file_id = str(uuid.uuid4())
        self.name = name
        self.owner = owner
        self.size = size
        self.content = content
        self.created_at = datetime.now()
        self.modified_at = datetime.now()
        self.permissions = {owner.user_id: "owner"}  # owner has full permissions
        self.shared_with = {}

    def add_permission(self, user: User, permission: str):
        self.permissions[user.user_id] = permission
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
        self.permissions = {owner.user_id: "owner"}  # owner has full permissions

    def add_file(self, file: File):
        self.files[file.file_id] = file
        self.modified_at = datetime.now()

    def add_folder(self, folder: 'Folder'):
        self.folders[folder.folder_id] = folder
        self.modified_at = datetime.now()

    def add_permission(self, user: User, permission: str):
        self.permissions[user.user_id] = permission
        self.modified_at = datetime.now()

# Step 2: Define the FileSharingSystem
class FileSharingSystem:
    def __init__(self):
        self.users = {}
        self.files = {}

    def create_user(self, username: str, email: str) -> User:
        user = User(username, email)
        self.users[user.user_id] = user
        return user

    def upload_file(self, name: str, owner_id: str, size: int) -> File:
        owner = self.users.get(owner_id)
        if not owner:
            raise ValueError("Owner not found")

        file = File(name, owner, size)
        self.files[file.file_id] = file
        return file

    def share_file(self, file_id: str, owner_id: str, user_id: str, permission: str):
        file = self.files.get(file_id)
        owner = self.users.get(owner_id)
        user = self.users.get(user_id)

        if not file or not owner or not user:
            raise ValueError("File, Owner or User not found")

        if file.owner.user_id != owner.user_id:
            raise PermissionError("Only the owner can share the file")

        file.shared_with[user.user_id] = permission
        file.modified_at = datetime.now()

    def download_file(self, file_id: str, user_id: str) -> File:
        file = self.files.get(file_id)
        user = self.users.get(user_id)

        if not file or not user:
            raise ValueError("File or User not found")

        if file.owner.user_id != user.user_id and user.user_id not in file.shared_with:
            raise PermissionError("Access denied")

        return file

    def get_shared_files(self, user_id: str) -> List[File]:
        user = self.users.get(user_id)
        if not user:
            raise ValueError("User not found")

        shared_files = []
        for file in self.files.values():
            if user.user_id in file.shared_with:
                shared_files.append(file)
        return shared_files

# Create the file sharing system
file_sharing_system = FileSharingSystem()

# Create users
user1 = file_sharing_system.create_user("Alice", "alice@example.com")
user2 = file_sharing_system.create_user("Bob", "bob@example.com")

# Upload files
file1 = file_sharing_system.upload_file("document1.txt", user1.user_id, 1024)
file2 = file_sharing_system.upload_file("image.jpg", user1.user_id, 2048)

# Share file with permissions
file_sharing_system.share_file(file1.file_id, user1.user_id, user2.user_id, "read")

# Download file
try:
    file = file_sharing_system.download_file(file1.file_id, user2.user_id)
    print(f"Downloaded File: {file.name}")
except PermissionError as e:
    print(e)

# Get shared files
shared_files = file_sharing_system.get_shared_files(user2.user_id)
for file in shared_files:
    print(f"Shared File: {file.name}")
