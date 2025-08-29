import numpy as np
import matplotlib.pyplot as plt

class LinealFunction:
    def __init__(self, m=0, b=0):
        """"Constructor de la clase"""
        #Parámetros instanciados
        self.m = m  #Pendiente
        self.b = b  #Corte con el eje y

    def evaluate(self, x):
        """Evalúa la función lineal f(x) = m*x + b"""
        return self.m * x + self.b

    def plot(self):
        """Dibuja la función lineal"""
        domain = np.arange(-4, 4, 0.1)
        f_range = self.evaluate(domain)

        plt.plot(domain, f_range, color='blue',
                 label=f'Línea recta con Pendiente {self.m} - Intercepto {self.b}')
        
        # 🔴 Corte con el eje Y: (0, b)
        plt.scatter(0, self.b, color='red', zorder=5, label=f"Corte eje Y (0,{self.b})")
        plt.text(0, self.b+0.5, f"(0,{self.b})", fontsize=9, ha='center', color='red')

        # 🔵 Corte con el eje X: (-b/m, 0), si m != 0
        if self.m != 0:
            x_intercept = -self.b / self.m
            plt.scatter(x_intercept, 0, color='green', zorder=5, label=f"Corte eje X ({x_intercept:.2f},0)")
            plt.text(x_intercept, 0.5, f"({x_intercept:.2f},0)", fontsize=9, ha='center', color='green')

        # Dibujar ejes
        plt.axhline(0, color='black')
        plt.axvline(0, color='black')

        plt.title(f'Función Lineal:', fontsize=14, pad=20, color='green')
        plt.xlabel('Eje x')
        plt.ylabel('Eje y')
        #[xmin, xmax, ymin, ymax]
        plt.axis([-4, 4, -10, 10])
        #Cuadrícula
        plt.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
        #Añadir leyenda al gráfico
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
