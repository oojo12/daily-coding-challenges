def find_target_word(mat, target):
    col_words = [''] * len(mat[0])
    for row in range(len(mat)):
        row_word = ''
        for col in range(len(mat[0])):
            col_words[col] += mat[row][col]
            row_word += mat[row][col]
        if row_word == target:
            return True
    
    for word in col_words:
        if word == target:
            return True
    return False
