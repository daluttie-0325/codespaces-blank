import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
#   DATOS DEL EJERCICIO
# ------------------------------

data = np.array([
    120,95,110,130,105,100,115,125,90,140,135,98,102,108,112,118,
    122,99,130,85,107,111,119,121,96,104,128,132,97,101
])

N = 500   # tamaño poblacional
n = len(data)
mean = np.mean(data)

# ------------------------------
#   CÁLCULOS ESTADÍSTICOS
# ------------------------------

# Suma
suma = np.sum(data)

# Varianza muestral
S2 = np.var(data, ddof=1)
S = np.sqrt(S2)

# Error estándar con corrección por población finita
FPC = np.sqrt(1 - n/N)
SE = (S / np.sqrt(n)) * FPC

# Intervalo de confianza al 95%
t = 2.045
IC_lower = mean - t*SE
IC_upper = mean + t*SE

# Estimación del total
T_est = N * mean
SE_total = N * SE

IC_total_lower = T_est - t*SE_total
IC_total_upper = T_est + t*SE_total

# ------------------------------
#   IMPRESIÓN DE RESULTADOS
# ------------------------------

print("===== RESULTADOS =====")
print(f"Tamaño de la muestra: n = {n}")
print(f"Media muestral: {mean:.4f}")
print(f"Varianza muestral: {S2:.4f}")
print(f"Desviación estándar: {S:.4f}")
print(f"Error estándar (FPC): {SE:.4f}")
print(f"IC 95% de la media: ({IC_lower:.4f}, {IC_upper:.4f})")
print("\n--- Estimación del total ---")
print(f"Total estimado: {T_est:.4f}")
print(f"IC 95% del total: ({IC_total_lower:.4f}, {IC_total_upper:.4f})")

# =====================================================================
#                           G R Á F I C O S
# =====================================================================

# ------------------------------
#   1. Histograma
# ------------------------------
plt.figure()
plt.hist(data)
plt.xlabel("Consumo (litros/mes)")
plt.ylabel("Frecuencia")
plt.title("Histograma del consumo de agua")
plt.show()

# ------------------------------
#   2. Boxplot
# ------------------------------
plt.figure()
plt.boxplot(data)
plt.ylabel("Consumo (litros/mes)")
plt.title("Diagrama de caja del consumo de agua")
plt.show()

# ------------------------------
#   3. Gráfico de barras
# ------------------------------
plt.figure()
plt.bar(range(1, n+1), data)
plt.xlabel("Hogar (ID ficticio)")
plt.ylabel("Consumo (litros/mes)")
plt.title("Gráfico de barras del consumo por hogar")
plt.show()

# ------------------------------
#   4. Densidad KDE manual
# ------------------------------

def kde(x, data, bandwidth=5):
    return np.mean(np.exp(-0.5*((x-data)/bandwidth)**2)) / (bandwidth*np.sqrt(2*np.pi))

xs = np.linspace(min(data)-10, max(data)+10, 300)
ys = np.array([kde(x, data) for x in xs])

plt.figure()
plt.plot(xs, ys)
plt.xlabel("Consumo (litros/mes)")
plt.ylabel("Densidad")
plt.title("Curva de densidad (KDE estimada)")
plt.show()

# ------------------------------
#   5. Intervalo de confianza
# ------------------------------
plt.figure()
plt.errorbar(1, mean, yerr=t*SE)
plt.xlim(0,2)
plt.xticks([])
plt.ylabel("Consumo (litros/mes)")
plt.title("Intervalo de confianza al 95% de la media")
plt.show()
