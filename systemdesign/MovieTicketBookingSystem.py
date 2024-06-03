'''
Components
User: Represents a user with unique credentials and personal information.
Movie: Represents a movie with details like title, genre, duration, and showtimes.
Booking: Represents a booking made by a user for a specific movie and showtime.
Seat: Represents a seat in a theater, which can be booked or available.
TicketingSystem: Manages users, movies, bookings, seats, and payment processing.
'''
# Step 1: Define the User and Movie Classes
import uuid
from datetime import datetime, timedelta

class User:
    def __init__(self, username: str, email: str, password: str):
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.email = email
        self.password = password

class Movie:
    def __init__(self, title: str, genre: str, duration: int):
        self.movie_id = str(uuid.uuid4())
        self.title = title
        self.genre = genre
        self.duration = duration
        self.showtimes = []
    
    def add_showtime(self, showtime: datetime):
        self.showtimes.append(showtime)

# Step 2: Define the Booking and Seat Classes
class Booking:
    def __init__(self, user: User, movie: Movie, showtime: datetime, seats: List[str]):
        self.booking_id = str(uuid.uuid4())
        self.user = user
        self.movie = movie
        self.showtime = showtime
        self.seats = seats
        self.booking_time = datetime.now()

class Seat:
    def __init__(self, seat_number: str, is_booked: bool = False):
        self.seat_number = seat_number
        self.is_booked = is_booked

# Step 3: Define the TicketingSystem
class TicketingSystem:
    def __init__(self):
        self.users = {}
        self.movies = {}
        self.bookings = {}
        self.seats = {}

    def register_user(self, username: str, email: str, password: str) -> User:
        user = User(username, email, password)
        self.users[user.user_id] = user
        return user

    def add_movie(self, title: str, genre: str, duration: int, showtimes: List[datetime]):
        movie = Movie(title, genre, duration)
        for showtime in showtimes:
            movie.add_showtime(showtime)
        self.movies[movie.movie_id] = movie

    def book_ticket(self, user_id: str, movie_id: str, showtime: datetime, seats: List[str]):
        user = self.users.get(user_id)
        movie = self.movies.get(movie_id)
        if not user or not movie:
            raise ValueError("User or Movie not found")

        for seat_number in seats:
            seat = self.seats.get(seat_number)
            if seat and seat.is_booked:
                raise ValueError(f"Seat {seat_number} is already booked")
            elif not seat:
                seat = Seat(seat_number)
                self.seats[seat_number] = seat

        booking = Booking(user, movie, showtime, seats)
        self.bookings[booking.booking_id] = booking
        for seat_number in seats:
            self.seats[seat_number].is_booked = True
        return booking

ticketing_system = TicketingSystem()

# Register Users
user1 = ticketing_system.register_user("Alice", "alice@example.com", "password1")
user2 = ticketing_system.register_user("Bob", "bob@example.com", "password2")

# Add Movies
movie1 = ticketing_system.add_movie("The Matrix", "Action", 150, [datetime.now() + timedelta(days=1, hours=18)])
movie2 = ticketing_system.add_movie("Inception", "Sci-Fi", 180, [datetime.now() + timedelta(days=1, hours=20)])

# Book Tickets
booking1 = ticketing_system.book_ticket(user1.user_id, movie1.movie_id, movie1.showtimes[0], ["A1", "A2"])
booking2 = ticketing_system.book_ticket(user2.user_id, movie2.movie_id, movie2.showtimes[0], ["B1", "B2"])

print(f"Booking 1 ID: {booking1.booking_id}, Seats: {booking1.seats}")
print(f"Booking 2 ID: {booking2.booking_id}, Seats: {booking2.seats}")
