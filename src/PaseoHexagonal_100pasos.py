import numpy as np 
import pylab 
import random 
import matplotlib.pyplot as plt
random.seed(108)

def paseo_hexag(n):
    """ 
    este método realiza una simulación de caminata aleatoria sobre un mallado hexagonal de n pasos
    la salida es el vector de las variaciones en cada paso expresadas en las coordenadas elegidas (listas de 3 elementos)
    """
    variaciones = []
    direcciones = [(1,0,0), (0,1,0), (0,0,1)]
    for i in range(1, n+1): 
        direccion = random.choice(direcciones)
        variaciones.append(direccion)
    return variaciones

def paseo_hexag_plot(variaciones):
    """
    este método representa una caminata aleatoria sobre una mallado triangular
    """
    x, y = np.zeros(len(variaciones)+1), np.zeros(len(variaciones)+1)
    # traducimos de coordenadas triangulares a cartesianas, es decir sobre la cuadrícula
    for i in range(1, len(variaciones)):
        # se ha de distinguir la paridad de los vértices, pues la posición relativa de los vértices a los que es posible el desplazamiento cambia
        if i%2 == 1:
            if variaciones[i-1][0] == 1:
                desplazamiento = [1/2, 1/2]
            elif variaciones[i-1][1] == 1:
                desplazamiento = [0, -1]
            else:
                desplazamiento = [-1/2, 1/2]
        else:
            if variaciones[i-1][0] == 1:
                desplazamiento = [-1/2, -1/2]
            elif variaciones[i-1][1] == 1:
                desplazamiento = [0, 1]
            else:
                desplazamiento = [1/2, -1/2]
        x[i] = x[i-1] + desplazamiento[0]
        y[i] = y[i-1] + desplazamiento[1]
    pylab.plot(x[:-1], y[:-1])
    plt.plot(x[0], y[0], "ro")
    plt.plot(x[-2], y[-2], "mo")
    pylab.title("Paseo aleatorio sobre mallado hexagonal")
    pylab.legend([str(len(variaciones))+" pasos"])
    plt.savefig(f"PaseoHexagonal_{str(len(y)-1)}pasos.jpg", dpi=200)

paseo_hexag_plot(paseo_hexag(100))
