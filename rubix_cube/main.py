'''
    AUTHOR: JASKARN DHILLON
    DATE: 2/21/2022
    PURPOSE: Show rubix cube graphically (3D)
'''

import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from rubix_cube import rubixCube

# COLOR CONSTANTS USED FOR ONE SIDE CUBE
YELLOW = [1, .9, .3] # Note it looks like teal because yellow hurts my eyes
WHITE = [1, 1, 1]
GREEN = [0, 1, 0]
BLUE = [0.25, 0.5, 1]
RED = [1, 0.25, 0]
ORANGE = [1, 0.65, 0]

# 2D arrays of the cubes faces
bottom_face = None
top_face = None
front_face = None
back_face = None
right_face = None
left_face = None

rbxcube = None # will be set to actual rubix cube class

# Needed for creating the faces
fig = None
ax = None


def create_bottom_face(d):
    global ax, bottom_face
    for m in range(d):
        for n in range(d):
            x = [0 + n, 1 + n, 1 + n, 0 + n]

            y = [0 + m, 0 + m, 1 + m, 1 + m]

            z = [0, 0, 0, 0]

            vertices = [list(zip(x,y,z))]

            poly = Poly3DCollection(vertices, alpha=1)
            face_color = YELLOW # alternative: matplotlib.colors.rgb2hex([0.5, 0.5, 1])
            poly.set_facecolor(face_color)
            poly.set_edgecolor('k')

            bottom_face[m][n] = poly


            ax.add_collection3d(poly)

def create_top_face(d):
    global ax, top_face
    for m in range(d):
        for n in range(d):
            x = [0 + n, 1 + n, 1 + n, 0 + n]

            y = [0 + m, 0 + m, 1 + m, 1 + m]

            z = [0 + d, 0 + d, 0 + d, 0 + d]

            vertices = [list(zip(x,y,z))]

            poly = Poly3DCollection(vertices, alpha=1)
            face_color = WHITE # alternative: matplotlib.colors.rgb2hex([0.5, 0.5, 1])
            poly.set_facecolor(face_color)
            poly.set_edgecolor('k')

            top_face[-m - 1][n] = poly

            ax.add_collection3d(poly)

def create_front_face(d):
    global ax
    for m in range(d):
        for n in range(d):
            x = [0 + n, 1 + n, 1 + n, 0 + n]

            y = [0, 0, 0, 0]

            z = [0 + (d - 1) - m, 0 + (d - 1) - m, 1 + (d - 1) - m, 1 + (d - 1) - m]

            vertices = [list(zip(x,y,z))]

            poly = Poly3DCollection(vertices, alpha=1)
            face_color = GREEN # alternative: matplotlib.colors.rgb2hex([0.5, 0.5, 1])
            poly.set_facecolor(face_color)
            poly.set_edgecolor('k')

            front_face[m][n] = poly

            ax.add_collection3d(poly)

def create_back_face(d):
    global ax
    for m in range(d):
        for n in range(d):
            x = [0 + n, 1 + n, 1 + n, 0 + n]

            y = [0 + d, 0 + d, 0 + d, 0 + d]

            z = [0 + (d - 1) - m, 0 + (d - 1) - m, 1 + (d - 1) - m, 1 + (d - 1) - m]

            vertices = [list(zip(x,y,z))]

            poly = Poly3DCollection(vertices, alpha=1)
            face_color = BLUE # alternative: matplotlib.colors.rgb2hex([0.5, 0.5, 1])
            poly.set_facecolor(face_color)
            poly.set_edgecolor('k')

            back_face[m][-n -1] = poly

            ax.add_collection3d(poly)

def create_right_face(d):
    global ax
    for m in range(d):
        for n in range(d):
            x = [0 + d, 0 + d, 0 + d, 0 + d]

            y = [0 + n, 1 + n, 1 + n, 0 + n]

            z = [0 + (d - 1) - m, 0 + (d - 1) - m, 1 + (d - 1) - m, 1 + (d - 1) - m]

            vertices = [list(zip(x,y,z))]

            poly = Poly3DCollection(vertices, alpha=1)
            face_color = RED # alternative: matplotlib.colors.rgb2hex([0.5, 0.5, 1])
            poly.set_facecolor(face_color)
            poly.set_edgecolor('k')
            right_face[m][n] = poly
            ax.add_collection3d(poly)

