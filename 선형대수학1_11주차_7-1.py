import numpy as np

A = np.array([
    [2, 3],
    [3, -6],
], dtype=float)

# 고유값과 고유벡터 계산
eigenvalues, X = np.linalg.eig(A)

# MATLAB 화면처럼 고유값을 2, 1, -1 순서로 정렬
order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[order]
X = X[:, order]

np.set_printoptions(precision=4, suppress=True, floatmode="fixed")
coefficients = (-1) ** len(A) * np.poly(A)
print("특성다항식 det(A - λ |):")
print(np.poly1d(np.round(coefficients, 10), variable="λ"))

print(eigenvalues)