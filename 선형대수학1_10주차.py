import matplotlib.pyplot as plt
import numpy as np

# 1. 3D 플롯 설정
fig = plt.figure(figsize=(9, 8))
ax = fig.add_subplot(111, projection='3d')

# 2. 벡터 정의
origin = np.array([0, 0, 0])
v1 = np.array([0, 1, 1])
v2 = np.array([1, 0, 1])
v3 = np.array([1, 1, 2])

# 3. 생성되는 평면 V 그리기 (z = x + y)
x_vals = np.linspace(-0.5, 1.8, 10)
y_vals = np.linspace(-0.5, 1.8, 10)
X, Y = np.meshgrid(x_vals, y_vals)
Z = X + Y

ax.plot_surface(X, Y, Z, alpha=0.2, color='cyan', edgecolor='none')

# 4. 세 벡터 그리기 (화살표)
# quiver 인자: x, y, z 시작점, u, v, w 벡터 성분
vectors = [
    (v1, 'blue', r'$v_1=(0,1,1)$'),
    (v2, 'green', r'$v_2=(1,0,1)$'),
    (v3, 'red', r'$v_3=v_1+v_2=(1,1,2)$'),
]

for vec, color, label in vectors:
    ax.quiver(
        0, 0, 0,
        vec[0], vec[1], vec[2],
        color=color,
        arrow_length_ratio=0.08,
        linewidth=2.2,
        label=label,
    )

# 5. 평행사변형 법칙 시각화 (점선 연결)
# v1 끝점 -> v3 끝점 (v2 방향 이동)
ax.plot(
    [v1[0], v3[0]],
    [v1[1], v3[1]],
    [v1[2], v3[2]],
    'k--',
    linewidth=1.2,
    alpha=0.7,
)
# v2 끝점 -> v3 끝점 (v1 방향 이동)
ax.plot(
    [v2[0], v3[0]],
    [v2[1], v3[1]],
    [v2[2], v3[2]],
    'k--',
    linewidth=1.2,
    alpha=0.7,
)

# 6. 각 점 텍스트 및 마커 표시
points = {
    r'$O(0,0,0)$': origin,
    r'$v_1$': v1,
    r'$v_2$': v2,
    r'$v_3$': v3,
}

for name, pt in points.items():
    ax.scatter(pt[0], pt[1], pt[2], color='black', s=25)
    ax.text(pt[0] + 0.05, pt[1] + 0.05, pt[2] + 0.05, name, fontsize=11)

# 7. 축 범위 및 라벨 설정
ax.set_xlim([-0.5, 2.0])
ax.set_ylim([-0.5, 2.0])
ax.set_zlim([-0.5, 2.5])

ax.set_xlabel('X axis', fontsize=11)
ax.set_ylabel('Y axis', fontsize=11)
ax.set_zlabel('Z axis', fontsize=11)
ax.set_title(
    r'Visualization of $V = \mathrm{span}\{v_1, v_2, v_3\}$ and $v_3 = v_1 + v_2$',
    fontsize=13,
)

# 보기 좋은 시점 각도 설정 (고도 25도, 방위각 45도)
ax.view_init(elev=25, azim=45)
ax.legend(loc='upper left', fontsize=10)
plt.tight_layout()

# 대화형 창 출력 (직접 마우스로 회전 가능)
plt.show()