def create_left_face(d):
    global ax
    for m in range(d):
        for n in range(d):
            x = [0, 0, 0, 0]

            y = [0 + n, 1 + n, 1 + n, 0 + n]

            z = [0 + (d - 1) - m, 0 + (d - 1) - m, 1 + (d - 1) - m, 1 + (d - 1) - m]

            vertices = [list(zip(x,y,z))]

            poly = Poly3DCollection(vertices, alpha=1)
            face_color = ORANGE # alternative: matplotlib.colors.rgb2hex([0.5, 0.5, 1])
            poly.set_facecolor(face_color)
            poly.set_edgecolor('k')

            left_face[m][-n -1] = poly

            ax.add_collection3d(poly)

def create_graphical_cube(d):
    # Initialize 2D array
    global bottom_face, top_face, front_face, back_face, right_face, left_face, rbxcube
    bottom_face = [[0 for x in range(d)] for y in range(d)]
    top_face = [[0 for x in range(d)] for y in range(d)]
    front_face = [[0 for x in range(d)] for y in range(d)]
    back_face = [[0 for x in range(d)] for y in range(d)]
    right_face = [[0 for x in range(d)] for y in range(d)]
    left_face = [[0 for x in range(d)] for y in range(d)]

    create_top_face(d)
    create_bottom_face(d)
    create_front_face(d)
    create_back_face(d)
    create_right_face(d)
    create_left_face(d)

    # initializes the 2D array
    rbxcube = rubixCube(d)

def _test_setting_face_colors():
    PINK = [1, .753, .796]
    r = 2
    c = 2
    bottom_face[r][c].set_facecolor(PINK)
    top_face[r][c].set_facecolor(PINK)
    front_face[r][c].set_facecolor(PINK)
    back_face[r][c].set_facecolor(PINK)
    right_face[r][c].set_facecolor(PINK)
    left_face[r][c].set_facecolor(PINK)

    fig.canvas.draw()
    fig.canvas.flush_events()


# plotting the 3D graph onto tkinter
def plot():
    global fig, ax
    # the figure that will contain the plot
    fig = Figure(figsize=(4,4))
    ax = fig.add_subplot(111, projection='3d')

    # Dimensions of cube
    d = 3

    create_graphical_cube(d)
    ax.set_xlim(-1,4)
    ax.set_ylim(-1,4)
    ax.set_zlim(-1,4)

    # Removes the numbers from the axis
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_zticklabels([])

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
    						master = window)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # # creating the Matplotlib toolbar
    # toolbar = NavigationToolbar2Tk(canvas,
    # 							window)
    # toolbar.update()
    #
    # # # placing the toolbar on the Tkinter window
    # # canvas.get_tk_widget().pack()

# Creates the buttons which will be used to perform the various operations on rubix cube
def create_operation_buttons():
    frame = Frame(master = window)

    # Adds the clockwise operations of
    frame_clockwise = Frame(master = frame)

    front_button = Button(master = frame_clockwise,command = front_rotation, height =2, width = 10, text = "F")
    right_button = Button(master = frame_clockwise,command = right_rotation, height =2, width = 10, text = "R")
    up_button = Button(master = frame_clockwise, command = up_rotation, height =2, width = 10, text = "U")
    back_button = Button(master = frame_clockwise, command = back_rotation, height =2, width = 10, text = "B")
    left_button = Button(master = frame_clockwise, command = left_rotation, height =2, width = 10, text = "L")
    down_button = Button(master = frame_clockwise, command = down_rotation, height =2, width = 10, text = "D")


    front_button.pack(side = tk.LEFT)
    right_button.pack(side = tk.LEFT)
    up_button.pack(side = tk.LEFT)
    back_button.pack(side = tk.LEFT)
    left_button.pack(side = tk.LEFT)
    down_button.pack(side = tk.LEFT)

    frame_clockwise.pack()

    # Adds the counter clockwise rubix cube operations
    frame_counterclockwise = Frame(master = frame)

    front_prime_button = Button(master = frame_counterclockwise, command = front_prime_rotation, height =2, width = 10, text = "F\'")
    right_prime_button = Button(master = frame_counterclockwise, command = right_prime_rotation, height = 2, width = 10, text = "R\'")
    up_prime_button = Button(master = frame_counterclockwise, command = up_prime_rotation, height =2, width = 10, text = "U\'")
    back_prime_button = Button(master = frame_counterclockwise, command = back_prime_rotation, height =2, width = 10, text = "B\'")
    left_prime_button = Button(master = frame_counterclockwise, command = left_prime_rotation, height =2, width = 10, text = "L\'")
    down_prime_button = Button(master = frame_counterclockwise, command = down_prime_rotation, height =2, width = 10, text = "D\'")


    front_prime_button.pack(side = tk.LEFT)
    right_prime_button.pack(side = tk.LEFT)
    up_prime_button.pack(side = tk.LEFT)
    back_prime_button.pack(side = tk.LEFT)
    left_prime_button.pack(side = tk.LEFT)
    down_prime_button.pack(side = tk.LEFT)

    frame_counterclockwise.pack()

    # Adds the entire frame containing bother rubix cube operations
    frame.pack()


