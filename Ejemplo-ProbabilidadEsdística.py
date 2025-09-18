import numpy as np

# Número de lanzamientos
n = 10000  

# Simular lanzamientos de un dado (valores entre 1 y 6)
dados = np.random.randint(1, 7, size=n)

# Probabilidades experimentales (frecuencias relativas)
valores, conteos = np.unique(dados, return_counts=True)
frecuencias_relativas = conteos / n

# Resultados
print("Resultados del experimento:")
for cara, frec in zip(valores, frecuencias_relativas):
    print(f"Cara {cara}: {frec:.4f} (prob. teórica: {1/6:.4f})")

# Estadísticos
print("\nEstadísticos de los lanzamientos:")
print("Media:", np.mean(dados))
print("Varianza:", np.var(dados))
print("Desviación estándar:", np.std(dados))