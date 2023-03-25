import numpy as np
import time
import sys
import pygame


def update_grid(grid):
    grid_snap = grid.copy()
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            count = np.sum(grid[r-1:r+2, c-1:c+2]) - grid[r, c]
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
    grid = np.zeros((size_x, size_y))
    if figure_name == "beehive":
        grid[20][20] = 1
        grid[21][20] = 1
        grid[19][21] = 1
        grid[19][22] = 1
        grid[21][21] = 1
        grid[21][22] = 1
        grid[20][23] = 1
    elif figure_name == "pulsar":
        grid[10][6] = 1
        grid[11][6] = 1
        grid[12][6] = 1
        grid[16][6] = 1
        grid[17][6] = 1
        grid[18][6] = 1
        grid[8][8] = 1
        grid[13][8] = 1
        grid[15][8] = 1
        grid[20][8] = 1
        grid[8][9] = 1
        grid[13][9] = 1
        grid[15][9] = 1
        grid[20][9] = 1
        grid[8][10] = 1
        grid[13][10] = 1
        grid[15][10] = 1
        grid[20][10] = 1
        grid[10][11] = 1
        grid[11][11] = 1
        grid[12][11] = 1
        grid[16][11] = 1
        grid[17][11] = 1
        grid[18][11] = 1
        grid[10][13] = 1
        grid[11][13] = 1
        grid[12][13] = 1
        grid[16][13] = 1
        grid[17][13] = 1
        grid[18][13] = 1
        grid[8][14] = 1
        grid[13][14] = 1
        grid[15][14] = 1
        grid[20][14] = 1
        grid[8][15] = 1
        grid[13][15] = 1
        grid[15][15] = 1
        grid[20][15] = 1
        grid[8][16] = 1
        grid[13][16] = 1
        grid[15][16] = 1
        grid[20][16] = 1
        grid[10][18] = 1
        grid[11][18] = 1
        grid[12][18] = 1
        grid[16][18] = 1
        grid[17][18] = 1
        grid[18][18] = 1
    elif figure_name == "penta-decathlon":
        grid[13][16] = 1
        grid[14][16] = 1
        grid[15][16] = 1
        grid[13][17] = 1
        grid[15][17] = 1
        grid[13][18] = 1
        grid[14][18] = 1
        grid[15][18] = 1
        grid[13][19] = 1
        grid[14][19] = 1
        grid[15][19] = 1
        grid[13][20] = 1
        grid[14][20] = 1
        grid[15][20] = 1
        grid[13][21] = 1
        grid[14][21] = 1
        grid[15][21] = 1
        grid[13][22] = 1
        grid[15][22] = 1
        grid[13][23] = 1
        grid[14][23] = 1
        grid[15][23] = 1
    elif figure_name == "glider":
        grid[3][1] = 1
        grid[4][2] = 1
        grid[4][3] = 1
        grid[3][3] = 1
        grid[2][3] = 1
    elif figure_name == "lwss":
        grid[3][5] = 1
        grid[4][5] = 1
        grid[5][5] = 1
        grid[6][5] = 1
        grid[2][6] = 1
        grid[6][6] = 1
        grid[6][7] = 1
        grid[5][8] = 1
        grid[2][8] = 1
    else:
        grid = np.random.randint(low=0, high=2, size=(size_x, size_y))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        # Print cells
        for i in range(size_x):
            for j in range(size_y):
                if grid[i, j] == 1:
                    pygame.draw.rect(screen, (0, 0, 0), (j * cell_size, i * cell_size, cell_size, cell_size))

        # Update screen
        pygame.display.flip()

        grid = update_grid(grid)

        time.sleep(sleep_between_steps)

    pygame.quit()


if __name__ == "__main__":
    cell_size = 5
    res_x = 500
    res_y = 500
    size_x = 100
    size_y = 100
    figure_name = None
    sleep_between_steps = 0

    # Input arguments
    if len(sys.argv) > 1:
        figure_name = sys.argv[1]
    if len(sys.argv) > 2:
        size_y = int(sys.argv[2].split(',')[0])
        size_x = int(sys.argv[2].split(',')[1])
    if len(sys.argv) > 3:
        res_y = int(sys.argv[3].split(',')[0])
        res_x = int(sys.argv[3].split(',')[1])
    if len(sys.argv) > 4:
        sleep_between_steps = int(sys.argv[4])

    cell_size = int(min(res_x, res_y) / min(size_x, size_y))

    # Pygame init
    pygame.init()

    # Create window
    screen = pygame.display.set_mode((res_y, res_x))

    main()
