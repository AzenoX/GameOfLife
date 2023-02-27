import glfw
from OpenGL.GL import *
import numpy as np
import time


size = 100


def draw_grid(grid):
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(-1.0, 1.0, 0.0)
    glScalef(5.0 / float(size), -5.0 / float(size), 1.0)

    for i in range(size):
        for j in range(size):
            if grid[i][j] == 1:
                glColor3f(0.0, 0.0, 0.0)  # black
            else:
                glColor3f(1.0, 1.0, 1.0)  # white
            glBegin(GL_QUADS)
            glVertex2f(i, j)
            glVertex2f(i + 1, j)
            glVertex2f(i + 1, j + 1)
            glVertex2f(i, j + 1)
            glEnd()


def count_adjacent_alive_box(grid, x, y):
    count = 0
    for cx in range(max(0, x - 1), min(size - 1, x + 2)):
        for cy in range(max(0, y - 1), min(size - 1, y + 2)):
            if cx != x or cy != y:
                if grid[cx][cy] == 1:
                    count = count + 1
    return count


def update_grid(grid):
    grid_snap = grid.copy()
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            count = count_adjacent_alive_box(grid, r, c)
            # If this box is alive
            if grid[r][c] == 1:
                if count != 2 and count != 3:
                    grid_snap[r][c] = 0
            # Else box is not alive
            else:
                if count == 3:
                    grid_snap[r][c] = 1
    return grid_snap


def main():
    if not glfw.init():
        raise Exception("Error while init GLFW")

    window = glfw.create_window(500, 500, "Grid", None, None)
    if not window:
        glfw.terminate()
        raise Exception("Error while creating the window")

    glfw.make_context_current(window)

    glClearColor(1.0, 1.0, 1.0, 1.0)

    # Grid creation
    grid = np.random.randint(low=0, high=2, size=(size, size))

    # If you want to try some known figure, comment line 71, uncomment line 74 and all lines corresponding to the figure
    # grid = np.zeros((size, size))

    # 4 beehives
    # grid[20][20] = 1
    # grid[21][20] = 1
    # grid[19][21] = 1
    # grid[19][22] = 1
    # grid[21][21] = 1
    # grid[21][22] = 1
    # grid[20][23] = 1

    # Pulsar
    # grid[10][6] = 1
    # grid[11][6] = 1
    # grid[12][6] = 1
    # grid[16][6] = 1
    # grid[17][6] = 1
    # grid[18][6] = 1
    # grid[8][8] = 1
    # grid[13][8] = 1
    # grid[15][8] = 1
    # grid[20][8] = 1
    # grid[8][9] = 1
    # grid[13][9] = 1
    # grid[15][9] = 1
    # grid[20][9] = 1
    # grid[8][10] = 1
    # grid[13][10] = 1
    # grid[15][10] = 1
    # grid[20][10] = 1
    # grid[10][11] = 1
    # grid[11][11] = 1
    # grid[12][11] = 1
    # grid[16][11] = 1
    # grid[17][11] = 1
    # grid[18][11] = 1
    # grid[10][13] = 1
    # grid[11][13] = 1
    # grid[12][13] = 1
    # grid[16][13] = 1
    # grid[17][13] = 1
    # grid[18][13] = 1
    # grid[8][14] = 1
    # grid[13][14] = 1
    # grid[15][14] = 1
    # grid[20][14] = 1
    # grid[8][15] = 1
    # grid[13][15] = 1
    # grid[15][15] = 1
    # grid[20][15] = 1
    # grid[8][16] = 1
    # grid[13][16] = 1
    # grid[15][16] = 1
    # grid[20][16] = 1
    # grid[10][18] = 1
    # grid[11][18] = 1
    # grid[12][18] = 1
    # grid[16][18] = 1
    # grid[17][18] = 1
    # grid[18][18] = 1

    # Penta-decathlon
    # grid[13][16] = 1
    # grid[14][16] = 1
    # grid[15][16] = 1
    # grid[13][17] = 1
    # grid[15][17] = 1
    # grid[13][18] = 1
    # grid[14][18] = 1
    # grid[15][18] = 1
    # grid[13][19] = 1
    # grid[14][19] = 1
    # grid[15][19] = 1
    # grid[13][20] = 1
    # grid[14][20] = 1
    # grid[15][20] = 1
    # grid[13][21] = 1
    # grid[14][21] = 1
    # grid[15][21] = 1
    # grid[13][22] = 1
    # grid[15][22] = 1
    # grid[13][23] = 1
    # grid[14][23] = 1
    # grid[15][23] = 1

    # Glider
    # grid[3][1] = 1
    # grid[4][2] = 1
    # grid[4][3] = 1
    # grid[3][3] = 1
    # grid[2][3] = 1

    # LWSS
    # grid[3][5] = 1
    # grid[4][5] = 1
    # grid[5][5] = 1
    # grid[6][5] = 1
    # grid[2][6] = 1
    # grid[6][6] = 1
    # grid[6][7] = 1
    # grid[5][8] = 1
    # grid[2][8] = 1

    while not glfw.window_should_close(window):
        draw_grid(grid)

        glfw.poll_events()

        glfw.swap_buffers(window)

        grid = update_grid(grid)

        time.sleep(0.1)

    glfw.terminate()


if __name__ == "__main__":
    main()
