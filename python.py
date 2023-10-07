class Hall:
    def __init__(self, rows, cols, hall_no):
        self._rows = rows
        self._cols = cols
        self.__hall_no = hall_no
        self.__show_list = []  
        # way 1
        self.__seats = []
        for a in range(rows):
            row = [0 for a in range(cols)]
            self.__seats.append(row)
    # way 2
    # self.__seats = [[0 for _ in range(cols)] for _ in range(rows)] 

    def _entry_show(self, id, movie_name, time):
        self.__show_list.append({"id": id, "movie_name": movie_name, "time": time})

    def book_seats(self, show_id, seat_list):
        for show in self.__show_list:
            if show["id"] == show_id:
                for row, col in seat_list:
                    if 1 <= row <= self._rows and 1 <= col <= self._cols:
                        if self.__seats[row - 1][col - 1] == 0:
                            self.__seats[row - 1][col - 1] = 1
                            print(f"Seat ({row},{col}) booked successfully for Show ID {show_id}.")
                        else:
                            print(f"Seat ({row},{col}) is already booked.")
                    else:
                        print(f"Invalid seat: ({row},{col}). Please give right information")
                break
        else:
            print(f"Show  ID {show_id} not found.")

        # for show in self.__show_list:
        #     if show["id"] == show_id:
        #         print(f"\nAvailable seats for Show ID {show_id} ({show['movie_name']} at {show['time']}):")
        #         for i in range(self._rows):
        #             for j in range(self._cols):
        #                 print(self.__seats[i][j], end=" ")
        #             print()


    def _view_all_shows(self):
        for show in self.__show_list:
            print(f"Movie - Name: {show['movie_name']}, Show ID: {show['id']}, Time: {show['time']}")

    def view_available_seats_hall(self, show_id):
        for show in self.__show_list:
            if show["id"] == show_id:
                print(f"\nAvailable seats:")
                for i in range(self._rows):
                    for j in range(self._cols):
                        if self.__seats[i][j] == 0:
                            print(f"seats({i + 1},{j + 1})" ,end="\n")

        for show in self.__show_list:
            if show["id"] == show_id:
                print(f"\n\nAvailable seats in graph:")
                for i in range(self._rows):
                    for j in range(self._cols):
                        print(self.__seats[i][j], end=" ")
                    print()


class cinema_management_mystem:
    def __init__(self):
        self.halls = []

    def add_hall(self, rows, cols, hall_no):
        hall = Hall(rows, cols, hall_no)
        self.halls.append(hall)

    def list_all_shows_today(self):
        print("Shows Today:")
        for hall in self.halls:
            print(f"Hall No: {hall._Hall__hall_no}")
            hall._view_all_shows()

    def view_available_seats(self, hall_no, show_id):
        for hall in self.halls:
            if hall._Hall__hall_no == hall_no:
                hall.view_available_seats_hall(show_id)
                return
        else:
            print(f"Hall not found.")

    def book_tickets(self, hall_no, show_id, seat_list):
        for hall in self.halls:
            if hall._Hall__hall_no == hall_no:
                hall.book_seats(show_id, seat_list)
                return
        else:
            print(f"Hall not found.")

    def show_menu(self):
        while True:
            print("\n1. View all shows today")
            print("2. View available seats")
            print("3. Book tickets")
            print("4. Exit")
            option = input("Enter option: ")

            if option == "1":
                self.list_all_shows_today()
            elif option == "2":
                hall_no = int(input("Enter Hall Number: "))
                show_id = int(input("Enter Show ID: "))
                self.view_available_seats(hall_no, show_id)
            elif option == "3":
                hall_no = int(input("Enter Hall Number: "))
                show_id = int(input("Enter Show ID: "))
                num_seats = int(input("Enter the number of seats: "))
                seat_list = []
                for x in range(num_seats):
                   # row, col = map(int, input("Enter row and column for seat (e.g., row col): ").split())
                    row =int(input("Enter row : "))
                    col = int(input("Enter col : "))
                    seat_list.append((row, col))
                self.book_tickets(hall_no, show_id, seat_list)
            elif option == "4":
                print("Thank you!")
                break
            else:
                print("Invalid\nPlease try again!")

#making a system
system = cinema_management_mystem()

# adding halls by my self
system.add_hall(rows=10, cols=10, hall_no=1)
system.add_hall(rows=12, cols=12, hall_no=2)

# adding shows to halls by my self
system.halls[0]._entry_show(id=1, movie_name="KGF3", time="9:00 PM")
system.halls[0]._entry_show(id=2, movie_name="PORAN", time="10:00 PM")
system.halls[1]._entry_show(id=3, movie_name="SURONGO", time="11:30 PM")

system.show_menu()
