# 📊 Graficador de Funciones Matemáticas en Python  
Proyecto de consola desarrollado en Python, permite graficar diferentes tipos de funciones matemáticas tales como: función lineal, cuadrática y racional. Esto con el objetivo de apoyar el aprendizaje y la visualización de conceptos matemáticos.  

## 🚀 Características  
- 📈 Graficación de funciones matemáticas (lineales, cuadráticas, racionales).  
- 🎨 Visualización interactiva utilizando **Matplotlib**.  
- ⚡ Código modular siguiendo la Programación Orientada a Objetos, fácil de extender para nuevas funciones.  

## 🛠️ Tecnologías utilizadas  
- [Python 3.x](https://www.python.org/)  
- [Matplotlib](https://matplotlib.org/) – para la visualización de gráficos  
- [NumPy](https://numpy.org/) – para el manejo de cálculos numéricos  
- [Rich-pyfiglet](https://pypi.org/project/rich-pyfiglet/) - para la interfaz de consola

### ▶️ Instalación y uso
1. Clonar el repositorio
```bash
git clone https://github.com/LauraVargas22/GraficadorFunciones.git
cd GraficaFunciones
```

2. Instalación de librerías
- Numpy
```bash
pip install numpy
```
- Matplotlib
```bash
pip install matplotlib
```
- Rich y Pyfiglet
```bash
pip install rich pyfiglet
```

3. Uso
```
python main.py
```

## 📂 Estructura del proyecto  
```
graficador-funciones/
├── modules/                 
│   ├── funcionLineal.py       # Lógica para graficar función lineal
│   ├── funcionCuadratica.py   # Lógica para graficar función cuadrática
│   ├── funcionRacional.py     # Lógica para graficar función racional
│   ├── menus.py               # Menús de navegación en consola
│   ├── salir.py               # Opción para salir del programa
│   ├── titles.py              # Títulos y subtítulos personalizados
│   ├── customs.py             # Estilos y configuraciones
│   └── mensajes.py            # Mensajes de ayuda y notificaciones
├── main.py                    # Archivo principal para ejecutar el programa
└── README.md                  # Documentación del proyecto
```
