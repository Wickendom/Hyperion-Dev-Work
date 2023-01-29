def input_mine_grid():
    grid = []
    #loop over each row and column to create a grid of mines and empty spaces
    for i in range(0,5):
        row = []
        for i in range(0,5):
            col = input("please enter either a # or a - ")
            row.append(col)
        grid.append(row)
    # print_grid(grid)
    solve_mine_grid(grid)


def solve_mine_grid(mine_grid):
    grid = []
    # loop over the inputted grid and create a row and fills each column by checking its neighbors for mines
    for y in range(0, 5):
        row = []
        for x in range(0, 5):
            if mine_grid[y][x] == '-':
                row.append(str(check_neighbors(x,y,mine_grid)))
            elif mine_grid[y][x] == '#':
                row.append('#')
        grid.append(row)
    print_grid(grid)


def check_neighbors(x,y,minegrid):
    nearby_mine_amount = 0
    # print(f"Checking neighbors for {x}, {y}")
    #below checks each neighbor whilst first checking that it will not go out of the array bounds
    # if it finds a mine it increases the above variable by one and returns that value
    if x > 0 and y > 0:
        if minegrid[y - 1][x - 1] == '#':
            nearby_mine_amount += 1
    if y > 0:
        if minegrid[y - 1][x] == '#':
            nearby_mine_amount += 1
    if y > 0 and x < 4:
        if minegrid[y - 1][x + 1] == '#':
            nearby_mine_amount += 1
    if x > 0:
        if minegrid[y][x - 1] == '#':
            nearby_mine_amount += 1
    if x < 4:
        if minegrid[y][x + 1] == '#':
            nearby_mine_amount += 1
    if y < 4 and x > 0:
        if minegrid[y + 1][x - 1] == '#':
            nearby_mine_amount += 1
    if y < 4:
        if minegrid[y + 1][x] == '#':
            nearby_mine_amount += 1
    if y < 4 and x < 4:
        if minegrid[y + 1][x + 1] == '#':
            nearby_mine_amount += 1
    return nearby_mine_amount


def print_grid(grid):
    # prints the grid in a user-friendly way
    for row in grid:
        print(row)


input_mine_grid()
