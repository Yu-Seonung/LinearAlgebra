import numpy as np

np.set_printoptions(precision=4, suppress=True, floatmode="fixed")

# 행렬 A와 문제에 주어진 벡터 x
A = np.array([
    [1, 2],
    [4, 3],
], dtype=float)

x = np.array([1, 2], dtype=float)

# 1. 전체 고유값과 고유벡터 계산
eigenvalues, eigenvectors = np.linalg.eig(A)

# 고유값을 내림차순으로 정렬
order = np.argsort(eigenvalues)[::-1]

print("고유값과 대표 고유벡터")

for i in order:
    vector = eigenvectors[:, i]

    # 첫 번째 0이 아닌 성분을 1로 맞추기
    first = np.flatnonzero(np.abs(vector) > 1e-12)[0]
    vector = vector / vector[first]

    print(f"λ = {eigenvalues[i]:g}, 고유벡터 = {vector}")

# 2. 주어진 벡터 x에 대해 Ax = 5x 확인
Ax = A @ x

print("\nx =", x)
print("Ax =", Ax)
print("5x =", 5 * x)
print("Ax = 5x인가?", np.allclose(Ax, 5 * x))
