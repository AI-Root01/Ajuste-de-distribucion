# Ajuste-de-distribucion
Análisis de Ajuste de Distribuciones

### Ejemplo
# Análisis de Ajuste de Distribuciones

## Resultados de ajuste de distribuciones:

| Distribución | AIC      | Parámetros                                                        |
|--------------|----------|-------------------------------------------------------------------|
| Beta         | -2068.51 | (2214614.03, 5.48, -20992.35, 20993.25)                         |
| Normal       | -2010.89 | (0.8484, 0.0224)                                                |
| Log-normal   | -2008.88 | (9.968e-06, -2242.05, 2242.90)                                  |
| Exponencial   | -1285.51 | (0.7683, 0.0801)                                               |
| Gamma        | -721.26  | (0.3436, 0.7683, 1.2001)                                       |

## Mejor Distribución

La **mejor distribución** para los datos de `Oxig_Disl_Max` es la **distribución Beta** con un AIC de **-2068.51**.

### Razones:

1. **AIC más Bajo**:
   - La distribución beta tiene el **AIC más bajo** entre las distribuciones probadas, lo que indica que se ajusta mejor a los datos. El AIC mide la calidad del modelo penalizando por la complejidad; por lo tanto, un AIC más bajo sugiere un mejor balance entre ajuste y complejidad.

2. **Parámetros Significativos**:
   - La distribución beta tiene parámetros que sugieren una forma que puede adaptarse bien a los datos. En particular, los valores de los parámetros indican una posible concentración de los datos en la parte alta del rango.

3. **Comparación con Otras Distribuciones**:
   - Aunque las distribuciones normal y log-normal también presentan buenos ajustes (AIC de -2010.89 y -2008.88), no superan la calidad del ajuste de la distribución beta.
   - Las distribuciones exponencial y gamma tienen AICs significativamente más altos, lo que indica que no son adecuadas para modelar estos datos.

### Conclusión:

Utilizar la distribución beta permitirá realizar análisis más precisos y confiables sobre los datos de `Oxig_Disl_Max`, así como facilitar simulaciones y predicciones futuras.
