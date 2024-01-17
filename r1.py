import random

# Define the representation for a solution to the scheduling problem
def create_schedule(courses, rooms, timeslots):
    # Shuffle the rooms and timeslots to add some randomness to the schedule
    random.shuffle(rooms)
    random.shuffle(timeslots)
    # Create a list to store the schedule
    schedule = []
    # Iterate over each course
    for course in courses:
        # Assign the next available room and timeslot to the course
        room = rooms[len(schedule) % len(rooms)]
        timeslot = timeslots[len(schedule) % len(timeslots)]
        # Add the course, room, and timeslot to the schedule
        schedule.append((course, room, timeslot))
    # Return the schedule
    return schedule
