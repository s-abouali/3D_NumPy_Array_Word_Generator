import numpy as np

array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                 [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                 [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])

word = array[1, 1, 0] + array[0, 0, 0] + array[1, 2, 2] + array[2, 1, 0] + array[0, 1, 1] + array[1, 0, 2]

print(word)