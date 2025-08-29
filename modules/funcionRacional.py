import numpy as np
import matplotlib.pyplot as plt
import modules.customs as cus

class RationalFunction:
    def __init__(self, cm=None, cd=None):
        """Constructor de la clase"""
        self.cm = np.array(cm if cm else [1], dtype=float)   # coeficientes numerador
        self.cd = np.array(cd if cd else [1, 0], dtype=float) # coeficientes denominador

    def evaluate(self, x):
        """Evalúa la función racional"""
        num = np.polyval(self.cm, x)
        den = np.polyval(self.cd, x)
        
        # Evitar división por cero
        result = np.where(np.abs(den) < 1e-10, np.nan, num / den)
        return result

    def asymptote_x(self):
        """Asíntotas verticales: ceros del denominador"""
        if len(self.cd) <= 1:
            return np.array([])
        
        roots = np.roots(self.cd)
        # Filtrar solo raíces reales
        real_roots = []
        for root in roots:
            if np.isreal(root):
                real_roots.append(root.real)
        return np.array(real_roots)

    def asymptote_y(self):
        """Asíntota horizontal"""
        deg_num = len(self.cm) - 1
        deg_den = len(self.cd) - 1
        
        if deg_num < deg_den:
            return 0
        elif deg_num == deg_den:
            return self.cm[0] / self.cd[0]
        else:
            return None  # asíntota oblicua (no implementada aquí)

    def x_intercepts(self):
        """Intersecciones con eje X (ceros del numerador)"""
        if len(self.cm) <= 1 and self.cm[0] == 0:
            return np.array([0])
        elif len(self.cm) <= 1:
            return np.array([])
        
        roots = np.roots(self.cm)
        # Filtrar solo raíces reales
        real_roots = []
        for root in roots:
            if np.isreal(root):
                real_roots.append(root.real)
        return np.array(real_roots)

    def y_intercept(self):
        """Intersección con eje Y"""
        num = np.polyval(self.cm, 0)
        den = np.polyval(self.cd, 0)
        if abs(den) < 1e-10:
            return None  # indefinido
        return num / den

    def to_string(self):
        """Devuelve la función en formato algebraico legible"""
        def poly_to_string(coeffs):
            if len(coeffs) == 0:
                return "0"
            
            terms = []
            degree = len(coeffs) - 1
            
            for i, coef in enumerate(coeffs):
                if coef == 0:
                    continue
                
                power = degree - i
                
                # Formato del coeficiente
                if coef == 1 and power > 0:
                    coef_str = ""
                elif coef == -1 and power > 0:
                    coef_str = "-"
                else:
                    coef_str = str(coef)
                
                # Formato de la potencia
                if power == 0:
                    term = coef_str if coef_str != "" else "1"
                elif power == 1:
                    term = f"{coef_str}x" if coef_str != "" else "x"
                else:
                    term = f"{coef_str}x^{power}" if coef_str != "" else f"x^{power}"
                
                terms.append(term)
            
            if not terms:
                return "0"
            
            # Unir términos con signos apropiados
            result = terms[0]
            for term in terms[1:]:
                if term.startswith('-'):
                    result += f" - {term[1:]}"
                else:
                    result += f" + {term}"
            
            return result
        
        num_str = poly_to_string(self.cm)
        den_str = poly_to_string(self.cd)
        return f"f(x) = ({num_str}) / ({den_str})"

    def plot(self, x_range=(-10, 10), points=1000):
        """Dibuja la función racional"""
        x = np.linspace(x_range[0], x_range[1], points)
        y = self.evaluate(x)

        plt.figure(figsize=(12, 8))
        
        # Detectar discontinuidades para graficar por segmentos
        diff = np.abs(np.diff(y))
        # Usar percentil más estricto para detectar mejor las discontinuidades
        threshold = np.nanpercentile(diff, 98)
        breaks = np.where(diff > threshold)[0]
        
        # Graficar la función por segmentos
        if len(breaks) > 0:
            start = 0
            first_segment = True
            for break_point in breaks:
                if break_point > start:
                    plt.plot(x[start:break_point+1], y[start:break_point+1], 'b-', linewidth=2,
                            label='f(x)' if first_segment else "")
                    first_segment = False
                start = break_point + 1
            # Último segmento
            if start < len(x):
                plt.plot(x[start:], y[start:], 'b-', linewidth=2,
                        label='f(x)' if first_segment else "")
        else:
            plt.plot(x, y, 'b-', linewidth=2, label='f(x)')

        # Asíntotas verticales
        asymptotes_x = self.asymptote_x()
        if len(asymptotes_x) > 0:
            vertical_labels = []
            for xv in asymptotes_x:
                if x_range[0] <= xv <= x_range[1]:
                    plt.axvline(x=xv, color='red', linestyle='--', alpha=0.8, linewidth=1.5)
                    vertical_labels.append(f"x={xv:.2f}")
            
            # Agregar etiqueta combinada para asíntotas verticales
            if vertical_labels:
                # Crear línea invisible solo para la leyenda
                plt.plot([], [], color='red', linestyle='--', alpha=0.8, linewidth=1.5,
                        label=f'Asíntotas verticales: {", ".join(vertical_labels)}')

        # Asíntota horizontal
        ay = self.asymptote_y()
        if ay is not None:
            plt.axhline(y=ay, color='green', linestyle='--', alpha=0.8, linewidth=1.5,
                       label=f'Asíntota horizontal: y={ay:.2f}')

        # Intersecciones con X
        x_ints = self.x_intercepts()
        if len(x_ints) > 0:
            x_labels = []
            for xv in x_ints:
                if x_range[0] <= xv <= x_range[1]:
                    plt.scatter(xv, 0, color='blue', s=80, zorder=5, edgecolors='black', linewidth=1)
                    x_labels.append(f"({xv:.2f}, 0)")
            
            # Agregar etiqueta combinada para intersecciones X
            if x_labels:
                plt.scatter([], [], color='blue', s=80, edgecolors='black', linewidth=1,
                           label=f'Intersecciones X: {", ".join(x_labels)}')

        # Intersección con Y
        y_int = self.y_intercept()
        if y_int is not None and x_range[0] <= 0 <= x_range[1]:
            plt.scatter(0, y_int, color='orange', s=80, zorder=5, edgecolors='black', linewidth=1,
                       label=f'Intersección Y: (0, {y_int:.2f})')

        plt.title(f'Función Racional: {self.to_string()}', fontsize=14, pad=20)
        plt.xlabel('x', fontsize=12)
        plt.ylabel('y', fontsize=12)
        plt.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
        
        # Configurar leyenda
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
        
        # Ajustar límites del gráfico de manera más inteligente
        y_valid = y[~np.isnan(y) & ~np.isinf(y)]
        if len(y_valid) > 0:
            # Usar percentiles para evitar valores extremos
            y_min, y_max = np.percentile(y_valid, [2, 98])
            y_range = y_max - y_min
            margin = max(y_range * 0.1, 1)  # Al menos 1 unidad de margen
            plt.ylim(y_min - margin, y_max + margin)
        
        #Evita la superposición de los elementos
        plt.tight_layout()
        plt.show()


