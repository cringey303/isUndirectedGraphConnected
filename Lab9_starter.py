# Name: Lucas Root
# KUID: 3144935
# Lab session: Wed 11am
# Lab #9
# Description: uses depth-first search to tell if a matrix is connected
#
# Collaborators: Gemini for test cases
# Outside sources: GeeksForGeeks DFS algorithm

#This function is similar to Lab 3, but now it will keep running until the user inputs a square matrix
def get_square_matrix(ints=False):
    """ 
    Takes a square matrix of numbers from the user. Each row can be 
    separated by commas and/or spaces. Automatically ends after the last row.

    If ints=False, the function returns a matrix of strings. 
    If ints=True, they will be cast to int instead
    """
    print("Enter your matrix:")
    matrix = []

    x = input()
    #If blank line, try again
    if not x.strip():
        return get_square_matrix(ints=ints)

    items = x.replace(",", " ").split()
    length = len(items)
    matrix = []

    if length == 1:
        matrix.append(items)
        return matrix

    #Save the first row
    if not ints:
        matrix.append(items)
    else:
        try:
            row = [int(entry) for entry in items]
            matrix.append(row)
        except ValueError:
            print("Error: all entries must be numbers! Try again:")
            #If first row is bad, try again
            return get_square_matrix(ints=ints)

    #Get the rest of the rows
    while True:
        x = input()
        items = x.replace(",", " ").split()
        if len(items) != length:
            print("Error: row lengths are mismatched! Try again:")
            continue  # re-try the line
        if not ints:
            matrix.append(items)
        else:
            try:
                row = [int(entry) for entry in items]
                matrix.append(row)
            except ValueError:
                print("Error: all entries must be numbers! Try again:")
                continue  # re-try the line
        #Check if matrix has been completed (is square)
        if len(matrix) == length:
            return matrix

#Helper function to print a 2-D matrix
def print_matrix(m):
    n = len(m)
    # Create labels (a, b, c, ...)
    labels = [chr(ord('a') + i) for i in range(n)]
    
    # Print top header row
    print("  ", end="")  # space for corner
    for label in labels:
        print(label, end=" ")
    print()
    
    # Print each row with its corresponding label
    for i, row in enumerate(m):
        print(labels[i], end=" ")  # row label
        for item in row:
            print(item, end=" ")
        print()

# u: current vertex
# n: number of vertices
# recursive depth-first search function
def dfs(u: int, M_R, visited, n: int):
    # mark visited
    visited[u] = True
    # check all neighbors
    for v in range(n):
        # check if u and v are connected and v not visited
        if M_R[u][v] == 1 and not visited[v]:
            dfs(v, M_R, visited, n)

def is_matrix_connected(M_R):
    n = len(M_R)

    visited = [False] * n
    
    dfs(0, M_R, visited, n)

    # if any value in visited is false after dfs, 
    # then you can't reach every node from one node
    # and the matrix is not connected
    if not all(visited):
        return False
    return True

def main():
    M_R = get_square_matrix(ints=True)
    print("Got: ")
    print_matrix(M_R)

    if is_matrix_connected(M_R):
        print("connected") 
    else:
        print("not connected")

if __name__ == "__main__":
    main()
