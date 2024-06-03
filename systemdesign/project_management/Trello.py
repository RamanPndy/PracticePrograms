from enum import Enum

class Status(Enum):
    TODO = 1

class User:
    '''
    Represents a user with attributes like user ID, name, and email.
    '''
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

class Card:
    '''
    Represents a task with attributes like card ID, title, description, assigned user, and status.
    '''
    def __init__(self, card_id, title, description):
        self.card_id = card_id
        self.title = title
        self.description = description
        self.assigned_user = None
        self.status = Status.TODO  # Status can be 'To Do', 'In Progress', 'Done'

    def assign_user(self, user):
        self.assigned_user = user

    def change_status(self, status):
        self.status = status

class List:
    '''
    Represents a list of cards with attributes like list ID, name, and a list of cards.
    '''
    def __init__(self, list_id, name):
        self.list_id = list_id
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card_id):
        self.cards = [card for card in self.cards if card.card_id != card_id]

class Board:
    '''
    Represents a board with attributes like board ID, name, and a list of lists.
    '''
    def __init__(self, board_id, name):
        self.board_id = board_id
        self.name = name
        self.lists = []

    def add_list(self, list_obj):
        self.lists.append(list_obj)

    def remove_list(self, list_id):
        self.lists = [lst for lst in self.lists if lst.list_id != list_id]

class ProjectManagementApp:
    '''
    Manages boards, users, and provides functionalities to manage the entire application.
    '''
    def __init__(self):
        self.users = {}
        self.boards = {}

    def create_user(self, user_id, name, email):
        user = User(user_id, name, email)
        self.users[user_id] = user
        return user

    def create_board(self, board_id, name):
        board = Board(board_id, name)
        self.boards[board_id] = board
        return board

    def create_list(self, board_id, list_id, name):
        board = self.boards.get(board_id)
        if not board:
            raise ValueError("Board not found")
        lst = List(list_id, name)
        board.add_list(lst)
        return lst

    def create_card(self, board_id, list_id, card_id, title, description):
        board = self.boards.get(board_id)
        if not board:
            raise ValueError("Board not found")
        lst = next((lst for lst in board.lists if lst.list_id == list_id), None)
        if not lst:
            raise ValueError("List not found")
        card = Card(card_id, title, description)
        lst.add_card(card)
        return card

    def assign_user_to_card(self, board_id, list_id, card_id, user_id):
        user = self.users.get(user_id)
        if not user:
            raise ValueError("User not found")
        board = self.boards.get(board_id)
        if not board:
            raise ValueError("Board not found")
        lst = next((lst for lst in board.lists if lst.list_id == list_id), None)
        if not lst:
            raise ValueError("List not found")
        card = next((card for card in lst.cards if card.card_id == card_id), None)
        if not card:
            raise ValueError("Card not found")
        card.assign_user(user)
        return card

    def move_card(self, board_id, from_list_id, to_list_id, card_id):
        board = self.boards.get(board_id)
        if not board:
            raise ValueError("Board not found")
        from_list = next((lst for lst in board.lists if lst.list_id == from_list_id), None)
        to_list = next((lst for lst in board.lists if lst.list_id == to_list_id), None)
        if not from_list or not to_list:
            raise ValueError("List not found")
        card = next((card for card in from_list.cards if card.card_id == card_id), None)
        if not card:
            raise ValueError("Card not found")
        from_list.remove_card(card_id)
        to_list.add_card(card)
        return card

# Initialize the project management application
app = ProjectManagementApp()

# Create users
user1 = app.create_user(1, "Alice", "alice@example.com")
user2 = app.create_user(2, "Bob", "bob@example.com")

# Create a board
board = app.create_board(1, "Project Alpha")

# Create lists
todo_list = app.create_list(1, 1, "To Do")
in_progress_list = app.create_list(1, 2, "In Progress")
done_list = app.create_list(1, 3, "Done")

# Create cards
card1 = app.create_card(1, 1, 1, "Design the UI", "Create wireframes for the project")
card2 = app.create_card(1, 1, 2, "Set up database", "Install and configure the database")

# Assign user to a card
app.assign_user_to_card(1, 1, 1, 1)

# Move card from "To Do" list to "In Progress" list
app.move_card(1, 1, 2, 1)

# Display the structure of the board
for lst in board.lists:
    print(f"List: {lst.name}")
    for card in lst.cards:
        assigned_user = card.assigned_user.name if card.assigned_user else "Unassigned"
        print(f"  Card: {card.title}, Assigned to: {assigned_user}, Status: {card.status}")
