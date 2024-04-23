import numpy as np
class Star_cinema:
    hall_list = []
    def entry_hall(self,row,column,hall_no):
        hall = Hall(row,column,hall_no)
        Star_cinema.hall_list.append(hall)
class Hall:
    def __init__(self,row,column,hall_no):
        self._row = row
        self._column = column
        self._hall_no = hall_no
        self._seats = {}
        self._show_list = []
    def entry_show(self,id,movie_name,time):
        movie_details = (id,movie_name,time)
        self._show_list.append(movie_details)
        self._seats[id] = np.zeros((self._row,self._column))
    def book_seats(self,id,list_of_tuple):
        for tuple in list_of_tuple:
            r = tuple[0]
            c = tuple[1]
            self._seats[id][r][c] = 1
            print(f"{id} show is booked for row : {r} column : {c}")
    def view_show_list(self):
        print(self._show_list)
    def view_available_seats(self,id):
        print(self._seats[id])
cineplex = Star_cinema()
cineplex.entry_hall(10,10,1)
# for hall in cineplex.hall_list:
#     print(hall.row,hall.column,hall.hall_no)
for hall in cineplex.hall_list:
    hall.entry_show(111,"movie name : jawan","time : 4:00")    
    hall.entry_show(222,"movie name : kgf","time : 6:00")
    hall.entry_show(333,"movie name : pushpa","time : 9:00")
# for hall in cineplex.hall_list:
#     for show in hall.show_list:
#         print(show)
# for hall in cineplex.hall_list:
#     print( hall.seats)
# for hall in cineplex.hall_list:
#     hall.book_seats(111,[(1,3),(1,4),(1,5)])
# for hall in cineplex.hall_list:
#     hall.view_show_list()
# for hall in cineplex.hall_list:
#     hall.view_available_seats(111)
run = True
while(run):
    print("\n\n\n============ WELCOME TO CINEPLEX MOVIE THEATER ===============")
    print("\n\t Choose your option sir ")
    print("\t 1: View all show")
    print("\t 2: View available seats")
    print("\t 3: Booking a ticket")
    print("\t 4: Exit")

    option = int(input("\n\tEnter your option sir : "))

    if option == 1:
        for hall in cineplex.hall_list:
            hall.view_show_list()
    elif option == 2:
        id = int(input("\n\tEnter the movie id : "))
        flag1 = False
        for hall in cineplex.hall_list:
            for show in hall._show_list:
                if id == show[0]:
                    flag1 = True
        if flag1 == True:
            for hall in cineplex.hall_list:
                hall.view_available_seats(id)
        else : 
            print("\n\t Error :: sorry invalid show id! ")
    elif option == 3:
        list = []
        id = int(input("\n\tEnter the show id : "))
        num_of_ticket = int(input("\n\t Number of ticket ? "))

        flag1 = False
        for hall in cineplex.hall_list:
            for show in hall._show_list:
                if id == show[0]:
                    flag1 = True
        flag2 = True
        for i in range (num_of_ticket):
            row = int(input(f"\n\t Enter the row number of {i+1}th ticket : "))
            col = int(input(f"\n\t Enter the column number of {i+1}th ticket : "))
            tuple = (row,col)
            list.append(tuple)
            for hall in cineplex.hall_list:
                if row >= hall._row or col >= hall._column:
                    flag2 = False
        if flag1 == True and flag2 == True:
            for hall in cineplex.hall_list:
                if hall._seats[id][row][col] == 1:
                    print("\n\t sorry this seats are already booked ")
                else:
                    for hall in cineplex.hall_list:
                        hall.book_seats(id,list)
        elif flag1 == False:
            print("\n\t Error :: invalid show id ") 
        elif flag2 == False:
            print("\n\t Error :: your entered seats is out of range")
    elif option == 4:
        run = False


