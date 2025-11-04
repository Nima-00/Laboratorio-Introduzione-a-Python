# ------------------------------------
# Foglio Esercizi 0
# ------------------------------------

# Ex 1: Ordered Squared List

def sqord_(A: list=[]) -> list:
    '''
    Input: List of integers sorted in non-decreasing order
    Return: List of squares in non-decreasing order
    '''
    n = len(A)
    result = [0] * n
    i, j = 0, n - 1
    pos = n - 1
    while i <= j:
        left_sq = A[i] * A[i]
        right_sq = A[j] * A[j]
        if left_sq > right_sq:
            result[pos] = left_sq
            i += 1
        else:
            result[pos] = right_sq
            j -= 1
        pos -= 1
    return result

a = [-19, -4, -2, 1, 3, 5, 8]
print(sqord_(a))


# Ex 2: Ordered Squared List

def is_prime(n: int=0) -> bool:
    '''
    Input: Integer n
    Return: True if n is prime, False otherwise
    '''
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    i = 2
    while i*i <= n:
        if n%i==0:
            return False
        i += 1
    return True
