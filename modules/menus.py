from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def show_menu():
    table = Table(
        title="📘 [bold cyan]FUNCIONES[/bold cyan]",
        header_style="bold magenta",
        border_style="bright_blue",
        show_lines=True
    )
    table.add_column("Opción", justify="center", style="bold yellow", no_wrap=True)
    table.add_column("Descripción", style="white")

    table.add_row("1", "📈  Función Lineal  ")
    table.add_row("2", "🟰  Función Cuadrática         ")
    table.add_row("3", "🚪  Salir  ")

    console.print(Panel.fit(table, border_style="cyan", title="Menú Principal"))
