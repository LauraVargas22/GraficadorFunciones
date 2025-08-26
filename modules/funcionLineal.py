import numpy as np
import matplotlib.pyplot as plt

class LinealFunction:
    def __init__(self, m=0, b=0):
        self.m = m
        self.b = b

    def evaluate(self, x):
        """Evalúa la función lineal f(x) = m*x + b"""
        return self.m * x + self.b

    def plot(self):
        """Dibuja la función lineal"""
        domain = np.arange(-4, 4, 0.1)
        f_range = self.evaluate(domain)

        plt.plot(domain, f_range, color='blue',
                 label=f'Línea recta con Pendiente {self.m} - Intercepto {self.b}')
        
        # Dibujar ejes
        plt.axhline(0, color='black')
        plt.axvline(0, color='black')

        plt.xlabel('Eje x')
        plt.ylabel('Eje y')
        plt.axis([-4, 4, -10, 10])
        plt.grid()
        plt.legend()
        plt.show()


def pedir_valores():
    """Solicita valores al usuario con validación"""
    while True:
        try:
            m = float(input("Ingrese la pendiente (m): "))
            b = float(input("Ingrese el intercepto (b): "))
            return m, b
        except ValueError:
            print("⚠️ Error: Ingrese solo números.")
