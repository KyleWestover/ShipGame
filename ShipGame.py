# Author: Kyle Westover
# GitHub username: KyleWestover
# Date: 11Mar22
# Description: Create a class called ShipGame that allows two players to play a game of Battleship


class Ship:
    """
    Represents a ship object with length and orientation
    """
    def __init__(self, length, orientation, coordinates):
        """
        Creates ship object with length, orientation, and coordinates of the 'head' of the ship (square clesest to A1).
        Used by ShipGame class.
        """
        self._length = length
        self._orientation = orientation
        self._coordinates = coordinates

    def get_orientation(self):
        """
        Returns ship orientation
        """
        return self._orientation

    def get_coordinates(self):
        """
        Returns coordinates for 'head' of ship
        """
        return self._coordinates

    def get_length(self):
        """
        Returns ship length
        """
        return self._length

    def set_length(self):
        """Modifies ship length"""
        self._length -= 1



class ShipGame:
    """
    Represents a game of battleship with a 10x10 board
    """
    def __init__(self):
        self._first_board = \
            {'A': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             'B': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             'C': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             'D': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             'E': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             'F': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             'G': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             'H': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             'I': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             'J': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']}
        self._second_board = \
            {'A': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             'B': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             'C': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             'D': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             'E': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             'F': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             'G': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             'H': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             'I': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             'J': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']}

        self._turn = 'first'
        self._current_state = 'UNFINISHED'
        self._first_ship_lookup = {}
        self._second_ship_lookup = {}
        self._first_ship_count = 0
        self._second_ship_count = 0

    def place_ship(self, player, ship_length, coordinates, orientation):
        """
        Takes as parameters the player, ship length, coordinates of square it will occupy closest to A1, and
        orientation. If ship would not fit entirely on board, would overlap with another ship, or has a length less than
        2, the ship will not be added and method will return false. Otherwise, ship will be added and method will return
        true
        """
        coord_counter = 0
        temp_ship = Ship(ship_length, coordinates, orientation)  # store ship object in temporary variable
        row_letter = coordinates[0].upper()  # extract row from coords
        row = ord(row_letter) - 64  # make row integer from row_letter
        if len(coordinates) > 2:  # make column integer based on coords
            column = int(coordinates[1:len(coordinates)])
        else:
            column = int(coordinates[1])
        if ship_length < 2:  # return false if ship is too short
            return False
        if row > 10 or row < 1 or column > 10 or column < 1:  # return false if input coordinates are invalid
            return False
        if player.lower() == 'first':
            next_column = column  # keeps column variable from being modified in loop
            next_row = row  # keeps row variable from being modified in loop
            temp_dict = {}  # creates temporary dictionary inside loop to be added to ship_lookups if all valid
            list_counter = 0  # used to access temp_list while filling player's board with ships
            temp_list = []  # used to store ship coordinates for board until all nodes of ship are found valid
            while coord_counter < ship_length:  # iterate through ship's full coordinates to verify all are valid
                if orientation.upper() == 'R':  # if placement is valid, add coordinates and ship object to dictionary; increment row and counter
                    if (row_letter + str(next_column)) in self._first_ship_lookup:  # return False if space filled by ship already
                        return False
                    if row > 10 or row < 1 or next_column > 10 or next_column < 1:  # return False if not valid space
                        return False
                    temp_dict[row_letter + str(next_column)] = temp_ship  # update temporary dictionary
                    temp_list.append(chr(next_row + 64))
                    temp_list.append(next_column - 1)
                    next_column += 1
                    coord_counter += 1
                if orientation.upper() == 'C':  # if placement is valid, add coordinates and ship object to dictionary; increment row and counter
                    if (chr(next_row + 64) + str(column)) in self._first_ship_lookup:  # return False if space filled by ship already
                        return False
                    if next_row > 10 or next_row < 1 or next_column > 10 or next_column < 1:  # return False if not valid space
                        return False
                    temp_dict[chr(next_row + 64) + str(column)] = temp_ship  # update temporary dictionary
                    temp_list.append(chr(next_row + 64))
                    temp_list.append(next_column - 1)
                    next_row += 1
                    coord_counter += 1
            for n in temp_dict:  # add entries to permanent dictionary
                self._first_board[temp_list[list_counter]][temp_list[list_counter + 1]] = 'S'
                list_counter += 2
                self._first_ship_lookup[n] = temp_dict[n]
            self._first_ship_count += 1  # update ship counter

            return True
        if player.lower() == 'second':
            next_column = column  # keeps column variable from being modified in loop
            next_row = row  # keeps row variable from being modified in loop
            temp_dict = {}  # creates temporary dictionary inside loop to be added to ship_lookups if all valid
            list_counter = 0  # used to access temp_list while filling player's board with ships
            temp_list = []   # used to store ship coordinates for board until all nodes of ship are found valid
            while coord_counter < ship_length:  # iterate through ship's full coordinates to verify all are valid
                if orientation.upper() == 'R':  # if placement is valid, add coordinates and ship object to dictionary; increment row and counter
                    if (row_letter + str(next_column)) in self._second_ship_lookup:  # return False if space filled by ship already
                        return False
                    if row > 10 or row < 1 or next_column > 10 or next_column < 1:  # return False if not valid space
                        return False
                    temp_dict[row_letter + str(next_column)] = temp_ship  # update temporary dictionary
                    temp_list.append(chr(next_row + 64))
                    temp_list.append(next_column-1)
                    next_column += 1
                    coord_counter += 1
                if orientation.upper() == 'C':  # if placement is valid, add coordinates and ship object to dictionary; increment row and counter
                    if (chr(next_row + 64) + str(column)) in self._second_ship_lookup:  # return False if space filled by ship already
                        return False
                    if next_row > 10 or next_row < 1 or next_column > 10 or next_column < 1:  # return False if not valid space
                        return False
                    # if placement is valid, add coordinates and ship object to dictionary; increment row and counter
                    temp_dict[chr(next_row + 64) + str(column)] = temp_ship  # update temporary dictionary
                    temp_list.append(chr(next_row + 64))
                    temp_list.append(next_column - 1)
                    next_row += 1
                    coord_counter += 1
            for n in temp_dict:  # add entries to permanent dictionary
                self._second_board[temp_list[list_counter]][temp_list[list_counter+1]] = 'S'
                list_counter += 2
                self._second_ship_lookup[n] = temp_dict[n]
            self._second_ship_count += 1  # update ship counter

            return True

    def get_current_state(self):
        """
        Returns current state of the game
        """
        return self._current_state

    def fire_torpedo(self, player, target):
        """
        Takes player firing torpedo and target square as parameters. If not that players turn or game already won,
        returns false. Otherwise, records move, updates turn, updates current state, and returns True
        """
        if player.lower() != self._turn:  # return false if player tries to fire torpedo out of turn
            return False
        if self.get_current_state() != 'UNFINISHED':  # if either player has already won, return false
            return False
        if player.lower() == 'first':
            row_letter = target[0].upper()  # set row, row letter, and column values from target param
            row = ord(row_letter) - 64
            if len(target) > 2:
                column = int(target[1:len(target)])
            else:
                column = int(target[1].upper())
            if self._second_board[row_letter][column - 1] != 'S':  # if player misses all in-play ship nodes
                if self._second_board[row_letter][column - 1] == 'X':  # if target has already hit the ship here
                    self._turn = 'second'  # update turn

                    return True
                else:
                    self._second_board[row_letter][column - 1] = 'O'  # put O in missed square for tracking purposes
                    self._turn = 'second'  # update turn

                    return True
            elif target.upper() in self._second_ship_lookup:  # if player hits ship
                self._second_ship_lookup[target].set_length()  # update ship length
                self._second_board[row_letter][column-1] = 'X'
                self._turn = 'second'
                if self._second_ship_lookup[target].get_length() == 0:  # update ship count if ship has been sunk
                    self._second_ship_count -= 1
                del self._second_ship_lookup[target]
                if self._second_ship_count == 0:
                    self._current_state = 'FIRST_WON'

                return True
        if player.lower() == 'second':
            row_letter = target[0].upper()  # set row, row letter, and column values from target param
            row = ord(row_letter) - 64
            if len(target) > 2:
                column = int(target[1:len(target)])
            else:
                column = int(target[1].upper())
            if self._first_board[row_letter][column-1] != 'S':  # if player misses all in-play ship nodes
                if self._first_board[row_letter][column-1] == 'X':  # if target has already hit the ship here
                    self._turn = 'first'  # update turn

                    return True
                else:
                    self._first_board[row_letter][column-1] = 'O'  # put O in missed square for tracking purposes
                    self._turn = 'first'  # update turn

                    return True
            elif target.upper() in self._first_ship_lookup:  # if player hits ship
                self._first_ship_lookup[target].set_length()  # update ship length
                self._first_board[row_letter][column-1] = 'X'  # put X in hit square
                self._turn = 'first'
                if self._first_ship_lookup[target].get_length() == 0:  # update ship count if ship has been sunk
                    self._first_ship_count -= 1
                del self._first_ship_lookup[target]
                if self._first_ship_count == 0:
                    self._current_state = 'SECOND_WON'

                return True

    def get_num_ships_remaining(self, player):
        """
        Takes player as parameter and returns number of ships that player has remaining
        """
        if player.lower() == 'first':
            return self._first_ship_count
        if player.lower() == 'second':
            return self._second_ship_count
        return
