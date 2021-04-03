def find_target_word(mat, target):
    col_words = [''] * len(mat[0])
    for row in range(len(mat)):
        row_word = ''
        for col in range(len(mat[0])):
            col_words[col] += mat[row][col]
            row_word += mat[row][col]
            if row_word == target:
                return True
            if col_words[col] == target:
                return True
    return False
    
 mat = [['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

assert True == find_target_word(mat, 'MAS')
assert True == find_target_word(mat, 'MASS')
assert True == find_target_word(mat, 'FACI')
assert True == find_target_word(mat, 'CQ')
assert True == find_target_word(mat, 'A')
assert True == find_target_word(mat, 'ABNA')
