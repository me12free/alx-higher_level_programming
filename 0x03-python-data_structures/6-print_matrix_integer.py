#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in matrix:
            for item in row:
                # Add space between items if not last item in row
                if row.index(item) != len(row) - 1:
                    endspace = " "
                else:
                    endspace = ""
                    # Print the items in the row
                    print("{:d}".format(item), end=endspace)
                    print()
