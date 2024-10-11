school bus tracking system
FR
1. it will move on only 1 route which will cover some areas
2. stopages/pick up location are already known
3. record start and end time
4. keep a record for absent
5. for each pick up location there is a timeout
6. real time lat/long of bus -> gps -> calculate the exact coordinates and transmit it
7. console panel where it will show bus location

8. parent should know pick/drop time of student
9. school authority should know when trip start/end
10. in real time total how many students are on boarded on bus
11. parent should also know real time location of the bus


Bus:
    id, school, capacity, currentTotalStudents, student_ids
    get_location()
    get
    onboard()
    send_notification()

Parent
    id
Student
    id, parent_id

BusTrip
    id, start_time, end_time

StudentTrip
    student_id, bus_id, pickup time, drop time


Notification service -> which will notify parents/school authority