import numpy as np 
import pylab 
import random 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
random.seed(100)

def paseo_1d_plot(y):
    """
    este método representa una caminata aleatoria unidimensional
    """
    x, y = range(len(y)), y
    plt.plot(x, y)
    plt.plot(x[0], y[0], "ro"); plt.plot(x[-1], y[-1], "mo")
    plt.title("Paseo aleatorio unidimensional")
    plt.legend([str(len(y)-1)+" pasos"])
    plt.show()
def paseo_2d_plot(vector):
    """
    este método representa una caminata aleatoria sobre una cuadrícula 2-dimensional
    """
    (x, y) = vector
    pylab.plot(x, y)
    plt.plot(x[0], y[0], "ro"); plt.plot(x[-1], y[-1], "mo")
    pylab.title("Paseo aleatorio sobre cuadrícula 2D")
    pylab.legend([str(len(x)-1)+" pasos"])
    pylab.show()

def paseo_3d_plot(vector):
    """
    este método representa una caminata aleatoria sobre una cuadrícula 3-dimensional
    """
    (x, y, z) = vector
    ax = plt.subplot(1,1,1, projection="3d")
    ax.plot(x, y, z,alpha=0.9)
    ax.scatter(x[0],y[0],z[0], color = "r"); ax.scatter(x[-1],y[-1],z[-1], color = "m")
    pylab.title("Paseo aleatorio sobre cuadrícula 3D")
    pylab.legend([str(len(x)-1)+" pasos"])
    plt.show()

def gen_direccion(m):
    """
    este método genera una dirección y un sentido para la caminata sobre cuadrícula m-dimensional
    """
    direccion = random.randint(0,m-1)
    sentido = random.choice([1,-1])
    return (direccion, sentido)

def paseo_md(n, m):
    """ 
    este método realiza una simulación de caminata aleatoria sobre una cuadrícula m-dimensional de n pasos
    la salida es una matriz de m vectores de las posiciones (incluyendo la inicial) en cada coordenada
    """
    matrix = []
    for p in range(m):
        matrix.append(np.zeros(n+1))
    for paso in range(1, n+1): 
        (direccion, sentido) = gen_direccion(m)
        for h in range(m):
            matrix[h][paso] = matrix[h][paso-1]
        matrix[direccion][paso] += sentido
    return matrix

def paseo_md_plot(matrix):
    """
    este método representa una caminata aleatoria sobre una cuadrícula m-dimensional de n pasos
    con el menor número de gráficas posible y la mayor cantidad de gráficas tridimensionales posible
    """
    m = len(matrix)
    num_3d, num_2d, num_1d = m//3, int(m%3 == 2), int(m%3 == 1)
    for d3 in range(num_3d):
        paseo_3d_plot(matrix[d3:d3+3])
    for d2 in range(num_2d):
        paseo_2d_plot(matrix[-2:])
    for d1 in range(num_1d):
        paseo_1d_plot(matrix[-1])

paseo_md_plot(paseo_md(1000,4))

paseo_md_plot(paseo_md(1000,8))
