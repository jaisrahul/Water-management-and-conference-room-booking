from datetime import datetime, timedelta

# Meeting room data
rooms = [
    {"name": "C-Contact", "capacity": 3},
    {"name": "S-Sharing", "capacity": 7},
    {"name": "T-Team", "capacity": 20}
]

# Buffer times
buffer_times = [("09:00", "09:15"),("13:15", "13:45"),("18:45", "19:00")]

# This Function to check if a given time overlaps with buffer times
def buffer_time_overlap(start_time, end_time):
    for buffer_start, buffer_end in buffer_times:
        buffer_start_time = datetime.strptime(buffer_start, "%H:%M")
        buffer_end_time = datetime.strptime(buffer_end, "%H:%M")
        if start_time < buffer_end_time and end_time > buffer_start_time:
            return True
    return False

# This Function to check if a room is available for booking
def room_available(room, start_time, end_time):
    if buffer_time_overlap(start_time, end_time):
        return False
    for booking in room["bookings"]:
        if start_time < booking["end_time"] and end_time > booking["start_time"]:
            return False
    return True

# This Function to book a room
def book_room(start_time, end_time, person_capacity):
    if person_capacity < 2 or person_capacity > 20:
        return "NO_VACANT_ROOM"

    start_time = datetime.strptime(start_time, "%H:%M")
    end_time = datetime.strptime(end_time, "%H:%M")

    for room in rooms:
        if room["capacity"] >= person_capacity and room_available(room, start_time, end_time):
            room["bookings"].append({"start_time": start_time, "end_time": end_time})
            return room["name"]
    
    return "NO_VACANT_ROOM"

# This Function to view available meeting rooms
def view_available_rooms(start_time, end_time):
    start_time = datetime.strptime(start_time, "%H:%M")
    end_time = datetime.strptime(end_time, "%H:%M")
    available_rooms = []
    for room in rooms:
        if room_available(room, start_time, end_time):
            available_rooms.append(room["name"])
    return " ".join(available_rooms)

# Initialize bookings for each room
for room in rooms:
    room["bookings"] = []

# Sample inputs and outputs
user_input = [
    ("VACANCY 10:00 12:00", "C-Contact S-Sharing T-Team"),
    ("BOOK 14:00 15:30 3", "C-Contact")
]

# Process inputs and print outputs
for command, expected_output in user_input:
    parts = command.split()
    action = parts[0]
    if action == "VACANCY":
        start_time, end_time = parts[1], parts[2]
        output = view_available_rooms(start_time, end_time)
    elif action == "BOOK":
        start_time, end_time, person_capacity = parts[1], parts[2], int(parts[3])
        output = book_room(start_time, end_time, person_capacity)
    else:
        output = "INCORRECT_INPUT"
    print(f"Input: {command}")
    print(f"Expected Output: {expected_output}")
    print(f"Actual Output: {output}")
    print("-" * 20)