def pedir_valores():
    """Función principal para interactuar con el usuario"""    
    while True:
        try:
            # Numerador
            print("\n--- NUMERADOR ---")
            n_cm = int(input("¿Cuántos coeficientes tiene el numerador? "))
            if n_cm <= 0:
                print("❌ Debe tener al menos 1 coeficiente.")
                continue
                
            cm = []
            print("Ingrese los coeficientes de mayor a menor grado:")
            for i in range(n_cm):
                while True:
                    try:
                        valor = float(input(f"Coeficiente {i+1}: "))
                        cm.append(valor)
                        break
                    except ValueError:
                        print("❌ Ingrese un número válido.")

            # Usar cu.borrarPantalla() si el módulo está disponible
            try:
                cus.borrarPantalla()
            except:
                pass

            # Denominador
            print("\n--- DENOMINADOR ---")
            n_cd = int(input("¿Cuántos coeficientes tiene el denominador? "))
            if n_cd <= 0:
                print("❌ Debe tener al menos 1 coeficiente.")
                continue
                
            cd = []
            print("Ingrese los coeficientes de mayor a menor grado:")
            for i in range(n_cd):
                while True:
                    try:
                        valor = float(input(f"Coeficiente {i+1}: "))
                        cd.append(valor)
                        break
                    except ValueError:
                        print("❌ Ingrese un número válido.")

            # Verificar que el denominador no sea cero
            if all(c == 0 for c in cd):
                print("❌ El denominador no puede ser cero en todos sus coeficientes.")
                continue

            # Usar cu.borrarPantalla() si el módulo está disponible
            try:
                cus.borrarPantalla()
            except:
                pass

            # Crear y graficar con rango por defecto
            f = RationalFunction(cm, cd)
            print(f"\n✅ Función creada: {f.to_string()}")
            
            # Mostrar información adicional
            print("\n--- INFORMACIÓN DE LA FUNCIÓN ---")
            
            # Asíntotas verticales
            asint_x = f.asymptote_x()
            if len(asint_x) > 0:
                print(f"Asíntotas verticales: x = {asint_x}")
            else:
                print("No hay asíntotas verticales")
            
            # Asíntota horizontal
            asint_y = f.asymptote_y()
            if asint_y is not None:
                print(f"Asíntota horizontal: y = {asint_y}")
            else:
                print("No hay asíntota horizontal (posible asíntota oblicua)")
            
            # Intersecciones
            x_ints = f.x_intercepts()
            if len(x_ints) > 0:
                print(f"Intersecciones con X: {x_ints}")
            else:
                print("No hay intersecciones con X")
            
            y_int = f.y_intercept()
            if y_int is not None:
                print(f"Intersección con Y: {y_int}")
            else:
                print("No hay intersección con Y (función indefinida en x=0)")
            
            print("\nGenerando gráfico...")
            f.plot()  # Usar rango por defecto (-10, 10)
            
            break  # Salir del bucle después de graficar

        except ValueError:
            print("❌ Error: Ingrese valores numéricos válidos.")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")