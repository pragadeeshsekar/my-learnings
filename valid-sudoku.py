# Check uniqueness 
def uniqueness(input_values):
    hashmap = {}.fromkeys(map(str, range(1, 10)), 0)
    for val in input_values:
        if val != '_':
            hashmap[val] += 1
            if hashmap[val] > 1:
                return False
    return True

# check uniqueness of sub-matrix
def min_matrix(matrix, start_row, start_col):
    row = start_row
    # get sub-matrix sudoku length
    sub_matrix_len = int(pow(len(matrix), 1/2))
    sub_matrix = []
    while row < (start_row + sub_matrix_len):
        sub_matrix.extend(matrix[row][start_col:start_col+sub_matrix_len])
        row += 1
    return uniqueness(sub_matrix)

# main validsudoku function
def check_valid_sudoku(input_list):
    '''
    param input_list: sudoku input in list of string - each index corresponds to
                      row elements and empty elements as .
                      for eg: 3x3 ['..1234...', ...]
    return Boolean: return validity response either True or False
    '''
    matrix_2d = [list(row.replace('.', '_')) for row in input_list]
    row_len, col_len = len(matrix_2d), len(matrix_2d[0])
    sub_matrix_len = int(pow(len(matrix_2d), 1/2))
    # row uniqueness check
    for row in matrix_2d:
        if not uniqueness(row):
            return False
    # column uniqueness check
    for col in range(col_len):
        col_val = []
        for row in range(row_len):
            col_val.append(matrix_2d[row][col])
        if not uniqueness(col_val):
            return False
    # sub-matrix uniqueness check
    for row in range(0, row_len, sub_matrix_len):
        for col in range(0, col_len, sub_matrix_len):
            if not min_matrix(matrix_2d, row, col):
                return False
    return True
