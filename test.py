from solution import *
values = grid_values('2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3')
before_values = reduce_puzzle(values)
display(before_values)
after_values = naked_twins(before_values)
display(after_values)
print(after_values != before_values)