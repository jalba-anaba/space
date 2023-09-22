import numpy as np
import matplotlib.pyplot as plt

# グリッドの設定
N = 100  # グリッドの数
x_start, x_end = -2.0, 2.0  # x軸方向の範囲
y_start, y_end = -1.0, 1.0  # y軸方向の範囲
x = np.linspace(x_start, x_end, N)
y = np.linspace(y_start, y_end, N)
X, Y = np.meshgrid(x, y)

# 渦電流のパラメータ
gamma = 5.0  # 渦の強さ
x_vortex, y_vortex = 0.0, 0.0  # 渦の中心座標

# 渦電流の速度場の計算
u_vortex = gamma / (2 * np.pi) * (Y - y_vortex) / ((X - x_vortex)**2 + (Y - y_vortex)**2)
v_vortex = -gamma / (2 * np.pi) * (X - x_vortex) / ((X - x_vortex)**2 + (Y - y_vortex)**2)

# 流れ場の速度場の計算
u = u_vortex
v = v_vortex

# 流れ場のポテンシャルの計算
phi = gamma / (2 * np.pi) * np.arctan2((Y - y_vortex), (X - x_vortex))

# 流れ場のストリームラインのプロット
plt.figure(figsize=(8, 4))
plt.streamplot(X, Y, u, v, density=2, linewidth=1, arrowsize=1, arrowstyle='->')
plt.scatter(x_vortex, y_vortex, color='red', marker='o', s=80)
plt.xlim(x_start, x_end)
plt.ylim(y_start, y_end)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Vortex Flow')
pip install matplotlib