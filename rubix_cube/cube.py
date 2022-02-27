'''
    AUTHOR: JASKARN DHILLON
    DATE: 2/21/2022
    PURPOSE: Show rubix cube graphically (3D)
'''

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# COLOR CONSTANTS USED FOR ONE SIDE CUBE
YELLOW = [1, 1, 0]
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

# Figure and where to plot the cube
fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111, projection='3d')

# Event handling (key presses)
def key_press_event(event):
    fig.canvas.pause()
    # if(event.key == 'd'):
    #     print("gg")
    test_setting_face_colors()
    print("hello darkness")


fig.canvas.mpl_connect('key_press_event', key_press_event)



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

def create_graphical_cube():
    # Dimensions of cube
    d = 3

    # Initialize 2D array
    global bottom_face, top_face, front_face, back_face, right_face, left_face
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



def test_setting_face_colors():
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



create_graphical_cube()
ax.set_xlim(-1,4)
ax.set_ylim(-1,4)
ax.set_zlim(-1,4)

plt.show()

