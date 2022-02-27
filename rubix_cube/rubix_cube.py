'''
    AUTHOR: JASKARN DHILLON
    DATE: 2/23/2022
    PURPOSE: Implement the rubix cube and its various functions
'''
import random
class rubixCube:
    def __init__(self, dimensions):
        # dimensions refers to how many squares on one row and column
        # Ex. 1x1, 2x2, 3x3, 4x4, 5x5
        self.dimensions = dimensions
        self._create_cube()

    # Using the dimensions creates a cube in 3D so 6 faces created
    def _create_cube(self):
        d = self.dimensions
        self.up_side = [["W" for x in range(d)] for y in range(d)]
        self.down_side = [["Y" for x in range(d)] for y in range(d)]
        self.right_side = [["R" for x in range(d)] for y in range(d)]
        self.left_side = [["O" for x in range(d)] for y in range(d)]
        self.front_side = [["G" for x in range(d)] for y in range(d)]
        self.back_side = [["B" for x in range(d)] for y in range(d)]

    # Creates a cube where all the squares are unique (IE instead of R put R and its position)
    def _create_cube_unique(self):
        d = self.dimensions
        self.up_side = [["Y" + str(x) + str(y) for x in range(d)] for y in range(d)]
        self.down_side = [["W" + str(x) + str(y) for x in range(d)] for y in range(d)]
        self.right_side = [["R" + str(x) + str(y) for x in range(d)] for y in range(d)]
        self.left_side = [["O" + str(x) + str(y) for x in range(d)] for y in range(d)]
        self.front_side = [["G" + str(x) + str(y) for x in range(d)] for y in range(d)]
        self.back_side = [["B" + str(x) + str(y) for x in range(d)] for y in range(d)]

    # display the cube in the terminal
    def display(self):
        # Will be in the format of this U = up, D = down, L = left, F = front, etc
        #   U
        # L F R B
        #   D
        d = self.dimensions

        # print up
        for x in self.up_side:
            #add the space
            row = ""
            for y in x:
                row += "  "

            for y in x:
                row += y + " "
            print(row)

        # print L F R B
        for x in range(d):
            row = ""
            for y in self.left_side[x]:
                row+= y + " "
            for y in self.front_side[x]:
                row+= y + " "
            for y in self.right_side[x]:
                row+= y + " "
            for y in self.back_side[x]:
                row+= y + " "
            print(row)

        # print down
        for x in self.down_side:
            #add the space
            row = ""
            for y in x:
                row += "  "
            for y in x:
                row += y + " "
            print(row)

    # Display the cube with unique numbers
    def display_uniques(self):
            # Will be in the format of this U = up, D = down, L = left, F = front, etc
            #   U
            # L F R B
            #   D
            d = self.dimensions

            # print up
            for x in self.up_side:
                #add the space
                row = ""
                for y in x:
                    row += "    "

                for y in x:
                    row += y + " "
                print(row)

            # print L F R B
            for x in range(d):
                row = ""
                for y in self.left_side[x]:
                    row+= y + " "
                for y in self.front_side[x]:
                    row+= y + " "
                for y in self.right_side[x]:
                    row+= y + " "
                for y in self.back_side[x]:
                    row+= y + " "
                print(row)

            # print down
            for x in self.down_side:
                #add the space
                row = ""
                for y in x:
                    row += "    "
                for y in x:
                    row += y + " "
                print(row)

    # Given an array and a 2d array will put that array into the given column index
    def _put_array_in_a_column(self, array2d, array, col_index):
        for x in range(len(array)):
            array2d[x][col_index] = array[x]

    # Given a array and a 2d array will put that array into the given row index
    def _put_array_in_a_row(self, array2d, array, row_index):
        for x in range(len(array)):
            array2d[row_index][x] = array[x]

    # Given a column index, an 2d array will return the column array at that index
    def _get_col(self, array2d, col_index):
        col = []
        for x in range(len(array2d)):
            col.append(array2d[x][col_index])

        return col

    # Given a row index, an 2d array will return the row array at that index
    def _get_row(self, array2d, row_index):
        return array2d[row_index]

    # given a side rotates the one side clockwise note
    # *** does not rotate take into account how the rotation affects other sides ***
    def _rotate_side_90_clockwise(self, side):
        #A deep copy of side
        temp_side = [row[:] for row in side]


        for x in range(len(side)):
            row = temp_side[-(x + 1)]
            self._put_array_in_a_column(side, row, x)

    # given a side rotate rotates that one side counterclockwise
    # *** does not rotate take into account how the rotation affects other sides ***
    def _rotate_side_90_counterclockwise(self, side):
        #A deep copy of side
        temp_side = [[side[j][i] for j in range(len(side))] for i in range(len(side[0])-1,-1,-1)]

        # copy the values to side
        for x in range(len(side)):
            for y in range(len(side)):
                side[x][y] = temp_side[x][y]



    # Rotates the front of the rubix cube clockwise 90 degress
    def Front(self):
        self._rotate_side_90_clockwise(self.front_side)

        # Move the squares affected by rotation
        d = self.dimensions
        top_bottom_row = self.up_side[-1].copy()
        right_first_column = self._get_col(self.right_side, 0).copy()
        down_first_row = self.down_side[0].copy()
        left_last_column = self._get_col(self.left_side, -1).copy()

        # Reverse the list so it makes sense
        right_first_column.reverse()
        left_last_column.reverse()


        self._put_array_in_a_column(self.right_side, top_bottom_row, 0)
        self._put_array_in_a_row(self.down_side, right_first_column, 0)
        self._put_array_in_a_column(self.left_side, down_first_row, -1)
        self._put_array_in_a_row(self.up_side, left_last_column, -1)

    # Rotate the front of the rubix cube counterclockwise 90 degress
    def Front_prime(self):
        self._rotate_side_90_counterclockwise(self.front_side)

        # Move the squares affected by rotation
        d = self.dimensions
        top_bottom_row = self._get_row(self.up_side, -1).copy()
        right_first_column = self._get_col(self.right_side, 0).copy()
        down_first_row = self._get_row(self.down_side, 0).copy()
        left_last_column = self._get_col(self.left_side, -1).copy()

        # Reversing list is needed so that rotation makes sense
        top_bottom_row.reverse()
        down_first_row.reverse()

        self._put_array_in_a_column(self.right_side, down_first_row, 0)
        self._put_array_in_a_column(self.left_side, top_bottom_row, -1)
        self._put_array_in_a_row(self.down_side, left_last_column, 0)
        self._put_array_in_a_row(self.up_side, right_first_column, -1)

    # Rotate the top of the rubix cube clockwise 90 degrees
    def Up(self):
        self._rotate_side_90_clockwise(self.up_side)

        # Move the squares affected by the rotation
        left_top = self.left_side[0].copy()
        front_top = self.front_side[0].copy()
        right_top = self.right_side[0].copy()
        back_top = self.back_side[0].copy()


        self._put_array_in_a_row(self.front_side, right_top, 0)
        self._put_array_in_a_row(self.right_side, back_top, 0)
        self._put_array_in_a_row(self.back_side, left_top, 0)
        self._put_array_in_a_row(self.left_side, front_top, 0)

    # Rotate the top of the rubix counterclockwise 90 degrees
    def Up_prime(self):
        self._rotate_side_90_counterclockwise(self.up_side)

        # Move the squares affected by the rotation
        left_top = self.left_side[0].copy()
        front_top = self.front_side[0].copy()
        right_top = self.right_side[0].copy()
        back_top = self.back_side[0].copy()

        self._put_array_in_a_row(self.front_side, left_top, 0)
        self._put_array_in_a_row(self.right_side, front_top, 0)
        self._put_array_in_a_row(self.back_side, right_top, 0)
        self._put_array_in_a_row(self.left_side, back_top, 0)

    # Rotate the right of the rubix cube clockwise 90 degress
    def Right(self):
        self._rotate_side_90_clockwise(self.right_side)

        # Move the squares affected by rotation
        up_last_col = self._get_col(self.up_side, -1)
        front_last_col = self._get_col(self.front_side, -1)
        down_last_col = self._get_col(self.down_side, -1)
        back_first_col = self._get_col(self.back_side, 0)

        # Reverse the string so it makes sense
        up_last_col.reverse()
        back_first_col.reverse()

        self._put_array_in_a_column(self.up_side, front_last_col, -1)
        self._put_array_in_a_column(self.back_side, up_last_col, 0)
        self._put_array_in_a_column(self.front_side, down_last_col, -1)
        self._put_array_in_a_column(self.down_side, back_first_col, -1)

    # Rotate the right of the rubix cube counter clockwise 90 degress
    def Right_prime(self):
        self._rotate_side_90_counterclockwise(self.right_side)

        # Move the squares affected by rotation
        up_last_col = self._get_col(self.up_side, -1)
        front_last_col = self._get_col(self.front_side, -1)
        down_last_col = self._get_col(self.down_side, -1)
        back_first_col = self._get_col(self.back_side, 0)

        # Reverse the string so it makes sense
        down_last_col.reverse()
        back_first_col.reverse()


        self._put_array_in_a_column(self.up_side, back_first_col, -1)
        self._put_array_in_a_column(self.back_side, down_last_col, 0)
        self._put_array_in_a_column(self.front_side, up_last_col, -1)
        self._put_array_in_a_column(self.down_side, front_last_col, -1)

    # Rotate the left of the rubix cube clockwise 90 degrees
    def Left(self):
        self._rotate_side_90_clockwise(self.left_side)

        # Move the squares affected by the rotation
        front_first_col = self._get_col(self.front_side, 0)
        up_first_col = self._get_col(self.up_side, 0)
        down_first_col = self._get_col(self.down_side, 0)
        back_last_col = self._get_col(self.back_side, -1)

        # Reverse the list so that rotation makes sense
        back_last_col.reverse()
        down_first_col.reverse()

        self._put_array_in_a_column(self.up_side, back_last_col, 0)
        self._put_array_in_a_column(self.front_side, up_first_col, 0)
        self._put_array_in_a_column(self.down_side, front_first_col, 0)
        self._put_array_in_a_column(self.back_side, down_first_col, -1)

    # Rotate the left of the rubix cube counter clockwise 90 degrees
    def Left_prime(self):
        self._rotate_side_90_counterclockwise(self.left_side)

        # Move the squares affected by the rotation
        front_first_col = self._get_col(self.front_side, 0)
        up_first_col = self._get_col(self.up_side, 0)
        down_first_col = self._get_col(self.down_side, 0)
        back_last_col = self._get_col(self.back_side, -1)

        # Reverse the list so that rotation makes sense
        back_last_col.reverse()
        up_first_col.reverse()

        self._put_array_in_a_column(self.up_side, front_first_col, 0)
        self._put_array_in_a_column(self.front_side, down_first_col, 0)
        self._put_array_in_a_column(self.down_side, back_last_col, 0)
        self._put_array_in_a_column(self.back_side, up_first_col, -1)

    # Rotate the down of the rubix cube clockwise 90 degrees
    def Down(self):
        self._rotate_side_90_clockwise(self.down_side)

        # Move the squares affected by the rotation
        left_last_row = self._get_row(self.left_side, -1).copy()
        front_last_row = self._get_row(self.front_side, -1).copy()
        right_last_row = self._get_row(self.right_side, -1).copy()
        back_last_row = self._get_row(self.back_side, -1).copy()

        self._put_array_in_a_row(self.left_side, back_last_row, -1)
        self._put_array_in_a_row(self.front_side, left_last_row, -1)
        self._put_array_in_a_row(self.right_side, front_last_row, -1)
        self._put_array_in_a_row(self.back_side, right_last_row, -1)

    # Rotate the down of the rubix cube counterclockwise 90 degrees
    def Down_prime(self):
        self._rotate_side_90_counterclockwise(self.down_side)

        # Move the squares affected by the rotation
        left_last_row = self._get_row(self.left_side, -1).copy()
        front_last_row = self._get_row(self.front_side, -1).copy()
        right_last_row = self._get_row(self.right_side, -1).copy()
        back_last_row = self._get_row(self.back_side, -1).copy()

        self._put_array_in_a_row(self.left_side, front_last_row, -1)
        self._put_array_in_a_row(self.front_side, right_last_row, -1)
        self._put_array_in_a_row(self.right_side, back_last_row, -1)
        self._put_array_in_a_row(self.back_side, left_last_row, -1)

    # Rotate the back of the rubix cube clockwise 90 degrees
    def Back(self):
        self._rotate_side_90_clockwise(self.back_side)

        # Move the squares affected by the rotation
        right_last_col = self._get_col(self.right_side,-1).copy()
        up_first_row =  self._get_row(self.up_side, 0).copy()
        left_first_col = self._get_col(self.left_side, 0).copy()
        down_last_row = self._get_row(self.down_side, -1).copy()

        # Reverse so the rotation make sense
        up_first_row.reverse()
        down_last_row.reverse()

        self._put_array_in_a_row(self.up_side, right_last_col, 0)
        self._put_array_in_a_column(self.left_side, up_first_row, 0)
        self._put_array_in_a_row(self.down_side, left_first_col, -1)
        self._put_array_in_a_column(self.right_side, down_last_row, -1)

    # Rotate the back of the rubix cube counterclockwise 90 degrees
    def Back_prime(self):
        self._rotate_side_90_counterclockwise(self.back_side)

        # Move the squares affected by the rotation
        right_last_col = self._get_col(self.right_side,-1).copy()
        up_first_row =  self._get_row(self.up_side, 0).copy()
        left_first_col = self._get_col(self.left_side, 0).copy()
        down_last_row = self._get_row(self.down_side, -1).copy()

        # Reverse so the rotation make sense
        right_last_col.reverse()
        left_first_col.reverse()

        self._put_array_in_a_row(self.up_side, left_first_col, 0)
        self._put_array_in_a_column(self.left_side, down_last_row, 0)
        self._put_array_in_a_row(self.down_side, right_last_col, -1)
        self._put_array_in_a_column(self.right_side, up_first_row, -1)

    # Given the rubix cube and a specific move will perform that move on that given rubix cube
    def make_move(self, move_name):
        cmd = move_name
        if(cmd == "f"):
            self.Front()
        elif(cmd == "f\'"):
            self.Front_prime()
        elif(cmd == "u"):
            self.Up()
        elif(cmd == "u\'"):
            self.Up_prime()
        elif(cmd == "r"):
            self.Right()
        elif(cmd == "r\'"):
            self.Right_prime()
        elif(cmd == "l"):
            self.Left()
        elif(cmd == "l\'"):
            self.Left_prime()
        elif(cmd == "d"):
            self.Down()
        elif(cmd == "d\'"):
            self.Down_prime()
        elif(cmd == "b"):
            self.Back()
        elif(cmd == "b\'"):
            self.Back_prime()

    # Given a move_list will execute that specefic move
    # Assumes that the move is an actual move
    def do_movelist(self, move_list):
        for x in move_list:
            self.make_move(x)

    # Returns the dimensions of the rubix cube
    def get_dimension(self):
        return self.dimensions

    # Rest the rubix cube to original position and color
    def reset_colors(self):
        self._create_cube()

    # Does a random list of moves that will make the cube random
    def generate_random_position(self):
        possible_moves = ['r', 'f', 'l', 'b', 'd', 'u']
        type_rotation = ['', '\'']

        for x in range(100):
            move = random.choice(possible_moves) + random.choice(type_rotation)
            self.make_move(move)


    '''
         This part of the class responsible for algorithim and solving the cube
    '''
    # returns the sequence of moves that make the cube have white faces 
    def _get_white_cross_algorithim(self):
        pass




#
# def main():
#     rbxcube = rubixCube(3)
#     lines = ["r", "r", "b", "b", "l", "l", "r", "r", "b", "b", "l", "l"]
#     movelist = lines
#     while(True):
#         cmd = input("Give me command ")
#         if(cmd == "s"):
#             rbxcube.display()
#         elif(cmd == "#"):
#             print("Goodbye!")
#             break
#         elif(cmd == "ml"):
#             do_movelist(rbxcube, movelist)
#         else:
#             make_move(rbxcube, cmd)

# main()
