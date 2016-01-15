'''
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
write a method to rotate the image by 90 degrees. 
Can you do this in place?
'''
def rotate(matrix):
    for row in matrix:
        if len(matrix) != len(row):
            return "Improper Matrix Size. Not NxN."
    #newMatrix = [list(row)[::-1] for row in zip(*matrix)]
    #transpose
    transposed = [None]*len(matrix)
    for i in range(len(matrix)):
        transposed[i] = [None]*len(matrix)
        for j in range(len(matrix[i])):
            transposed[i][j] = matrix[j][i]
    #rotates by reversing each transposed row
    rotated = [row[::-1] for row in transposed]
    return rotated
    
    
if __name__ == '__main__':
    matrix = [[1,2,3,4,5],[5,6,7,8,9],[9,0,1,2,3],[3,4,5,6]]
    print(rotate(matrix))
    matrix = [[1,2,3,4,5],[5,6,7,8,9],[9,0,1,2,3],[3,4,5,6,7],[8,9,0,1,2]]
    print(rotate(matrix))
