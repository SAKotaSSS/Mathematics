import numpy as np
                           # 場合によって使う
x = 3                      # float(input("x成分："))
y = 2                      # float(input("y成分："))
z = 4                      # float(input("z成分："))
vector3 = [x, y, z]

# x軸に沿って、n平行移動
n = 3
nvector3 = [x + n, y, z]
print(nvector3)

# 回転移動させる為の行列を生成
p = (1/3) * np.pi
Rs = np.array([[1, 0, 0],[0, np.cos(p), (-1) * np.sin(p)],[0, np.sin(p), np.cos(p)]])
print(Rs)
avector3 = []
for i in range(0, 3):
    sum = 0
    for k in range(0, 3):
        s = nvector3[i]*Rs[i][k]
        sum = sum + s
    avector3.append(sum)

print(avector3)