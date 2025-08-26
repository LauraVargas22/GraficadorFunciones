import pyfiglet
from rich.console import Console
from rich.panel import Panel

console = Console()

# Título principal
title1 = pyfiglet.figlet_format("FUNCIONES", font="slant",)
subtitle = pyfiglet.figlet_format("MATEMATICAS", font="digital")

def show_title():
    console.print(Panel.fit(
        f"[bold cyan]{title1}[/bold cyan]\n[bold magenta]{subtitle}[/bold magenta]",
        border_style="bright_blue",
        title="📘 PROGRAMA",
    ))

# Subtítulos
lineal = pyfiglet.figlet_format("Funcion Lineal", font="small")
quadratic = pyfiglet.figlet_format("Funcion Cuadratica", font="small")

def show_lineal():
    console.print(Panel.fit(
        f"[green]{lineal}[/green]",
        border_style="green",
        title="📈 Lineal"
    ))

def show_quadratic():
    console.print(Panel.fit(
        f"[yellow]{quadratic}[/yellow]",
        border_style="yellow",
        title="🟰 Cuadrática"
    ))
