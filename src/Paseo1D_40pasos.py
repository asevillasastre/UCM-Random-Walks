import numpy as np
import random 
import matplotlib.pyplot as plt 
random.seed(10)

def paseo_1d(n):
    """ 
    este método realiza una simulación de caminata aleatoria unidimensional de n pasos
    la salida es un vector de las posiciones, incluyendo la inicial
    """
    y = np.zeros(n+1)
    for i in range(1, n+1): 
        y[i] = y[i-1] + random.choice([-1,1])
    return y

def paseo_1d_plot(y):
    """
    este método representa una caminata aleatoria unidimensional
    """
    x, y = range(len(y)), y
    plt.plot(x, y)
    plt.plot(x[0], y[0], "ro"); plt.plot(x[-1], y[-1], "mo")
    plt.title("Paseo aleatorio unidimensional")
    plt.legend([str(len(y)-1)+" pasos"])
    plt.savefig(f"Paseo1D_{str(len(y)-1)}pasos.jpg", dpi=200)
    
paseo_1d_plot(paseo_1d(40))