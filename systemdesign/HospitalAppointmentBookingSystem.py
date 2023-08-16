from datetime import datetime

class User:
    def __init__(self, user_id, username, role):
        self.user_id = user_id
        self.username = username
        self.role = role

class Doctor(User):
    def __init__(self, user_id, username, speciality):
        super().__init__(user_id, username, "Doctor")
        self.speciality = speciality

class Patient(User):
    def __init__(self, user_id, username):
        super().__init__(user_id, username, "Patient")

class Appointment:
    def __init__(self, appointment_id, doctor_id, patient_id, date_time, status):
        self.appointment_id = appointment_id
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.date_time = date_time
        self.status = status

class AppointmentBookingSystem:
    def __init__(self):
        self.doctors = {}  # doctor_id -> Doctor
        self.patients = {}  # patient_id -> Patient
        self.appointments = {}  # appointment_id -> Appointment

    def create_doctor(self, doctor_id, username, speciality):
        doctor = Doctor(doctor_id, username, speciality)
        self.doctors[doctor_id] = doctor
        return doctor

    def create_patient(self, patient_id, username):
        patient = Patient(patient_id, username)
        self.patients[patient_id] = patient
        return patient

    def book_appointment(self, doctor_id, patient_id, date_time):
        appointment_id = len(self.appointments) + 1
        appointment = Appointment(appointment_id, doctor_id, patient_id, date_time, "Booked")
        self.appointments[appointment_id] = appointment
        return appointment

    def confirm_appointment(self, appointment_id):
        appointment = self.appointments.get(appointment_id)
        if appointment:
            appointment.status = "Confirmed"
            return True
        return False

# Example usage
booking_system = AppointmentBookingSystem()

doctor = booking_system.create_doctor(1, "DrSmith", "Cardiologist")
patient = booking_system.create_patient(1, "JohnDoe")

appointment_time = datetime(2023, 8, 20, 14, 30)
appointment = booking_system.book_appointment(doctor.user_id, patient.user_id, appointment_time)
booking_system.confirm_appointment(appointment.appointment_id)
