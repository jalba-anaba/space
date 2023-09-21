# Import Python3.9 Modules
import numpy as np # 数値計算ライブラリ
from scipy.integrate import odeint # 常微分方程式を解くライブラリ
import matplotlib.pyplot as plt # 描画ライブラリ

# 二体問題の運動方程式
def func(x, t):
    GM = 398600.4354360959 # 地球の重力定数, km3/s2
    r = np.linalg.norm(x[0:3])
    dxdt = [x[3],
            x[4],
            x[5],
            -GM*x[0]/(r**3),
            -GM*x[1]/(r**3),
            -GM*x[2]/(r**3)]
    return dxdt 

# 微分方程式の初期条件
x0 = [10000, 0, 0, 0, 7, 0] # 位置(x,y,z)＋速度(vx,vy,vz)
t  = np.linspace(0, 86400, 1000) # 1日分 軌道伝播

# 微分方程式の数値計算
sol = odeint(func, x0, t)


# 描画
plt.plot(sol[:, 0],sol[:, 1], 'b')
plt.grid() # 格子をつける
plt.gca().set_aspect('equal') # グラフのアスペクト比を揃える
plt.show()
import pykep as pk
GM = 132712440041.9393 # km3/s2
r, v = pk.par2ic([
                    149598261.1504, # a, km
                    0.01671123, # e, -
                    -2.6720990848033185e-07, # i, rad
                    0.0, # O, rad
                    1.796601474049171, # w, rad
                    0.0 # E, rad
                 ], GM)
print(r, v)
import numpy as np
import matplotlib.pyplot as plt # 描画ライブラリ
import pykep as pk

GM = 132712440041.9393 # km3/s2
ea_all = np.linspace(0, 2*np.pi, 1000) # 0 to 2pi radian

pos = np.array([ 
        pk.par2ic([
                    149598261.1504, # a, km
                    0.01671123, # e, -
                    -2.6720990848033185e-07, # i, rad
                    0.0, # O, rad
                    1.796601474049171, # w, rad
                    ea_t # E, rad
                   ], GM)[0] # 位置のみを取り出す
        for ea_t in ea_all
      ]) # Pythonのリスト内包表記を用いて，一括で計算

# 描画
plt.plot(pos[:,0],pos[:,1], 'b')
plt.grid() # 格子をつける
plt.gca().set_aspect('equal') # グラフのアスペクト比を揃える
plt.show()
from sgp4.api import Satrec, jday

# ISSのTLE
s = '1 25544U 98067A   21226.49389238  .00001429  00000-0  34174-4 0  9998'
t = '2 25544  51.6437  54.3833 0001250 307.1355 142.9078 15.48901431297630'

# SGP4による位置・速度の計算
satellite = Satrec.twoline2rv(s, t)
jd, fr = jday(2021, 8, 15, 0, 0, 0)
e, r, v = satellite.sgp4(jd, fr)

# 結果の出力
print(r)  # True Equator Mean Equinox position (km)
print(v)  # True Equator Mean Equinox velocity (km/s)