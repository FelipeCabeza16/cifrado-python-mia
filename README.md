# Cifrado de datos – Transmisión segura

Aplicación de escritorio en Python (Tkinter) que cifra y descifra números enteros de 6 dígitos.
Actividad de la asignatura **Aplicaciones** – Maestría en Inteligencia Artificial, Universidad de La Salle.

## Caso práctico

Una organización transmite datos desde dispositivos móviles que podrían estar intervenidos, por lo que los datos se cifran antes de enviarse.

**Cifrado** de un número de 6 dígitos:

1. A cada dígito se le suma 7 y se toma el residuo de dividir entre 10.
2. Se intercambian posiciones: 1º↔3º, 2º↔4º y 5º↔6º.

**Descifrado**: se aplica el proceso inverso (primero los mismos intercambios, que son su propia inversa; luego se resta 7 módulo 10).

| Original | Cifrado |
|----------|---------|
| 123456   | 018932  |
| 791658   | 834652  |

Ejemplo paso a paso (123456): sumar 7 → `8 9 0 1 2 3`; intercambios → `0 1 8 9 3 2` → **018932**.

## Ejecución

Requisitos: Python 3.8+ con Tkinter (incluido en Windows/macOS; en Ubuntu/Debian: `sudo apt install python3-tk`). No hay dependencias externas.

```bash
git clone <url-del-repositorio>
cd cifrado-datos
python3 src/main.py
```

Pruebas automáticas:

```bash
python3 -m unittest discover -s tests -v
```

## Estructura

```
cifrado-datos/
├── src/
│   ├── main.py                     # punto de entrada
│   └── cifrado/
│       ├── logica.py               # cifrar, descifrar, validar (sin GUI)
│       └── ui/
│           ├── ventana_principal.py   # datos del autor + navegación
│           ├── ventana_cifrado.py
│           └── ventana_descifrado.py
├── tests/test_logica.py            # pruebas unitarias
├── docs/capturas/                  # capturas para el informe
└── README.md
```

## Cómo se hizo

1. **Análisis**: se tradujo el enunciado a reglas precisas (suma módulo 10 + tres intercambios) y se calcularon a mano los resultados esperados de 123456 y 791658.
2. **Lógica primero**: se implementó `logica.py` y sus pruebas antes de la interfaz. Se trabaja con `str` y no con `int` para conservar los ceros a la izquierda (p. ej. `018932`).
3. **Interfaz**: Tkinter, por venir con Python. La ventana principal es un `Tk`; cifrado y descifrado son `Toplevel` hijas, por lo que la navegación es simple y se pueden cerrar sin terminar la app.
4. **Validación**: toda entrada pasa por `validar_numero` (exactamente 6 dígitos ASCII); si falla se muestra un `messagebox` de error.
5. **Verificación**: pruebas unitarias con los dos casos del enunciado, ida y vuelta sobre muestras del rango completo y entradas inválidas.

## Buenas prácticas aplicadas

- **Separación de responsabilidades**: la lógica no importa Tkinter, así que se prueba sin GUI y se podría reutilizar con otra interfaz.
- **Funciones pequeñas y con una sola tarea** (`validar_numero`, `intercambiar_posiciones`, `cifrar`, `descifrar`).
- **Sin números mágicos**: `LONGITUD`, `DESPLAZAMIENTO` e `INTERCAMBIOS` son constantes con nombre.
- **Nombres descriptivos** en español y docstrings en cada módulo y función pública.
- **Reutilización**: `intercambiar_posiciones` sirve para cifrar y descifrar porque cada intercambio es su propia inversa.
- **Pruebas automáticas** con `unittest` (biblioteca estándar, sin dependencias).
- **Manejo de errores** en el borde de la interfaz, con mensajes claros al usuario.
- **Sin dependencias externas**, para que cualquiera ejecute el proyecto con solo Python.

## Control de versiones

- Repositorio Git con rama principal `main`.
- Commits pequeños y atómicos, uno por cambio lógico, siguiendo [Conventional Commits](https://www.conventionalcommits.org/es/) (`feat:`, `test:`, `docs:`, `chore:`).
- La lógica y sus pruebas se versionaron antes que la interfaz.
- `.gitignore` excluye `__pycache__`, entornos virtuales, archivos de editor y el `.zip` de entrega.
- Historial: `git log --oneline`.

## Entrega

Comprimir el proyecto junto con el informe de pruebas:

```bash
git archive --format=zip --prefix=cifrado-datos/ -o entrega.zip HEAD
```

## Autor

Andrés Felipe Cabezas – Maestría en Inteligencia Artificial, Universidad de La Salle.
