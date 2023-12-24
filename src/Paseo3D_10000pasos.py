import numpy as np
import random 
import matplotlib.pyplot as plt 
import pylab
from mpl_toolkits.mplot3d import Axes3D
random.seed(101)

def paseo_3d(n):
    """ 
    este método realiza una simulación de caminata aleatoria sobre una cuadrícula 3-dimensional de n pasos
    la salida es una terna de vectores de las posiciones (incluyendo la inicial) en cada coordenada
    """
    x, y, z, direcciones = np.zeros(n+1), np.zeros(n+1), np.zeros(n+1), [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0)]
    for i in range(1, n+1): 
        direccion = random.choice(direcciones)
        x[i], y[i], z[i] = x[i-1] + direccion[0], y[i-1] + direccion[1], z[i-1] + direccion[2]
    return (x, y, z)

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
    plt.savefig(f"Paseo3D_{str(len(y)-1)}pasos.jpg", dpi=200)

paseo_3d_plot(paseo_3d(10**5))
