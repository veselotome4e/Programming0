def magic_square(square):
    
    n = len(square)
    m = len(square[0]) - 1

    #taking the main diagonal and the second as well
    diagonal_sum = 0
    second_diagonal_sum = 0
    start_index = 0
    
    
    while start_index < n:
        current_value_main_diagonal = square[start_index][start_index]
        diagonal_sum += current_value_main_diagonal

        current_value_second_diagonal = square[start_index][m]
        second_diagonal_sum += current_value_second_diagonal
        
        m-=1
        start_index +=1

    
    #compare 
    if diagonal_sum == second_diagonal_sum and sum_square_rows_and_columns(square, diagonal_sum):
        return True
    else:
        return False
    
    
def sum_square_rows_and_columns(square, searched_sum):

    n = len(square)
    m = len(square[0])

    for index_row in range(0,n):
        rows_sum = 0
        columns_sum = 0
        for index_column in range(0,m):
            
            row_element = square[index_row][index_column]
            column_element = square[index_column][index_row]
            
            rows_sum += row_element
            columns_sum +=  column_element
            
        if rows_sum != searched_sum and columns_sum != searched_sum:
            return False

    return True


square1 = [ [23, 28, 21], [22, 24, 26], [27, 20, 25] ]
square2 = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
print(magic_square(square1))
print(magic_square(square2))


  
 
 
    
            
            
