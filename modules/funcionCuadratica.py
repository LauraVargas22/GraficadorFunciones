import numpy as np
import matplotlib.pyplot as plt

class QuadraticFunction:
    #Constructor de la Clase
    def __init__(self, a=0, b=0, c=0):
        #Parámetros instanciados
        self.a = a #Coeficiente cuadrático
        self.b = b #Coeficiente lineal
        self.c = c #Término indefinido

    def evaluate(self, x):
        """Evalúa la función cuadrática f(x) = ax² + bx + c"""
        return self.a * x**2 + self.b * x + self.c
    
    def vertex(self):
        """Calcula el vértice de la parábola"""
        if self.a == 0:
            return None
        #Evalúa el corte con el eje x
        x_v = -self.b / (2 * self.a)
        #Evalua el corte en el eje y, teniendo en cuenta el corte en el eje x
        y_v = self.evaluate(x_v)
        return (x_v, y_v)
    
    def roots(self):
        """Calcula las raíces reales (si existen)"""
        #Evalua que a no sea 0
        if self.a == 0:
            return None
        #Discriminante = b² - 4ac
        discriminant = self.b**2 - 4*self.a*self.c
        #Si el discriminante es < 0, no hay raíces reales
        if discriminant < 0:
            return []  # No hay raíces reales
        #Si el discriminante es = 0, hay una raíz real
        elif discriminant == 0:
            x = -self.b / (2*self.a)
            return [x]
        #Si el discriminante es > 0, hay dos raíces reales distintas
        else:
            root_disc = np.sqrt(discriminant)
            #Evalua las raíces con la ecuación cuadrática
            x1 = (-self.b + root_disc) / (2*self.a)
            x2 = (-self.b - root_disc) / (2*self.a)
            return [x1, x2]
    
    def plot(self):
        """Dibuja la función cuadrática con vértice y raíces"""
        domain = np.arange(-6, 6, 0.1)
        f_range = self.evaluate(domain)

        #Etiqueta con la función
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
        #Si hay raíces, evalúa la lista con las raíces almacenadas
        if roots and len(roots) > 0:
            for i, r in enumerate(roots):
                plt.scatter(r, 0, color='green', zorder=5, label=f'Raíz {i+1}: {r:.2f}')
        else:
            #En caso de no tener raíces reales
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


