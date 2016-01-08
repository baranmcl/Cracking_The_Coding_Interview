'''
Write an algorithm such that if an element in an MxM matrix is 0, its entire row and column are set to 0.
'''
def zeroMatrix(matrix):
    for row in matrix:
        if len(matrix) != len(row):
            return "Improper Matrix Size. Not NxN."
    #Find Zeros
    rowZero = set()
    colZero = set()   
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            if matrix[row][column] == 0:
                print("Zero found at: %s, %s" %(row, column))
                rowZero.add(row)
                colZero.add(column)
    #Edit Matrix
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            if column in colZero: matrix[row][column] = 0
            if row in rowZero: matrix[row][column] = 0
            
    return matrix

if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,6,7,8],[9,0,1,2],[3,4,5,6]]
    print(zeroMatrix(matrix))
