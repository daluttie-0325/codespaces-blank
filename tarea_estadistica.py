import pandas as pd
import matplotlib.pyplot as plt
from statistics import mean, median, multimode

# Datos reales extraídos de la tabla (Códigos 1 a 60)
notas = [
    30,50,20,40,30,20,30,40,40,50,
    50,20,40,30,20,40,30,30,20,20,
    40,30,40,50,20,30,30,40,30,20,
    30,40,20,30,50,20,30,40,20,20,
    40,50,30,20,30,30,50,20,10,20,
    30,30,40,40,30,50,30,20,20,10
]

# Crear DataFrame
df = pd.DataFrame({"nota": notas})

# Frecuencia absoluta
abs_freq = df["nota"].value_counts().sort_index()

# Frecuencia relativa
rel_freq = abs_freq / abs_freq.sum()

# Porcentaje normalizado
pct_norm = rel_freq * 100

# Frecuencia acumulada
abs_acum = abs_freq.cumsum()
rel_acum = rel_freq.cumsum()

# Tabla completa
tabla_frecuencias = pd.DataFrame({
    "Frecuencia Absoluta": abs_freq,
    "Frecuencia Relativa": rel_freq,
    "Porcentaje Normalizado": pct_norm,
    "Frecuencia Acumulada Abs": abs_acum,
    "Frecuencia Acumulada Rel": rel_acum
})

print("\nTABLA DE FRECUENCIAS:\n")
print(tabla_frecuencias)

# Cálculos solicitados
A = max(notas) - min(notas)   # Amplitud total
K = max(notas) / 2            # Número de clases
H = A / K                     # Extensión de intervalo

print("\nAmplitud total (A):", A)
print("Número de clases (K):", K)
print("Extensión del intervalo (H):", H)

# Medidas estadísticas
media = mean(notas)
mediana = median(notas)
moda = multimode(notas)  # Puede haber más de una moda

print("\nMedia:", media)
print("Mediana:", mediana)
print("Moda:", moda)

# Diagrama de barras (personas por calificación)
plt.figure(figsize=(8,5))
plt.bar(abs_freq.index, abs_freq.values)
plt.title("Cantidad de personas por calificación")
plt.xlabel("Calificación")
plt.ylabel("Número de personas")
plt.xticks(abs_freq.index)
plt.show()