import matplotlib.pyplot as plt
import numpy as np

# Datos dados
inicial = [
    [502, 2.04],
    [1000, 2.04],
    [2000, 2.04],
    [3000, 1.92],
    [4990, 1.56],
    [5841, 1.40],
    [5618, 1.44],
]
 

# Convertir a arrays
frecuencia = np.array([p[0] for p in inicial])
voltaje = np.array([p[1] for p in inicial])

# Graficar
plt.figure(figsize=(8,5))
plt.semilogx(frecuencia, voltaje, marker='o', linestyle='-', color='b', label='Respuesta')

# Títulos y etiquetas
plt.title("Respuesta en Frecuencia")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Voltaje [V]")

# Grid principal y secundario
plt.grid(which="major", linestyle='-', linewidth=0.8, color='black')
plt.grid(which="minor", linestyle=':', linewidth=0.5, color='gray')
plt.minorticks_on()

# Leyenda
plt.legend()

plt.show()
