import matplotlib.pyplot as plt
#from sklearn.linear_model import LinearRegression
from scipy.optimize import curve_fit
import numpy as np
import matplotlib as mpl
from math import *
sigma_nu=1
sigma_n = 0
nu1=np.array([134.3,271,407,542,681,819,957,1096,1237])
n1=np.array([1,2,3,4,5,6,7,8,9])
nu2=np.array([163.6,325,487,651,814,978,1143,1309,1475])
n2=np.array([1,2,3,4,5,6,7,8,9])
nu3=np.array([185.7,373,560,748,934,1124,1311,1502,1690])
n3=np.array([1,2,3,4,5,6,7,8,9])
nu4=np.array([206.4,413,621,828,1036,1244,1452,1661,1872])
n4=np.array([1,2,3,4,5,6,7,8,9])
nu5=np.array([223.9,450,675,901,1125,1354,1578,1808,2034])
n5=np.array([1,2,3,4,5,6,7,8,9])
# u = nu
# v = n
# sigma_u = sigma_nu/n
# sigma_v =sigma_n/n
# print(sigma_u/u, '\n', sigma_v/v)
# относительные погрешности
# plt.plot(v, u, "+")
def f(v,u):
    mu = np.mean(u) # средее
    mv = np.mean(v)
    mv2 = np.mean(v**2) # средний квадрат
    mu2 = np.mean(u**2)
    muv = np.mean (u * v) # среднее от произведения
    k = (muv - mu * mv) / (mv2 - mv**2)
    N = len(v) # число точек
    sigma_k = np.sqrt(( (mu2 - mu**2)/(mv2 - mv**2)-k**2)/N)
    print("k = ", k,"sigma_k=", sigma_k)
    return (k)
# np.polyfit(v, u, 1)
plt.figure(figsize=(8,6), dpi=100) # размер графика
plt.ylabel("$nu $, $Гц$") # подписи к осям
plt.xlabel("$n$")
plt.title('Рис.2. Наилучшая прямая для линеаризованной зависимости $nu(n)$') # заголовок˓→графика
plt.grid(True, linestyle="--") # сетка
x = np.array([0,10]) # две точки аппроксимирующей прямой
plt.plot(x, f(n1,nu1) * x , "-r",linewidth=1, label="Линейная аппроксимация") # аппроксимация
plt.errorbar(n1, nu1, xerr=sigma_n, yerr=sigma_nu, fmt="ok", label="Экспериментальные точки") # точки с погрешностями
plt.plot(x, f(n2,nu2) * x , "-b",linewidth=1, label="Линейная аппроксимация") # аппроксимация
plt.errorbar(n2, nu2, xerr=sigma_n, yerr=sigma_nu, fmt="ok") # точки с погрешностями
plt.plot(x, f(n3,nu3) * x , "-g",linewidth=1, label="Линейная аппроксимация") # аппроксимация
plt.errorbar(n3, nu3, xerr=sigma_n, yerr=sigma_nu, fmt="ok") # точки с погрешностями
plt.plot(x, f(n4,nu4) * x , "-y",linewidth=1, label="Линейная аппроксимация") # аппроксимация
plt.errorbar(n4, nu4, xerr=sigma_n, yerr=sigma_nu, fmt="ok") # точки с погрешностями
plt.plot(x, f(n5,nu5) * x , "-o",linewidth=1, label="Линейная аппроксимация") # аппроксимация
plt.errorbar(n5, nu5, xerr=sigma_n, yerr=sigma_nu, fmt="ok") # точки с погрешностями
plt.legend() # легенда
# print("I0 = %.3f" % I0)
# M = k
# print("M = %.3f г" % M)
# N = len(v) # число точек
# sigma_k = np.sqrt(( (mu2 - mu**2)/(mv2 - mv**2)-k**2)/N )
# sigma_b = sigma_k * np.sqrt(mv2)
# sigma_I0 = sigma_k / k * I0
# sigma_M = M * np.sqrt( (sigma_b / b)**2 + (sigma_I0 / I0)**2 )
# print("sigma_k = %.3f" % (sigma_k))



plt.show()
