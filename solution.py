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

    # Find all instances of naked twins

    # Eliminate the naked twins as possibilities for their peers
    pass

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [x+y for x in A for y in B]

rows = 'ABCDEFGHI'
cols = '123456789'
boxes = cross(rows,cols)
rowBoxes = [cross(r,cols) for r in rows]
colBoxes = [cross(rows,c) for c in cols]
squareBoxes = [cross(r,c) for r in ['ABC','DEF','GHI'] for c in ['123','456','789']]

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
    return dict(zip(boxes,grid))

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
            print(
                ('+'+'-'*((maxLen+1)*3+1))*3+'+'
            )
        countRow += 1
        countCol = 0
        print('|',end='')
        for box in r:
            print(values[box]+' ',end='')
            countCol += 1
            if countCol % 3 == 0:
                print('|',end='')
        print('')
    return 0




def eliminate(values):
    pass

def only_choice(values):
    pass

def reduce_puzzle(values):
    values = eliminate (values)
    values = naked_twins (values)
    return only_choice (values)


def search(values):
    pass

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """

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
