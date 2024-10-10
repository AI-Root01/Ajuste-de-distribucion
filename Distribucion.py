import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Cargar los datos
file_path = 'zona_2203900_entrenamiento.csv'
data = pd.read_csv(file_path)

# Extraer la columna Oxig_Disl_Max
oxig_disl_max = data['Oxig_Disl_Max'].values

# Graficar el histograma
plt.figure(figsize=(10, 6))
sns.histplot(oxig_disl_max, bins=30, kde=True, stat='density', color='blue', label='Datos')
plt.title('Histograma y Gráfico de Densidad de Oxig_Disl_Max')
plt.xlabel('Oxig_Disl_Max')
plt.ylabel('Densidad')
plt.grid(True)
plt.legend()
plt.show()

# Listado de distribuciones a ajustar
distributions = [
    stats.norm,        # Normal
    stats.expon,       # Exponencial
    stats.lognorm,     # Log-normal
    stats.gamma,       # Gamma
    stats.beta         # Beta
]

# Ajustar cada distribución y calcular AIC
results = []
for distribution in distributions:
    params = distribution.fit(oxig_disl_max)  # Ajustar la distribución a los datos
    # Calcular el logaritmo de la verosimilitud
    log_likelihood = np.sum(distribution.logpdf(oxig_disl_max, *params))
    # Calcular el AIC
    k = len(params)  # Número de parámetros
    aic = 2 * k - 2 * log_likelihood
    results.append((distribution.name, aic, params))

# Ordenar los resultados por AIC
results = sorted(results, key=lambda x: x[1])

# Imprimir los resultados
print("Resultados de ajuste de distribuciones:")
for name, aic, params in results:
    print(f"Distribución: {name}, AIC: {aic:.2f}, Parámetros: {params}")

# La mejor distribución
best_distribution = results[0]
print(f"\nLa mejor distribución es {best_distribution[0]} con un AIC de {best_distribution[1]:.2f}.")
