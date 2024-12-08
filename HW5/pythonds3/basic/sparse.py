# Adapated from https://gist.github.com/saitejamalyala/7badbf9ec5b008c91de66f687431ec57

import math
from typing import Dict, Tuple, Optional, List

class SparseMatrix:
    """Sparse Matrix class
    Args:
        data: A dictionary of (i, j) -> value
    """

    def __init__(self, data: Dict[Tuple[int, int], float] = None):
        self.data = data or {}

    def from_dense_matrix(self, matrix: List[List[float]]) -> "SparseMatrix":
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    self[(i, j)] = matrix[i][j]
        # [self[(i, j)] for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] != 0]
        return self

    def __getitem__(self, key: Tuple[int, int]) -> float:
        return self.data.get(key, 0)

    def __setitem__(self, key: Tuple[int, int], value: float):
        self.data[key] = value

    def __delitem__(self, key: Tuple[int, int]):
        del self.data[key]

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        if not self.data:
            return "SparseMatrix()"

        # Determine the dimensions of the matrix
        max_row = max(key[0] for key in self.data) + 1
        max_col = max(key[1] for key in self.data) + 1

        # Construct a string representation of the dense matrix
        dense_repr = "["
        for i in range(max_row):
            if i > 0:
                dense_repr += " "
            dense_repr += "["
            for j in range(max_col):
                dense_repr += f"{self[i, j]}"
                if j < max_col - 1:
                    dense_repr += ", "
            dense_repr += "]"
            if i < max_row - 1:
                dense_repr += "\n"
        dense_repr += "]"

        return f"SparseMatrix(\n{dense_repr}\n)"

    def __add__(self, other: "SparseMatrix") -> "SparseMatrix":
        if not isinstance(other, SparseMatrix):
            raise ValueError("Addition only supports SparseMatrix instances.")

        result = SparseMatrix()
        keys = set(self.data.keys()) | set(other.data.keys())
        for key in keys:
            result[key] = self[key] + other[key]
        return result


    def __sub__(self, other: "SparseMatrix") -> "SparseMatrix":
        if not isinstance(other, SparseMatrix):
            raise ValueError("Subtraction only supports SparseMatrix instances.")

        result = SparseMatrix()
        keys = set(self.data.keys()) | set(other.data.keys())
        for key in keys:
            result[key] = self[key] - other[key]
        return result

    # return SparseMatrix({k: v - other.data.get(k, 0) for k, v in self.data.items()})

       
    def __mul__(self, other: "SparseMatrix") -> "SparseMatrix":
        if not isinstance(other, SparseMatrix):
            raise ValueError("Multiplication only supports SparseMatrix instances.")

        result = SparseMatrix()
        # Iterate over non-zero elements in self
        for (i, k) in self.data:
            # Iterate over non-zero elements in other, where the column index of other matches the row index of self
            for (j, l) in other.data:
                if k == j:
                    result[i, l] += self[i, k] * other[j, l]
        return result

    def __rmul__(self, other: float) -> "SparseMatrix":
        result = SparseMatrix()
        for key in self:
            result[key] = self[key] * other
        return result

    def __truediv__(self, other: float) -> "SparseMatrix":
        result = SparseMatrix()
        for key in self:
            result[key] = self[key] / other
        return result

    def __neg__(self) -> "SparseMatrix":
        result = SparseMatrix()
        for key in self:
            result[key] = -self[key]
        return result

    def __pow__(self, other: float) -> "SparseMatrix":
        result = SparseMatrix()
        for key in self:
            result[key] = self[key] ** other
        return result

    def __rpow__(self, other: float) -> "SparseMatrix":
        result = SparseMatrix()
        for key in self:
            result[key] = other ** self[key]
        return result

    def __eq__(self, other: "SparseMatrix") -> bool:
        return self.data == other.data

    def __ne__(self, other: "SparseMatrix") -> bool:
        return self.data != other.data

    def __lt__(self, other: "SparseMatrix") -> bool:
        return self.data < other.data

    def __le__(self, other: "SparseMatrix") -> bool:
        return self.data <= other.data

    def __gt__(self, other: "SparseMatrix") -> bool:
        return self.data > other.data

    def __ge__(self, other: "SparseMatrix") -> bool:
        return self.data >= other.data

    def __abs__(self) -> "SparseMatrix":
        result = SparseMatrix()
        for key in self:
            result[key] = abs(self[key])
        return result

    def __round__(self) -> "SparseMatrix":
        result = SparseMatrix()
        for key in self:
            result[key] = round(self[key])
        return result

    def __floor__(self) -> "SparseMatrix":
        result = SparseMatrix()
        for key in self:
            result[key] = math.floor(self[key])
        return result

    def __ceil__(self) -> "SparseMatrix":
        result = SparseMatrix()
        for key in self:
            result[key] = math.ceil(self[key])
        return result

    def __trunc__(self) -> "SparseMatrix":
        result = SparseMatrix()
        for key in self:
            result[key] = math.trunc(self[key])
        return result
