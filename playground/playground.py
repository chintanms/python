
import os
import numpy as np
import matplotlib.pyplot as plt 


#np.random.seed(123987)

def eval_poly(coeffs, x):
    result = 0
    for a in coeffs:
        result = x*result + a
    return result

def fact(n) :
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


def plot_algo_complexity_lines():

    x1 = np.arange(1, 46, 1)
    y_log = np.log2(x1)
    y_linear = x1
    y_nlogn = x1 * np.log2(x1)
    y_quad = x1 * x1
    y_poly = [eval_poly([1, 1, 1], i) for i in x1]

    x_exp = np.arange(1, 12)
    y_exp = np.exp2(x_exp)

    x_fact = np.arange(1, 8)
    y_fact = [fact(n) for n in x_fact]

    x_pow = np.arange(1, 6)
    y_pow = [n**n for n in x_pow]

    plt.plot(x1, y_log)
    plt.plot(x1, y_linear)
    plt.plot(x1, y_nlogn)
    plt.plot(x1, y_quad)
    plt.plot(x1, y_poly)
    plt.plot(x_exp, y_exp)
    plt.plot(x_fact, y_fact)
    plt.plot(x_pow, y_pow)
    plt.legend(['Log', 'Linear', '$n*log(n)$', 'Quadratic', 'Polynomial: $x^2+x+1$', 'Exp: $2^n$', 'Factorial: $n!$', 'Power: $n^n$'])

    plt.show()


plot_algo_complexity_lines()
