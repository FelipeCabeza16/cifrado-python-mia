"""Ventana principal: datos del autor y navegación."""
import tkinter as tk
from tkinter import ttk

from cifrado.ui.ventana_cifrado import VentanaCifrado
from cifrado.ui.ventana_descifrado import VentanaDescifrado

AUTOR = {
    "Estudiante": "Andrés Felipe Cabezas",
    "Programa": "Maestría en Inteligencia Artificial",
    "Universidad": "Universidad de La Salle",
    "Asignatura": "Aplicaciones",
}


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Transmisión segura de datos")
        self.resizable(False, False)
        self._crear_widgets()

    def _crear_widgets(self):
        marco = ttk.Frame(self, padding=25)
        marco.pack()
        ttk.Label(marco, text="Cifrado de datos", font=("Arial", 18, "bold")).pack(pady=(0, 10))
        for etiqueta, valor in AUTOR.items():
            ttk.Label(marco, text=f"{etiqueta}: {valor}").pack(anchor="w")
        ttk.Button(marco, text="Cifrar número", command=lambda: VentanaCifrado(self)).pack(fill="x", pady=(20, 5))
        ttk.Button(marco, text="Descifrar número", command=lambda: VentanaDescifrado(self)).pack(fill="x")
        ttk.Button(marco, text="Salir", command=self.destroy).pack(fill="x", pady=(15, 0))
