import sys
from datetime import datetime

class StudyRoomBookingSystem:

    def __init__(self):
        self.rooms = [None] * 10
        self.users = {}
        self.booked_rooms = {}

    def register_user(self):
        print("Register a new user")
        username = input("Enter username: ")
        password = input("Enter password: ")
        self.users[username] = password
        print("Registration successful!")

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            print(f"Welcome back, {username}!")
            return True
        else:
            print("Invalid username or password!")
            return False

    def show_available_rooms(self):
        print("\nAvailable Rooms:")
        for i in range(10):
            if self.rooms[i] is None:
                print(f"Room {i + 1}: Available")
            else:
                u, en, ex = self.rooms[i]
                print(f"Room {i + 1}: Booked by {u} (Entry: {en}, Exit: {ex})")

    def book_room(self):
        room_number = int(input("Select a room (1-10): ")) - 1

        if room_number < 0 or room_number >= 10:
            print("Invalid room number!")
            return

        if self.rooms[room_number] is not None:
            print("Room already booked!")
            return

        username = input("Enter username: ")
        password = input("Enter password: ")

        if not self.login(username, password):
            print("Login failed!")
            return

        entry_time = input("Enter entry time (HH:MM): ")
        exit_time = input("Enter exit time (HH:MM): ")

        try:
            datetime.strptime(entry_time, "%H:%M")
            datetime.strptime(exit_time, "%H:%M")
        except ValueError:
            print("Invalid time format!")
            return

        self.rooms[room_number] = (username, entry_time, exit_time)
        self.booked_rooms[room_number] = (username, entry_time, exit_time)

        print(f"Room {room_number + 1} booked successfully!")

    def cancel_booking(self):
        room_number = int(input("Cancel which room (1-10): ")) - 1

        if room_number < 0 or room_number >= 10:
            print("Invalid room number!")
            return

        if self.rooms[room_number] is None:
            print("Room not booked yet.")
            return

        username = input("Enter username: ")
        password = input("Enter password: ")

        if self.login(username, password) and self.rooms[room_number][0] == username:
            self.rooms[room_number] = None
            del self.booked_rooms[room_number]
            print("Booking canceled successfully.")
        else:
            print("You cannot cancel this booking.")

    def exit_system(self):
        print("Exiting the system.")
        sys.exit()

    def main_menu(self):
        while True:
            print("\n-- Study Room Booking System --")
            print("1. Register User")
            print("2. Login and Book a Room")
            print("3. View Available Rooms")
            print("4. Cancel Room Booking")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.register_user()
            elif choice == "2":
                self.book_room()
            elif choice == "3":
                self.show_available_rooms()
            elif choice == "4":
                self.cancel_booking()
            elif choice == "5":
                self.exit_system()
            else:
                print("Invalid choice!")

if __name__ == "__main__":
    system = StudyRoomBookingSystem()
    system.main_menu()
