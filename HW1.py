import numpy as np
import matplotlib.pyplot as plt
import os


def task1():
    os.mkdir("results")
    f = open('results/task_01_4O-506C_Litvarov_3.txt', 'w')
    x = np.arange(-15, -5,0.1)
    print(' x \t f(x)', file=f)
    y = 100 * np.sqrt( abs( 1 - 0.01 * x**2 )) + 0.01 * abs( x+10 )
    for i in range(len(x)):
        print(x[i], '\t', y[i], file=f, end="\n")
    f.close()
    plt.figure()
    plt.plot(x, y)
    plt.grid()
    plt.savefig('image.png')
    plt.show()


if os.path.exists('results'):
    os.remove('results/task_01_4O-506C_Litvarov_3.txt')
    os.rmdir("results")
task1()


