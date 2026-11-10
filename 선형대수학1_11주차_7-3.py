import numpy as np

A = np.array([
    [3, -1, -1],
    [-12, 0, 5],
    [4, -2, -1],
], dtype=float)

# 고유값과 고유벡터 계산
eigenvalues, X = np.linalg.eig(A)

# MATLAB 화면처럼 고유값을 2, 1, -1 순서로 정렬
order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[order]
X = X[:, order]

# 고유값을 대각행렬로 변환
lamda = np.diag(eigenvalues)

np.set_printoptions(precision=4, suppress=True, floatmode="fixed")

print("X =")
print(X)
print("\nlamda =")
print(lamda)