import numpy as np
import matplotlib.pyplot as plt

class QuadraticFunction:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def evaluate(self, x):
        """Evalúa la función cuadrática f(x) = ax² + bx + c"""
        return self.a * x**2 + self.b * x + self.c
    
    def vertex(self):
        """Calcula el vértice de la parábola"""
        if self.a == 0:
            return None
        x_v = -self.b / (2 * self.a)
        y_v = self.evaluate(x_v)
        return (x_v, y_v)
    
    def roots(self):
        """Calcula las raíces reales (si existen)"""
        if self.a == 0:
            return None
        discriminant = self.b**2 - 4*self.a*self.c
        if discriminant < 0:
            return []  # No hay raíces reales
        elif discriminant == 0:
            x = -self.b / (2*self.a)
            return [x]
        else:
            root_disc = np.sqrt(discriminant)
            x1 = (-self.b + root_disc) / (2*self.a)
            x2 = (-self.b - root_disc) / (2*self.a)
            return [x1, x2]
    
    def plot(self):
        """Dibuja la función cuadrática con vértice y raíces"""
        domain = np.arange(-6, 6, 0.1)
        f_range = self.evaluate(domain)

        plt.plot(domain, f_range, color='blue',
                 label=f'f(x) = {self.a}x² + {self.b}x + {self.c}')

        # Ejes
        plt.axhline(0, color='black')
        plt.axvline(0, color='black')

        # Vértice
        vertex = self.vertex()
        if vertex:
            plt.scatter(*vertex, color='red', zorder=5, label=f'Vertice {vertex}')

        # Raíces
        roots = self.roots()
        if roots and len(roots) > 0:
            for i, r in enumerate(roots):
                plt.scatter(r, 0, color='green', zorder=5, label=f'Raíz {i+1}: {r:.2f}')
        else:
            # Mensaje más prominente cuando no hay raíces reales
            plt.text(3, -15, "⚠️ NO TIENE RAÍCES REALES", fontsize=9,
                 color="black", ha="center", weight='bold',
                 bbox=dict(facecolor='white', alpha=0.8, edgecolor='purple', boxstyle='round,pad=0.5'))

        plt.xlabel('Eje x')
        plt.ylabel('Eje y')
        plt.axis([-6, 6, -20, 20])
        plt.grid()
        plt.legend()
        plt.show()

def pedir_valores():
    """Solicitar valores al usuario con validación"""
    while True:
        try:
            a = float(input("Ingrese a: "))
            b = float(input("Ingrese b: "))
            c = float(input("Ingrese c: "))
            return a, b, c
        except ValueError:
            print("⚠️ Error: Ingrese solo números.")


