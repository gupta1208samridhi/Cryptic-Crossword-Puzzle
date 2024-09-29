all_pos = []
for row in range(15):
    for col in range(15):
        all_pos.append((row,col))

def check_white(pos: tuple[int]) -> bool:
    row, column = pos
    return grid[row][column] == 'W'

def check_down(pos: tuple[int]) -> bool:
    row, column = pos
    if (row == 0 and grid[row + 1][column] == 'W') or (0 < row < 14 and grid[row - 1][column] == 'B'and grid[row + 1][column] == 'W'):
        return True

def check_across(pos: tuple[int]) -> bool:
    row, column = pos
    if  (column == 0 and grid[row][column + 1] == 'W') or (0 < column < 14 and grid[row][column - 1] == 'B' and grid[row][column + 1] == 'W'):
        return True
   
def numbered_pos(all_pos: list[tuple]) -> list[tuple]:
    numbered_pos = []
    number = 1
    for pos in all_pos:
        if check_white(pos) and (check_down(pos) or check_across(pos)):
            row, column = pos
            numbered_pos.append((row + 1, column + 1, number))
            number += 1
    return numbered_pos

print(numbered_pos(all_pos))
