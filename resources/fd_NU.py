#import sympy as sp
#
#b, c, a, hr, hl, beta = sp.symbols('f(b) f(c) f(a) h_r h_l beta')
#fp, fpp = sp.symbols('f\'(a) f\'\'(a)')
#
#eq1 = sp.Eq(b, a + fp*hr + fpp*hr*hr/2)
#eq2 = sp.Eq(c, a - fp*hl + fpp*hl*hl/2)
#eq3 = sp.Eq(beta, hr/hl)
#
#sp.pprint(eq1)
#sp.pprint(eq2)
#sp.pprint(eq3)
#
#res = sp.solve([eq1, eq2, eq3], (fp, fpp, hl))
#sp.pprint(res)

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 200)
y = np.sin(x) + 2*x - x**2 - 2

dy = 2 - 2*x + np.cos(x)

h = np.mean(np.diff(x))
rdisp = (np.random.rand(x.shape[0] - 2) - 0.5)*(h/2)
x[1:-1] += rdisp

y = np.sin(x) + 2*x - x**2 - 2

hr = x[2:] - x[1:-1]
hl = x[1:-1] - x[:-2]
beta = hr/hl

dyn = (-(beta**2)*y[:-2] + (beta**2 - 1)*y[1:-1] + y[2:])/(hr*(beta + 1))

plt.plot(x, dy)
plt.plot(x[1:-1], dyn)
plt.show()
