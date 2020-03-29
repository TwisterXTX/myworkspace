import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def func(x):
    return -(x-2)*(x-8)+40


x = np.linspace(0, 10)

y = func(x)

fig, ax = plt.subplots()

plt.plot(x, y, 'r', linewidth=2)

a = 2
b = 9

ax.set_xticks([a, b])
ax.set_yticks([])

ax.set_xticklabels([r'$a$', r'$b$'])

ix = np.linspace(a, b)
iy = func(ix)
ixy = zip(ix, iy)
# verts = [(a, 0)]
# for tmp in ix:
    # print(tmp)
    # verts = verts + [(ix(tmp), iy(tmp))]

# verts = verts + [(b, 0)]
verts = [(a, 0)]+list(ixy)+[(b, 0)]

poly = Polygon(verts, facecolor='g', edgecolor='r')
ax.add_patch(poly)
plt.figtext(0.9, 0.03, '$x$')

plt.figtext(0.1, 0.9, '$y$')

x_math = (a+b)*0.5
y_math = 35
plt.text(x_math, y_math, r'$ \int_a^b(-(x-2)*(x-8)+40)dx$', fontsize=12, horizontalalignment='center')
# plt.ylim(ymin=25)

plt.show()
