import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x ** 2

a = 0  
b = 2  


num_points = 10000

x_random = np.random.uniform(a, b, num_points)
y_random = np.random.uniform(0, max(f(x_random)), num_points)

points_under_curve = sum(y_random <= f(x_random))

rectangle_area = (b - a) * max(f(x_random))
curve_area = (points_under_curve / num_points) * rectangle_area

print("Інтеграл методом Монте-Карло: ", curve_area)

plt.plot(x_random, y_random, 'b.', markersize=1)
plt.plot(np.linspace(a, b), f(np.linspace(a, b)), 'r-', linewidth=2)
plt.fill_between(np.linspace(a, b), f(np.linspace(a, b)), color='gray', alpha=0.3)
plt.xlim([a, b])
plt.ylim([0, max(f(x_random)) + 0.1])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()


result, error = spi.quad(f, a, b)
print("Інтеграл за допомогою функції quad: ", result)