# Given a character of a rubix cube color and converts that into a color
# Ex. input G returns [0, 1, 0](GREEN constant defined above)
def get_color_from_character(c):
    if (c == "G"):
        return GREEN
    if (c == "W"):
        return WHITE
    if (c == "R"):
        return RED
    if (c == "B"):
        return BLUE
    if (c == "Y"):
        return YELLOW
    if (c == "O"):
        return ORANGE


# Method which takes in the classe rbxcube of all sides and updates the colors of the graph
# Based off the rbxcube object
def update_colors():
    d = rbxcube.get_dimension()

    # Front
    for x in range(d):
        for y in range(d):
            color = get_color_from_character(rbxcube.front_side[x][y])
            front_face[x][y].set_facecolor(color)
    # Up
    for x in range(d):
        for y in range(d):
            color = get_color_from_character(rbxcube.up_side[x][y])
            top_face[x][y].set_facecolor(color)
    # Right
    for x in range(d):
        for y in range(d):
            color = get_color_from_character(rbxcube.right_side[x][y])
            right_face[x][y].set_facecolor(color)
    # Left
    for x in range(d):
        for y in range(d):
            color = get_color_from_character(rbxcube.left_side[x][y])
            left_face[x][y].set_facecolor(color)
    # Down
    for x in range(d):
        for y in range(d):
            color = get_color_from_character(rbxcube.down_side[x][y])
            bottom_face[x][y].set_facecolor(color)
    # Back
    for x in range(d):
        for y in range(d):
            color = get_color_from_character(rbxcube.back_side[x][y])
            back_face[x][y].set_facecolor(color)

    fig.canvas.draw()
    fig.canvas.flush_events()

# Rotate the front of cube 90 degrees clockwise
def front_rotation():
    rbxcube.Front()
    update_colors()

# Rotat the front of cube 90 degrees counterclockwise
def front_prime_rotation():
    rbxcube.Front_prime()
    update_colors()

# Rotate the right of cube 90 degress clockwise
def right_rotation():
    rbxcube.Right()
    update_colors()

# Rotate the right of cube 90 degrees counterclockwise
def right_prime_rotation():
    rbxcube.Right_prime()
    update_colors()

def left_rotation():
    rbxcube.Left()
    update_colors()

def left_prime_rotation():
    rbxcube.Left_prime()
    update_colors()

def up_rotation():
    rbxcube.Up()
    update_colors()

def up_prime_rotation():
    rbxcube.Up_prime()
    update_colors()

def back_rotation():
    rbxcube.Back()
    update_colors()

def back_prime_rotation():
    rbxcube.Back_prime()
    update_colors()

def down_rotation():
    rbxcube.Down()
    update_colors()

def down_prime_rotation():
    rbxcube.Down_prime()
    update_colors()

#Buttons such as reset, random, and solve will be located here
def create_option_buttons():
    frame = Frame(master = window)
    reset_button = Button(master = frame, command = reset, height =2, width = 10, text = "Reset")
    solve_button = Button(master = frame, height =2, width = 10, text = "Solve")
    scramble_button = Button(master = frame, command = scramble, height =2, width = 10, text = "Scramble")

    reset_button.pack(side = tk.LEFT)
    solve_button.pack(side = tk.LEFT)
    scramble_button.pack(side = tk.LEFT)

    frame.pack()

# reset the cube to original position
def reset():
    rbxcube.reset_colors()
    update_colors()

# Scramble the cube
def scramble():
    rbxcube.generate_random_position()
    update_colors()


# the main Tkinter window
window = Tk()

# Makes the window not disappear when clicking off
window.wm_attributes("-topmost", True)

# setting the title
window.title('Plotting in Tkinter')

# dimensions of the main window
window.geometry("600x700")

create_option_buttons()
plot()
create_operation_buttons()

# run the gui
window.mainloop()
