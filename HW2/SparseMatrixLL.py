# Author: 林凡皓
# Date: 2024-3-20
# Purpose: creating a Python class SparseMatrixLL, which uses list of list to store a sparse matrix,
#          the outer list stores the rows, and each row of the matrix is stored in a seperated 
#          unordered list. 

from pythonds3.basic import UnorderedList

class MatrixEntry:
    """
    Represents an entry in a sparse matrix that should be stored into the data field of Node.

    Attributes:
        col (int): Column number of the entry.
        val (int or float): Value of the entry.
    """

    def __init__(self, column_number, value):
        """
        Initialize a MatrixEntry instance.

        Args:
            column_number (int): The column number of the entry.
            value (int or float): The value of the entry.
        """
        self.col = column_number
        self.val = value

    def __eq__(self, other):
        """
        Check if two MatrixEntry instances are equal based on their column number.

        Args:
            other (MatrixEntry): Another MatrixEntry instance to compare with.

        Returns:
            bool: True if the column numbers are equal, False otherwise.
        """
        if isinstance(other, MatrixEntry):
            return self.col == other.col
        return False


class SparseMatrixLL:
    """
    Represents a sparse matrix using linked lists.

    Attributes:
        _nrows (int): Number of rows in the matrix.
        _ncols (int): Number of columns in the matrix.
        _row_list (list): List of UnorderedList, each representing a row in the matrix.
    """
    
    def __init__(self, nrows, ncols):
        """
        Initialize a SparseMatrixLL instance.

        Args:
            nrows (int): Number of rows in the matrix.
            ncols (int): Number of columns in the matrix.
        """
        self._nrows = nrows
        self._ncols = ncols
        self._row_list = [UnorderedList() for i in range(nrows)]


    def __setitem__(self, index, value):
        """
        Set the value at a specified index in the matrix.

        Args:
            index (tuple): A tuple (row, column) specifying the index.
            value (int or float): The value to set at the specified index.
        """
        row, col = index
        self.check_row(row)
        self.check_col(col)

        # print(row, col, value)
        entry = MatrixEntry(col, value)
        if value != 0:  # Only add MatrixEntry if value is not zero
            self._row_list[row].add(entry)
            # print(self._row_list[row])
        else:
            if self._row_list[row].search(entry):
                self._row_list[row].remove(entry)


    def __getitem__(self, index):
        """
        Get the value at a specified index in the matrix.

        Args:
            index (tuple): A tuple (row, column) specifying the index.

        Returns:
            int or float: The value at the specified index.
        """
        row, col = index
        self.check_row(row)
        self.check_col(col)

        entry = MatrixEntry(col, None)
        if self._row_list[row].search(entry):
            current = self._row_list[row]._head
            while current is not None:
                if current.data.col == col:
                    return current.data.val
                else:
                    current = current.get_next()
        else:
            return 0



    
    def __add__(self, other):
        """
        Add two sparse matrices.

        Args:
            other (SparseMatrixLL): Another SparseMatrixLL instance to add.

        Returns:
            SparseMatrixLL: A new SparseMatrixLL instance representing the sum.
        """
        if (self._ncols != other._ncols) or (self._nrows != other._nrows):
            print(f"Error occurs because of different shapes of matrix !")
        else:
            result = SparseMatrixLL(self._nrows, self._ncols)

            for i in range(self._nrows):
                for j in range(self._ncols):
                    result[i, j] = self[i, j] + other[i, j]
            
            return result
        

    def __sub__(self, other):
        """
        Subtract another sparse matrix from this matrix.

        Args:
            other (SparseMatrixLL): Another SparseMatrixLL instance to subtract.

        Returns:
            SparseMatrixLL: A new SparseMatrixLL instance representing the difference.
        """

        if (self._ncols != other._ncols) or (self._nrows != other._nrows):
            print(f"Error occurs because of different shapes of matrix !")
        else:
            result = SparseMatrixLL(self._nrows, self._ncols)

            for i in range(self._nrows):
                for j in range(self._ncols):
                    result[i, j] = self[i, j] - other[i, j]
            
            return result


    def __mul__(self, other):
        """
        Multiply this sparse matrix with another matrix.

        Args:
            other (SparseMatrixLL): Another SparseMatrixLL instance to multiply with.

        Returns:
            SparseMatrixLL: A new SparseMatrixLL instance representing the product.
        """
        if (self._ncols != other._nrows):
            print(f"Error occurs because the shape of two matrixs did not match !")
        else:
            result = SparseMatrixLL(self._nrows, other._ncols)

            for i in range(self._nrows):
                for j in range(other._ncols):
                    sum = 0
                    for k in range(self._ncols):
                        sum += self[i ,k] * other[k, j]
                    result[i, j] = sum
            print(result)
            return result


    #### Do not modify the code below ####
    def from_dense_matrix(self, dense_matrix):
        """
        Populate this sparse matrix from a dense matrix.

        Args:
            dense_matrix (list of lists): A dense matrix represented as a list of lists.
        """
        if not dense_matrix or not dense_matrix[0]:
            raise ValueError("Dense matrix must be non-empty")

        nrows = len(dense_matrix)
        ncols = len(dense_matrix[0])

        if nrows != self._nrows or ncols != self._ncols:
            raise ValueError("Dense matrix dimensions must match the sparse matrix dimensions")

        for i in range(self._nrows):
            for j in range(self._ncols):
                value = dense_matrix[i][j]
                if value != 0:
                    self[i, j] = value

    def check_row(self, row):
        """
        Check if a row index is within the bounds of the matrix.

        Args:
            row (int): The row index to check.
        """
        if type(row) is not int:
            raise TypeError("Row should be an integer")
        if row < 0 or row >= self._nrows:
            raise IndexError("Row number is out of range")

    def check_col(self, col):
        """
        Check if a column index is within the bounds of the matrix.

        Args:
            col (int): The column index to check.
        """
        if type(col) is not int:
            raise TypeError("Column should be an integer")
        if col < 0 or col >= self._ncols:
            raise IndexError("Column number is out of range")
            
    def __delitem__(self, index):
        """
        Delete an entry at a specified index in the matrix.

        Args:
            index (tuple): A tuple (row, column) specifying the index.
        """
        row, col = index
        self.check_row(row)
        self.check_col(col)

        entry = MatrixEntry(col, None)
        if self._row_list[row].search(entry):
            self._row_list[row].remove(entry)
                        
    def to_dense(self):
        """
        Convert this sparse matrix to a dense matrix representation.

        Returns:
            list of lists: A dense matrix representation of this sparse matrix.
        """
        dense_matrix = [[0 for _ in range(self._ncols)] for _ in range(self._nrows)]
        for i in range(self._nrows):
            for j in range(self._ncols):
                dense_matrix[i][j] = self[i, j]
        return dense_matrix

    def __len__(self):
        """
        Get the total number of non-zero entries in the matrix.

        Returns:
            int: The number of non-zero entries.
        """
        total_entries = 0
        for row_list in self._row_list:
            current = row_list._head
            while current:
                total_entries += 1
                current = current.next
        return total_entries

    def __str__(self):
        """
        Create a string representation of the matrix.

        Returns:
            str: A string representation of the matrix.
        """
        matrix_str = ""
        for i in range(self._nrows):
            row_str = ' '.join(str(self[i, j]) for j in range(self._ncols))
            matrix_str += row_str + "\n"
        return matrix_str
    
    def printout(self):
        """
        Print out the non-zero entries of the matrix in a readable format.
        """
        for i in range(self._nrows):
            row_entries = []
            for j in range(self._ncols):
                value = self[i, j]
                if value != 0:
                    row_entries.append(f"{j}: {value}")
            if row_entries:
                print(f"[{i}]:", ', '.join(row_entries))
    #### Do not modify the code above ####