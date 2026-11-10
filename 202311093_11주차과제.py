import numpy as np
from fractions import Fraction
from math import lcm

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

A = np.array([
    [3, 2],
    [3, -2],
])

# 2. 고유값과 고유벡터 계산
eigenvalues, eigenvectors = np.linalg.eig(A)

for i in np.argsort(eigenvalues):
    eigenvalue = eigenvalues[i]
    vector = eigenvectors[:,i]

    # 이 문제의 고유벡터를 보기 쉬운 정수비로 변환
    vector = vector / vector[np.argmax(np.abs(vector))]
    fractions = [
        Fraction(float(t)).limit_denominator(1000)
        for t in vector
    ]
    common = lcm(*(f.denominator for f in fractions))
    x = np.array([int(f * common) for f in fractions])

    # 첫 번째 0이 아닌 성분을 양수로 통일
    if x[np.flatnonzero(x)[0]] < 0:
        x = -x
    print(f"\n고유값 λ = {eigenvalue:g}")
    print("고유벡터 x=", x)

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

print("행렬 A\n")
A = np.array([
    [0, 0, 0],
    [0, 2, 5],
    [0, 0, -1]
])

# 2. 고유값과 고유벡터 계산
eigenvalues, eigenvectors = np.linalg.eig(A)

for i in np.argsort(eigenvalues):
    eigenvalue = eigenvalues[i]
    vector = eigenvectors[:,i]

    # 이 문제의 고유벡터를 보기 쉬운 정수비로 변환
    vector = vector / vector[np.argmax(np.abs(vector))]
    fractions = [
        Fraction(float(t)).limit_denominator(1000)
        for t in vector
    ]
    common = lcm(*(f.denominator for f in fractions))
    x = np.array([int(f * common) for f in fractions])

    # 첫 번째 0이 아닌 성분을 양수로 통일
    if x[np.flatnonzero(x)[0]] < 0:
        x = -x
    print(f"\n고유값 λ = {eigenvalue:g}")
    print("고유벡터 x=", x)
print("행렬 B\n")
B = np.array([
    [4, 0, 0],
    [0, 0, 0],
    [1, 0, -3]
])
# 2. 고유값과 고유벡터 계산
eigenvalues, eigenvectors = np.linalg.eig(B)

for i in np.argsort(eigenvalues):
    eigenvalue = eigenvalues[i]
    vector = eigenvectors[:,i]

    # 이 문제의 고유벡터를 보기 쉬운 정수비로 변환
    vector = vector / vector[np.argmax(np.abs(vector))]
    fractions = [
        Fraction(float(t)).limit_denominator(1000)
        for t in vector
    ]
    common = lcm(*(f.denominator for f in fractions))
    x = np.array([int(f * common) for f in fractions])

    # 첫 번째 0이 아닌 성분을 양수로 통일
    if x[np.flatnonzero(x)[0]] < 0:
        x = -x
    print(f"\n고유값 λ = {eigenvalue:g}")
    print("고유벡터 x=", x)
