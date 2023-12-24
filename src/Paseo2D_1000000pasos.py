import numpy as np
import random 
import matplotlib.pyplot as plt 
import pylab
random.seed(14)

def paseo_2d(n):
    """ 
    este método realiza una simulación de caminata aleatoria sobre una cuadrícula 2-dimensional de n pasos
    la salida es una tupla de vectores de las posiciones (incluyendo la inicial) en cada coordenada
    """
    x, y, direcciones = np.zeros(n+1), np.zeros(n+1), [(0,1), (0,-1), (1,0), (-1,0)]
    for i in range(1, n+1): 
        direccion = random.choice(direcciones)
        x[i], y[i] = x[i-1] + direccion[0], y[i-1] + direccion[1]
    return (x, y)

def paseo_2d_plot(vector):
    """
    este método representa una caminata aleatoria sobre una cuadrícula 2-dimensional
    """
    (x, y) = vector
    pylab.plot(x, y)
    plt.plot(x[0], y[0], "ro"); plt.plot(x[-1], y[-1], "mo")
    pylab.title("Paseo aleatorio sobre cuadrícula 2D")
    pylab.legend([str(len(x)-1)+" pasos"])
    plt.savefig(f"Paseo2D_{str(len(y)-1)}pasos.jpg", dpi=200)

paseo_2d_plot(paseo_2d(10**6))
