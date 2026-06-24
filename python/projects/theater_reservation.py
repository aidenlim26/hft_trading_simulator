class Theater:
    def __init__(self):
        self.grid = []          # Start with empty master list, "grid" is just a variable name, can change to "self.2dlist" and would run the same
        for i in range(3):
            new_row = []
            for c in range(4):
                new_row.append('O')
            self.grid.append(new_row)

    def display_seats(self):
        print('Displaying Seats')
        for i in range(len(self.grid)):
            for c in range(len(self.grid[i])):
                print(self.grid[i][c], end=' ')             # (end = ' ') tells python to not start new line (or press enter) when printing, and instead just add a space instead.

            print()                # Same function here, the print() has no specific argument, which makes python start a new line, so that every row on the output has a new line

    def seat_availability(self,row,col):
        if self.grid[row][col] == 'O':
            self.grid[row][col] = "X"
            print('Seat is available')
        elif self.grid[row][col] == 'X':
            print('That seat is already taken!')


program_continue = True
my_theatre = Theater()

while program_continue == True:
    my_theatre.display_seats()
    
    row_input = int(input('Please enter your desired seat row: '))
    col_input = int(input("Please enter your desired seat column: "))
    my_theatre.seat_availability(row_input,col_input)


