f = open("11.txt", "r")

contents = f.read()
lines = contents.split('\n')
grid = [line.split(' ') for line in lines]
print grid


array = []

for i in range(0,20):
    for j in range(0,20):
        try:
            array.append(int(grid[i][j]) * int(grid[i][j+1]) * int(grid[i][j+2]) * int(grid[i][j+3]))
        except IndexError:
            pass
        try:
            array.append(int(grid[i][j]) * int(grid[i+1][j]) * int(grid[i+2][j]) * int(grid[i+3][j]))
        except IndexError:
            pass
        try:
            array.append(int(grid[i][j]) * int(grid[i+1][j+1]) * int(grid[i+2][j+2]) * int(grid[i+3][j+3]))
        except IndexError:
            pass
        try:
            array.append(int(grid[i][j]) * int(grid[i-1][j+1]) * int(grid[i-2][j+2]) * int(grid[i-3][j+3]))
        except IndexError:
            pass
print max(array)
