import numpy as np
from fractions import Fraction
from math import lcm

np.set_printoptions(precision=4, suppress=True, floatmode="fixed")

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