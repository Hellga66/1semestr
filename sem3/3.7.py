import numpy as np

def f(matrix):
    A = matrix[:, :-1]  
    b = matrix[:, -1]    
    try:
        solution = np.linalg.solve(A, b)
        return solution
    except np.linalg.LinAlgError as e:
        return f"Ошибка при решении системы: {e}"
matrix = np.array([[2,2,-1,7],[2,-1,2,1],[-1,2,2,1]])
print(f(matrix))