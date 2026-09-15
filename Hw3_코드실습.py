# %%
def add_square_matrices(A,B):
    """같은 크기의 두 정방행렬을 더하여 새로운 행렬을 변환합니다."""
    n = len(A)

    # 두 행렬의 행 개수 확인
    if n == 0 or len(B) != n:
        raise ValueError("두 행렬은 비어 있지 않고 크기가 같아야 합니다.")

    # 각 행의 원소 개수가 n개인지 확인: n x n 정방행렬 검사
    if any(len(row) != n for row in A):
        raise ValueError("A는 정방행렬이어야 합니다.")

    if any(len(row) != n for row in B):
        raise ValueError("B는 A와 같은 크기의 정방행렬이어야 합니다.")

    # 결과를 저장할 n x n 행렬을 0으로 초기화
    C = [[0 for _ in range(n)] for _ in range(n)]

    # 같은 위치의 원소끼리 덧셈
    for i in range(n):       # 행 인덱스
        for j in range(n):   # 열 인덱스
            C[i][j] = A[i][j] + B[i][j]
    return C

# 두 정방행렬 정의
A = [
    [3, -1, 3],
    [0, 4 , 6],
    [2 , 7, -5]
]

B = [
    [0, -2, -4],
    [1, 6, -2],
    [1, -1, 2]
]


# %%
# 행렬 덧셈
C = add_square_matrices(A, B)

# 결과 출력
print("A + B =")
for row in C:
    print(row)

# %%
# A: 4행 3열 godfuf
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

# B: 3행 2열 행렬
B = [
    [1, 2],
    [3, 4],
    [5, 6]
]

# 행렬의 크기
rows_a = len(A)    # A의 행 개수: 4
cols_a = len(A[0]) # A의 열 개수: 3
rows_b = len(B)    # B의 행 개수: 3
cols_b = len(B[0]) # B의 열 개수: 2

# 행렬 곱셈 가능 여부 확인
if cols_a != rows_b:
    raise ValueError("A의 열 개수와 B의 행 개수가 같아야 합니다.")

# 결과 행렬 C: 4행 2열, 모든 원소를 0으로 초기화
C = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

# 행렬 곱셈
for i in range(rows_a):
    for j in range(cols_b):
        for k in range(cols_a):
            C[i][j] += A[i][k] * B[k][j]

# 결과 출력
print("A * B =")
for row in C:
    print(row)



# %%
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 대각합 계산
diagonal_sum = sum([matrix[i][i] for i in range(len(matrix))])

print("대각합 =", diagonal_sum)

# %%
import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("대각합 =", np.trace(matrix))