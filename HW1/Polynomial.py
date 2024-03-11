# Author: 林凡皓
# Date: 2024/3/2
# Purpose: 建立一個Polynomial class，其中包含多項是相加、多項式相減、多項式相乘和多項式取負號的功能。
#          多項式如何顯示出來已經定義在__str__(self)
#          __init__(self, coefficients)為初始化，定義self._coeff為輸入的coefficients list，定義self._degree為多項式最高次方。

class Polynomial:
    """
    Class implementation of a polynomial. The polynomial coefficients are 
    represented in a list in descending order of their degrees.
    """
    def __init__(self, coefficients):
        """
        Initialize the Polynomial instance.

        Args:
            coefficients (list): A list of coefficients, starting with the 
                                 coefficient of the highest degree term.
        """
        self._coeff = coefficients                     # Big O : O(1)
        while self._coeff and self._coeff[0] == 0:     # Big O : O(n)
            self._coeff = self._coeff[1:]             
        self._degree = len(self._coeff) - 1            # Big O : O(1)


    def __add__(self, other):
        """
        Add two polynomials.

        Args:
            other (Polynomial): Another Polynomial instance to add.

        Returns:
            Polynomial: The sum of the two polynomials.
        """
        
        diff = abs(len(self._coeff) - len(other._coeff))                  # Big O : O(1)

        if len(self._coeff) < len(other._coeff):      
            result = [0] * len(other._coeff)                              # Big O : O(k)
            result[:diff] = other._coeff[:diff]                           # Big O : O(k)
            for i in range(len(self._coeff)):                             # Big O : O(n)
                result[diff+i] = self._coeff[i] + other._coeff[diff+i]     
        else:
            result = [0] * len(self._coeff)                               # Big O : O(n) 
            result[:diff] = self._coeff[:diff]                            # Big O : O(n)
            for i in range(len(other._coeff)):                            # Big O : O(k)
                result[diff+i] = self._coeff[diff+i] + other._coeff[i]

        return Polynomial(result)

    def __sub__(self, other):
        """
        Subtract one polynomial from another.

        Args:
            other (Polynomial): Another Polynomial instance to subtract.

        Returns:
            Polynomial: The result of the subtraction.
        """
        
        diff = abs(len(self._coeff) - len(other._coeff))                  # Big O : O(1)

        if len(self._coeff) < len(other._coeff):         
            result = [0] * len(other._coeff)                              # Big O : O(k)
            result[:diff] = [-num for num in other._coeff[:diff]]         # Big O : O(k)
            for i in range(len(self._coeff)):                             # Big O : O(n)
                result[diff+i] = self._coeff[i] - other._coeff[diff+i]     
        else:
            result = [0] * len(self._coeff)                               # Big O : O(n)
            result[:diff] = self._coeff[:diff]                            # Big O : O(n) 
            for i in range(len(other._coeff)):                            # Big O : O(k)
                result[diff+i] = self._coeff[diff+i] - other._coeff[i]
        return Polynomial(result)
    
    def __mul__(self, other):
        """
        Multiply two polynomials.

        Args:
            other (Polynomial): Another Polynomial instance to multiply with.

        Returns:
            Polynomial: The product of the two polynomials.
        """

        result = [0]*(self._degree + other._degree + 1)      # Big O : O(n+k)

        # print (s_coeff, o_coeff)
        for i,self_coeff in enumerate(self._coeff):          # Big O : O(n)
           for j,other_coeff in enumerate(other._coeff):     # Big O : O(k)
                result[i+j] += (self_coeff * other_coeff)
                # print(i,j)
        return Polynomial(result)
            
    
    def __neg__(self):
        """
        Negate the polynomial.

        Returns:
            Polynomial: A new Polynomial instance representing the negation of the current polynomial.
        """

        num = len(self._coeff)                # Big O : O(1)
        result = []                           # Big O : O(1)
        for i in range(num):                  # Big O : O(n)
             result.append(-self._coeff[i])

        return Polynomial(result)
    


    #### Do not modify the code below ####
    def __str__(self):
        """
        String representation of the polynomial.

        Returns:
            str: A human-readable string representing the polynomial.
        """
        terms = []
        first_term = True

        for i, coeff in enumerate(self._coeff):
            power = len(self._coeff) - i - 1
            if abs(coeff) > 1e-9:
                # Format coefficient and power
                coeff_str = "" if abs(coeff) == 1 and power != 0 else f"{coeff:.4f}".rstrip('0').rstrip('.')
                if power == 0:
                    term = coeff_str
                elif power == 1:
                    term = f"{coeff_str}x"
                else:
                    term = f"{coeff_str}x^{power}"
                # Add sign and format term
                if coeff > 0 and not first_term:
                    term = "+ " + term
                elif coeff < 0:
                    term = "- " + term.lstrip('-')
                terms.append(term)
                first_term = False

        return ' '.join(terms) if terms else "0"

    def __repr__(self):
        """
        Official string representation of the polynomial, for debugging.

        Returns:
            str: The same as __str__ for readability.
        """
        return self.__str__()
    #### Do not modify the code above ####