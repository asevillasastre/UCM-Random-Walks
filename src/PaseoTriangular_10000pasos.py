import numpy as np 
import pylab 
import random 
import matplotlib.pyplot as plt
import math
random.seed(11)

def paseo_triang(n):
    """ 
    este método realiza una simulación de caminata aleatoria sobre un mallado triangular de n pasos
    en este caso la salida es un diccionario de listas que contienen las posiciones y las variaciones en cada paso expresadas en las coordenadas elegidas (listas de 3 elementos)
    """
    x = []
    for k in range(n+1):
        x.append([0,0,0])
    variaciones = []
    direcciones = [(0,1,-1), (0,-1,1), (1,0,-1), (-1,0,1), (1,-1,0), (-1,1,0)]
    for i in range(1, n+1): 
        direccion = random.choice(direcciones)
        variaciones.append(direccion)
        for coord in range(3):
            x[i][coord] = x[i-1][coord] + direccion[coord]
    return {"posiciones": x, "variaciones": variaciones}

def paseo_triang_plot(diccionario):
    """
    este método representa una caminata aleatoria sobre una mallado triangular
    """
    x, y = np.zeros(len(diccionario["posiciones"])), np.zeros(len(diccionario["posiciones"]))
    # traducimos de coordenadas triangulares a cartesianas, es decir sobre la cuadrícula
    for i in range(1, len(diccionario["variaciones"])):
        if diccionario["variaciones"][i-1][0] == 0:
            desplazamiento = [diccionario["variaciones"][i-1][1]/2, - diccionario["variaciones"][i-1][1]]
        elif diccionario["variaciones"][i-1][1] == 0:
            desplazamiento = [diccionario["variaciones"][i-1][0], 0]
        else:
            desplazamiento = [diccionario["variaciones"][i-1][0]/2, diccionario["variaciones"][i-1][0]]
        x[i] = x[i-1] + desplazamiento[0]
        y[i] = y[i-1] + desplazamiento[1]
    pylab.plot(x[:-1], y[:-1])
    plt.plot(x[0], y[0], "ro")
    plt.plot(x[-2], y[-2], "mo")
    pylab.title("Paseo aleatorio sobre mallado triangular")
    pylab.legend([str(len(diccionario["variaciones"]))+" pasos"])
    plt.savefig(f"PaseoTriang_{str(len(y)-1)}pasos.jpg", dpi=200)

paseo_triang_plot(paseo_triang(10000))


