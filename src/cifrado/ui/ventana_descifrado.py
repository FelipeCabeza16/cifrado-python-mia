"""Ventana de descifrado."""
import tkinter as tk
from tkinter import messagebox, ttk

from cifrado.logica import descifrar


class VentanaDescifrado(tk.Toplevel):
    def __init__(self, padre):
        super().__init__(padre)
        self.title("Descifrado de datos")
        self.resizable(False, False)
        self.entrada = tk.StringVar()
        self.resultado = tk.StringVar(value="—")
        self._crear_widgets()

    def _crear_widgets(self):
        marco = ttk.Frame(self, padding=20)
        marco.pack()
        ttk.Label(marco, text="Número cifrado (6 dígitos):").grid(row=0, column=0, sticky="w")
        caja = ttk.Entry(marco, textvariable=self.entrada, width=12, font=("Arial", 14))
        caja.grid(row=1, column=0, pady=5)
        caja.focus()
        caja.bind("<Return>", lambda _: self.ejecutar_descifrado())
        ttk.Button(marco, text="Descifrar", command=self.ejecutar_descifrado).grid(row=2, column=0, pady=5)
        ttk.Label(marco, text="Número original:").grid(row=3, column=0, sticky="w", pady=(10, 0))
        ttk.Label(marco, textvariable=self.resultado, font=("Arial", 18, "bold")).grid(row=4, column=0)
        ttk.Button(marco, text="Cerrar", command=self.destroy).grid(row=5, column=0, pady=(15, 0))

    def ejecutar_descifrado(self):
        """Descifra el número ingresado y lo muestra; avisa si la entrada es inválida."""
        try:
            self.resultado.set(descifrar(self.entrada.get()))
        except ValueError as error:
            messagebox.showerror("Dato inválido", str(error), parent=self)
