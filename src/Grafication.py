import numpy as np
import matplotlib.pyplot as plt

# rango de valores
x = np.linspace(-10, 10, 400)

# funciones de activación
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha*x)

def softplus(x):
    return np.log(1 + np.exp(x))

# lista de funciones
funciones = [
    ("Sigmoid", sigmoid),
    ("Tanh", tanh),
    ("ReLU", relu),
    ("Leaky ReLU", leaky_relu),
    ("Softplus", softplus)
]

# graficar
for nombre, funcion in funciones:
    y = funcion(x)
    
    plt.figure()
    plt.plot(x, y, label=nombre)
    plt.title(f"Función de Activación: {nombre}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    
    plt.show()