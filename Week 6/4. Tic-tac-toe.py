def board_to_string(matrix):

    rows = 3
    columns = 3
    counter = 1

    for each_row in range(0, rows):
        for each_column in range(0, columns):
            current_element = matrix[each_row][each_column]
            if counter == columns:
                combination = str(current_element) + "\\n"
                matrix[each_row][each_column] = combination
                counter = 0
            else:
                combination = str(current_element) + "|"
                matrix[each_row][each_column] = combination
            counter+=1

    return matrix

board = [ ["X", "O", "#"],
          ["X", "X", "X"],
          ["#", "#", "#"] ]
#print(board_to_string(board))
 
def board_to_string_modified(matrix):

    rows = 3
    columns = 3
    counter = 1

    for each_row in range(0, rows):
        for each_column in range(0, columns):
            current_element = matrix[each_row][each_column]
            if counter == columns:
                combination = " " + str(current_element) + " " 
                matrix[each_row][each_column] = combination
                counter = 0
            else:
                combination = " " + str(current_element) + " " + "|"
                matrix[each_row][each_column] = combination
            counter+=1

    return matrix

def board_to_string_final_modification(matrix):

    rows = 3
    columns = 3
    counter = 1

    for each_row in range(0, rows):
        for each_column in range(0, columns):
            current_element = matrix[each_row][each_column]
            if counter == columns:
                combination = " |" + " " + str(current_element) + " " + "|"
                matrix[each_row][each_column] = combination
                counter = 0
            else:
                combination = " |" + " " + str(current_element) + " "
                matrix[each_row][each_column] = combination
            counter+=1

    return matrix



print(board_to_string_final_modification(board))




