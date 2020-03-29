
'''
matplotlib画图常规步骤（OOP思想）
参考：http://www.pynumerical.com/archives/76/
1.创建画布和子图（一个或者多个）
fig,ax = plt.subplots() # 创建一个子图
fig,(ax0,ax1) = plt.subplots(2,1) # 创建两行一列两个子图

3.在子图axes中进行各种图形的绘制，标签、曲线，图例等
曲线 ax.scatter() /数据标签 ax.legend() /题目 ax.set_title /网格 ax.grid() /坐标名称 ax.set_xlabel()，ax.set_ylabel()
'''
import numpy as np
import matplotlib.pyplot as plt

fig, (ax0, ax1) = plt.subplots(2, 1)

x = np.linspace(0, 2*np.pi, 50)
y1 = np.sin(x)
y2 = np.cos(x)

ax0.plot(x, y1, 'r')
ax0.legend('sin(x)')
ax1.plot(x, y2, 'g')
ax1.legend('cos(x)')
ax0.set_title('title test')

plt.show()