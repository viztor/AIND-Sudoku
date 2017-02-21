assignments = []

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # find al instances with 2 possibles
    with2possibles = [item for item in values if len(values[item]) == 2]
    # Find all instances of naked twins
    nakedTwins = []
    for order, pair1 in enumerate(with2possibles[:-1]):
        for pair2 in with2possibles[order+1:]:
                if (pair1,pair2) in twinsNeighbor and values[pair1] == values[pair2]:
                    nakedTwins.append((pair1,pair2,values[pair1],twinsNeighbor[(pair1,pair2)]))

    # print(nakedTwins)
    # Eliminate the naked twins as possibilities for their peers
    if nakedTwins != []:
        for pair in nakedTwins:
            if len(pair[3]) != 0:
                for box in pair[3]:
                    boxVal = values[box]
                    # print((box, values[box]))
                    for val in pair[2]:
                        boxVal = boxVal.replace(val,'')
                    values = assign_value(values, box, boxVal)
                    # print((box,values[box]))
    return values

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [x+y for x in A for y in B]

# Helper values
rows = 'ABCDEFGHI'
cols = '123456789'
boxes = cross(rows,cols)

# Generating each row and col and square and diagonal
rowBoxes = [cross(r,cols) for r in rows]
colBoxes = [cross(rows,c) for c in cols]
squareBoxes = [cross(r,c) for r in ['ABC','DEF','GHI'] for c in ['123','456','789']]
diagonalBoxes = [[x+y for x,y in zip(rows,cols)],[x+y for x,y in zip(rows,reversed(cols))]]

# Generating list of possible twins and the region they belongs to
twinsMap = {(x,y): region for region in (rowBoxes + colBoxes + squareBoxes + diagonalBoxes) for x in region for y in region}
twinsNeighbor = {key: [val for val in twinsMap[key] if (val != key[0] and val != key[1])] for key in twinsMap}

# Generate a list of neighbors for each region.
sameCol = {x: [col for col in colBoxes if x in col][0] for x in boxes}
sameRow = {x: [row for row in rowBoxes if x in row][0] for x in boxes}
sameSquare = {x: [square for square in squareBoxes if x in square][0] for x in boxes}
sameDiagonal = {x: [item for line in [diag for diag in diagonalBoxes if x in diag] for item in line if item != x] for x in boxes}

neighbors = {x: [val for val in set(sameCol[x] + sameRow[x] + sameSquare[x] + sameDiagonal[x]) if val != x] for x in boxes}


def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    assert(len(grid) == 81)
    res = dict(zip(boxes,grid))
    for val in res:
        if res[val] == '.':
            res[val] = '123456789'

    return res

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    maxLen = max([len(values[b]) for b in boxes])
    countRow = 0
    for r in rowBoxes:
        if countRow % 3 == 0:
            print(('+'+'-'*((maxLen+1)*3))*3+'+')
        countRow += 1
        countCol = 0
        print('|',end='')
        for box in r:
            print(' '*(maxLen - len(values[box]))+values[box]+' ',end='')
            countCol += 1
            if countCol % 3 == 0:
                print('|',end='')
        print('')
    print(('+' + '-' * ((maxLen + 1) * 3)) * 3 + '+')
    return 0




def eliminate(values):
    cleared = [box for box in values if len(values[box]) == 1]
    for box in cleared:
        for neighbor in neighbors[box]:
            values = assign_value(values, neighbor, values[neighbor].replace(values[box],''))
    return values

def only_choice(values):
    for place in (rowBoxes+colBoxes+squareBoxes+diagonalBoxes):
        for i in '123456789':
            choices = [box for box in place if i in values[box]]
            if len(choices) == 1:
                values = assign_value(values, choices[0], i)
    return values

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        before_value = {k: values[k] for k in values if len(values[k]) == 1}
        # display(values)
        values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)
        after_values = {k: values[k] for k in values if len(values[k]) == 1}
        stalled = after_values == before_value
        for box in values:
            if len(values[box]) == 0:
                return False

    return values

def search(values):
    values = reduce_puzzle(values)
    if values is False:
        return False
    unsolved = [(key,item) for (key,item) in values.items() if len(item) > 1 ]
    if unsolved == []:
        return values

    box, options = min(unsolved, key= lambda x: len(x[1]))
    for option in options:
        tempVals = values.copy()
        tempVals[box] = option
        res = search(tempVals)
        if res is not False:
            res[box] = option
            return res
    return False


def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    res = search(values)
    if res is False:
        return False
    else:
        return res


if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
