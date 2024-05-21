from enum import Enum
class Status(Enum):
    BOOKED, CONFIRMED, CANCELLED = 1,2,3
class User:
    def __init__(self, user_id, username, email, password, role):
        self.id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.role = role

class Service:
    def __init__(self, service_id, name, description, duration, provider_id, availability):
        self.id = service_id
        self.name = name
        self.description = description
        self.duration = duration
        self.provider_id = provider_id
        self.availability = availability

class Appointment:
    def __init__(self, appointment_id, customer_id, service_id, date_time, status):
        self.id = appointment_id
        self.customer_id = customer_id
        self.service_id = service_id
        self.date_time = date_time
        self.status = status

class AppointmentBookingSystem:
    def __init__(self):
        self.users = {}  # user_id -> User
        self.services = {}  # service_id -> Service
        self.appointments = {}  # appointment_id -> Appointment

    def create_user(self, user_id, username, email, password, role):
        user = User(user_id, username, email, password, role)
        self.users[user_id] = user
        return user

    def create_service(self, service_id, name, description, duration, provider_id, availability):
        service = Service(service_id, name, description, duration, provider_id, availability)
        self.services[service_id] = service
        return service

    def book_appointment(self, customer_id, service_id, date_time):
        appointment_id = len(self.appointments) + 1
        appointment = Appointment(appointment_id, customer_id, service_id, date_time, Status.BOOKED)
        self.appointments[appointment_id] = appointment
        return appointment

    def confirm_appointment(self, appointment_id):
        appointment = self.appointments.get(appointment_id)
        if appointment:
            appointment.status = Status.CONFIRMED
            return True
        return False

    def cancel_appointment(self, appointment_id):
        appointment = self.appointments.get(appointment_id)
        if appointment:
            appointment.status = Status.CANCELLED
            return True
        return False

# Example usage
booking_system = AppointmentBookingSystem()

customer = booking_system.create_user(1, "JohnDoe", "john@example.com", "password", "Customer")
provider = booking_system.create_user(2, "JaneSmith", "jane@example.com", "password", "Service Provider")

service = booking_system.create_service(1, "Haircut", "Basic haircut", 60, provider.user_id, "Mon-Fri, 9am-5pm")

appointment = booking_system.book_appointment(customer.user_id, service.service_id, "2023-08-20 10:00")
booking_system.confirm_appointment(appointment.appointment_id)
booking_system.cancel_appointment(appointment.appointment_id)
