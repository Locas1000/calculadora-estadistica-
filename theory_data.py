"""
Diccionario de Teoría Estadística y Métodos de Pruebas de Hipótesis.
Contiene la información conceptual, supuestos, hipótesis, fórmulas matemáticas
en LaTeX, intervalos de confianza y ejemplos prácticos para cada método implementado.
"""

THEORY_DICTIONARY = {
    "1_prop": {
        "id": "1_prop",
        "title": "Prueba de Hipótesis para Una Proporción",
        "short_name": "Una Proporción (Z)",
        "distribution": "Normal Estándar (Z)",
        "badge_class": "badge-z",
        "objective": "Evaluar si la proporción poblacional de éxitos (p) difiere significativamente de un valor teórico o estándar preestablecido (p₀).",
        "when_to_use": "Se utiliza con variables cualitativas o categóricas dicotómicas (éxito/fracaso, cumple/no cumple, sí/no) cuando se analiza una sola muestra representativa.",
        "assumptions": [
            "La muestra fue seleccionada de manera aleatoria e independiente.",
            "La variable es dicotómica (distribución binomial B(n, p)).",
            "Condición de aproximación normal (Teorema de De Moivre-Laplace): tanto n · p₀ ≥ 5 como n · (1 - p₀) ≥ 5.",
            "El tamaño de la muestra n representa menos del 10% de la población si el muestreo es sin reemplazo."
        ],
        "hypotheses": {
            "two_sided": r"H_0: p = p_0 \quad\text{vs}\quad H_1: p \neq p_0 \quad \text{(Dos colas)}",
            "left_tail": r"H_0: p = p_0 \quad\text{vs}\quad H_1: p < p_0 \quad \text{(Cola izquierda)}",
            "right_tail": r"H_0: p = p_0 \quad\text{vs}\quad H_1: p > p_0 \quad \text{(Cola derecha)}"
        },
        "formula_latex": r"Z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1 - p_0)}{n}}}",
        "formula_explanation": r"Donde \(\hat{p} = \frac{x}{n}\) es la proporción muestral observada, \(x\) es el número de éxitos, \(n\) el tamaño muestral y \(p_0\) la proporción nula especificada.",
        "standard_error_formula": r"SE = \sqrt{\frac{p_0(1 - p_0)}{n}}",
        "confidence_interval_formula": r"CI = \hat{p} \pm Z_{\alpha/2} \cdot \sqrt{\frac{\hat{p}(1 - \hat{p})}{n}}",
        "confidence_interval_note": "Para el intervalo de confianza de Wald, el error estándar se estima utilizando la proporción muestral p̂.",
        "decision_rule": "Si el valor p < α, se rechaza la hipótesis nula (H₀) en favor de la hipótesis alternativa (H₁). Hay evidencia estadística suficiente.",
        "example": "Un desarrollador de software afirma que el 80% (p₀ = 0.80) de los usuarios están satisfechos con una actualización. En una encuesta de 500 usuarios (n = 500), 390 reportaron estar satisfechos (x = 390, p̂ = 0.78). Se desea probar con α = 0.05 si la satisfacción real es diferente del 80%."
    },
    "2_prop": {
        "id": "2_prop",
        "title": "Prueba de Hipótesis para Dos Proporciones",
        "short_name": "Dos Proporciones (Z)",
        "distribution": "Normal Estándar (Z)",
        "badge_class": "badge-z",
        "objective": "Determinar si existe una diferencia estadísticamente significativa entre las proporciones de éxito de dos poblaciones o tratamientos independientes (p₁ y p₂).",
        "when_to_use": "Se emplea en pruebas A/B, ensayos clínicos, estudios comparativos de satisfacción o encuestas entre dos grupos diferentes e independientes.",
        "assumptions": [
            "Las dos muestras son independientes entre sí y seleccionadas aleatoriamente.",
            "Las poblaciones de origen siguen procesos de Bernoulli independientes.",
            "Condición de normalidad para ambas muestras: n₁·p̂₁ ≥ 5, n₁·(1-p̂₁) ≥ 5, n₂·p̂₂ ≥ 5, y n₂·(1-p̂₂) ≥ 5."
        ],
        "hypotheses": {
            "two_sided": r"H_0: p_1 - p_2 = 0 \quad\text{vs}\quad H_1: p_1 - p_2 \neq 0 \quad \text{(Dos colas)}",
            "left_tail": r"H_0: p_1 - p_2 = 0 \quad\text{vs}\quad H_1: p_1 - p_2 < 0 \quad \text{(Cola izquierda)}",
            "right_tail": r"H_0: p_1 - p_2 = 0 \quad\text{vs}\quad H_1: p_1 - p_2 > 0 \quad \text{(Cola derecha)}"
        },
        "formula_latex": r"Z = \frac{\hat{p}_1 - \hat{p}_2}{\sqrt{\bar{p}(1 - \bar{p})\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}}",
        "formula_explanation": r"Bajo H₀ (p₁ = p₂), se usa la proporción combinada o ponderada: \(\bar{p} = \frac{x_1 + x_2}{n_1 + n_2}\).",
        "standard_error_formula": r"SE_{\text{pool}} = \sqrt{\bar{p}(1 - \bar{p})\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}",
        "confidence_interval_formula": r"CI = (\hat{p}_1 - \hat{p}_2) \pm Z_{\alpha/2} \cdot \sqrt{\frac{\hat{p}_1(1 - \hat{p}_1)}{n_1} + \frac{\hat{p}_2(1 - \hat{p}_2)}{n_2}}",
        "confidence_interval_note": "Nótese que en el intervalo de confianza no se asume p₁ = p₂, por lo que se calcula el error estándar separado de cada muestra.",
        "decision_rule": "Si el valor p < α, se rechaza H₀ y se concluye que existe una diferencia estadísticamente significativa entre ambas proporciones poblacionales.",
        "example": "Se compara la tasa de clics de dos plataformas publicitarias: la Plataforma A obtuvo 180 clics de 250 vistas (n₁ = 250, x₁ = 180), y la Plataforma B obtuvo 150 clics de 240 vistas (n₂ = 240, x₂ = 150). Con α = 0.05, ¿hay diferencia entre ambas plataformas?"
    },
    "1_mean": {
        "id": "1_mean",
        "title": "Prueba de Hipótesis para Una Media",
        "short_name": "Una Media (t-Student)",
        "distribution": "t-Student (df = n - 1)",
        "badge_class": "badge-t",
        "objective": "Contrastar si la media de una población cuantitativa (μ) es igual a un valor de referencia fijado (μ₀), cuando la desviación estándar poblacional (σ) es desconocida.",
        "when_to_use": "Se utiliza al analizar una variable continua (peso, tiempo, rendimiento, gasto) de un solo grupo muestral cuando se desconoce σ y se aproxima con la desviación estándar muestral s.",
        "assumptions": [
            "Muestra aleatoria simple de la población.",
            "La población de origen sigue una distribución normal, o el tamaño de la muestra es moderadamente grande (n ≥ 30) para respaldar el Teorema del Límite Central.",
            "La varianza poblacional σ² es desconocida y se estima con s²."
        ],
        "hypotheses": {
            "two_sided": r"H_0: \mu = \mu_0 \quad\text{vs}\quad H_1: \mu \neq \mu_0 \quad \text{(Dos colas)}",
            "left_tail": r"H_0: \mu = \mu_0 \quad\text{vs}\quad H_1: \mu < \mu_0 \quad \text{(Cola izquierda)}",
            "right_tail": r"H_0: \mu = \mu_0 \quad\text{vs}\quad H_1: \mu > \mu_0 \quad \text{(Cola derecha)}"
        },
        "formula_latex": r"t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}",
        "formula_explanation": r"Donde \(\bar{x}\) es la media muestral, \(s\) la desviación estándar muestral, \(n\) el tamaño de la muestra y \(df = n - 1\) los grados de libertad.",
        "standard_error_formula": r"SE = \frac{s}{\sqrt{n}}",
        "confidence_interval_formula": r"CI = \bar{x} \pm t_{\alpha/2, \, df} \cdot \frac{s}{\sqrt{n}}",
        "confidence_interval_note": r"El valor crítico \(t_{\alpha/2, \, df}\) se obtiene de la distribución t con \(df = n - 1\) grados de libertad.",
        "decision_rule": "Si el valor p < α, se rechaza H₀. La media muestral difiere significativamente del valor teórico μ₀.",
        "example": "El rendimiento histórico de un bono corporativo promedia un 50% anual. En una muestra de 30 días (n = 30), el rendimiento promedio fue x̄ = 50 con s = 8.0. Con α = 0.01, se desea verificar si el rendimiento se mantiene en el valor esperado."
    },
    "2_mean": {
        "id": "2_mean",
        "title": "Prueba de Hipótesis para Dos Medias Independientes",
        "short_name": "Dos Medias (t de Welch)",
        "distribution": "t-Student (Grados de libertad aproximados de Welch)",
        "badge_class": "badge-t",
        "objective": "Comparar los promedios de dos poblaciones continuas independientes (μ₁ y μ₂) sin asumir que sus varianzas poblacionales sean iguales (prueba robusta ante heterocedasticidad).",
        "when_to_use": "Se emplea para comparar dos tratamientos, dos grupos experimentales o dos poblaciones cuando las dispersiones pueden diferir (método estándar recomendado en estadística moderna frente al t clásico con varianzas agrupadas).",
        "assumptions": [
            "Las muestras de ambos grupos son independientes entre sí y seleccionadas aleatoriamente.",
            "Las poblaciones son aproximadamente normales o los tamaños muestrales son suficientemente grandes.",
            r"No se asume igualdad de varianzas: \(\sigma_1^2 \neq \sigma_2^2\)."
        ],
        "hypotheses": {
            "two_sided": r"H_0: \mu_1 - \mu_2 = 0 \quad\text{vs}\quad H_1: \mu_1 - \mu_2 \neq 0 \quad \text{(Dos colas)}",
            "left_tail": r"H_0: \mu_1 - \mu_2 = 0 \quad\text{vs}\quad H_1: \mu_1 - \mu_2 < 0 \quad \text{(Cola izquierda)}",
            "right_tail": r"H_0: \mu_1 - \mu_2 = 0 \quad\text{vs}\quad H_1: \mu_1 - \mu_2 > 0 \quad \text{(Cola derecha)}"
        },
        "formula_latex": r"t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}",
        "formula_explanation": r"Los grados de libertad se calculan mediante la aproximación de Welch-Satterthwaite para reflejar la incertidumbre de varianzas desiguales.",
        "standard_error_formula": r"SE = \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}",
        "degrees_of_freedom_formula": r"df = \frac{\left(\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}\right)^2}{\frac{(s_1^2/n_1)^2}{n_1 - 1} + \frac{(s_2^2/n_2)^2}{n_2 - 1}}",
        "confidence_interval_formula": r"CI = (\bar{x}_1 - \bar{x}_2) \pm t_{\alpha/2, \, df} \cdot \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}",
        "confidence_interval_note": "Si el intervalo de confianza incluye al cero (0), indica que no hay evidencia de diferencia entre ambas medias al nivel especificado.",
        "decision_rule": "Si el valor p < α, se rechaza H₀ y se concluye que las medias de ambas poblaciones son significativamente distintas.",
        "example": "Se compara el tiempo promedio de atención entre dos sucursales bancarias: Sucursal 1 (x̄₁ = 14.5 min, s₁ = 3.2, n₁ = 25) vs Sucursal 2 (x̄₂ = 12.1 min, s₂ = 4.8, n₂ = 30). Con α = 0.05, ¿difieren los tiempos medios de atención?"
    },
    "1_var": {
        "id": "1_var",
        "title": "Prueba de Hipótesis para Una Varianza",
        "short_name": "Una Varianza (χ²)",
        "distribution": "Chi-Cuadrada (df = n - 1)",
        "badge_class": "badge-chi",
        "objective": "Determinar si la varianza poblacional (σ²) o la desviación estándar (σ) de una población normal coincide con un valor esperado o de especificación (σ₀²).",
        "when_to_use": "Fundamental en control estadístico de procesos, control de calidad y finanzas para monitorear consistencia, tolerancia, volatilidad o riesgo.",
        "assumptions": [
            "Muestra aleatoria simple de tamaño n.",
            "La población de origen debe seguir con rigurosidad una distribución normal (esta prueba es extremadamente sensible a desviaciones de la normalidad)."
        ],
        "hypotheses": {
            "two_sided": r"H_0: \sigma^2 = \sigma_0^2 \quad\text{vs}\quad H_1: \sigma^2 \neq \sigma_0^2 \quad \text{(Dos colas)}",
            "left_tail": r"H_0: \sigma^2 = \sigma_0^2 \quad\text{vs}\quad H_1: \sigma^2 < \sigma_0^2 \quad \text{(Cola izquierda)}",
            "right_tail": r"H_0: \sigma^2 = \sigma_0^2 \quad\text{vs}\quad H_1: \sigma^2 > \sigma_0^2 \quad \text{(Cola derecha)}"
        },
        "formula_latex": r"\chi^2 = \frac{(n - 1)s^2}{\sigma_0^2}",
        "formula_explanation": r"Donde \(s^2\) es la varianza muestral, \(n\) el tamaño de la muestra, \(df = n - 1\) los grados de libertad y \(\sigma_0^2\) la varianza hipotética.",
        "standard_error_formula": "No aplica error estándar lineal directo debido a la asimetría positiva de la distribución Chi-Cuadrada.",
        "confidence_interval_formula": r"CI = \left[ \frac{(n - 1)s^2}{\chi^2_{1 - \alpha/2, \, df}}, \; \frac{(n - 1)s^2}{\chi^2_{\alpha/2, \, df}} \right]",
        "confidence_interval_note": r"Nótese que el valor crítico superior \(\chi^2_{1-\alpha/2}\) divide el extremo inferior del intervalo y viceversa debido a la relación inversa del denominador.",
        "decision_rule": "Si el valor p < α, se rechaza H₀. La variabilidad observada en el proceso difiere significativamente del valor teórico σ₀².",
        "example": "Un índice bursátil requiere una varianza de rendimientos máxima de 0.0152 (σ₀² = 0.0152). En una muestra de 6 periodos (n = 6), se observa una desviación estándar muestral s = 0.1233 (s² = 0.01520). Con α = 0.05, ¿cumple con la varianza esperada?"
    },
    "2_var": {
        "id": "2_var",
        "title": "Prueba de Hipótesis para Dos Varianzas (Cociente)",
        "short_name": "Dos Varianzas (F de Fisher)",
        "distribution": "F de Fisher-Snedecor (df₁ = n₁ - 1, df₂ = n₂ - 1)",
        "badge_class": "badge-f",
        "objective": "Comparar las varianzas de dos poblaciones normales independientes para verificar si son iguales (prueba de homogeneidad de varianzas u homocedasticidad).",
        "when_to_use": "Se emplea para verificar si dos métodos de medición, dos máquinas o dos portafolios de inversión tienen la misma variabilidad o precisión.",
        "assumptions": [
            "Ambas muestras provienen de poblaciones independientes y fueron seleccionadas aleatoriamente.",
            "Ambas poblaciones siguen rigurosamente una distribución normal (la prueba F no es robusta ante desviaciones de la normalidad)."
        ],
        "hypotheses": {
            "two_sided": r"H_0: \frac{\sigma_1^2}{\sigma_2^2} = 1 \quad\text{vs}\quad H_1: \frac{\sigma_1^2}{\sigma_2^2} \neq 1 \quad \text{(Dos colas)}",
            "left_tail": r"H_0: \frac{\sigma_1^2}{\sigma_2^2} = 1 \quad\text{vs}\quad H_1: \frac{\sigma_1^2}{\sigma_2^2} < 1 \quad \text{(Cola izquierda)}",
            "right_tail": r"H_0: \frac{\sigma_1^2}{\sigma_2^2} = 1 \quad\text{vs}\quad H_1: \frac{\sigma_1^2}{\sigma_2^2} > 1 \quad \text{(Cola derecha)}"
        },
        "formula_latex": r"F = \frac{s_1^2}{s_2^2}",
        "formula_explanation": r"El estadístico F es la razón de las dos varianzas muestrales, con \(df_1 = n_1 - 1\) grados de libertad en el numerador y \(df_2 = n_2 - 1\) en el denominador.",
        "standard_error_formula": "Se fundamenta en el cociente de dos variables aleatorias independientes distribuidas como Chi-cuadrada divididas por sus grados de libertad.",
        "confidence_interval_formula": r"CI = \left[ \frac{s_1^2}{s_2^2} \cdot \frac{1}{F_{1 - \alpha/2, \, df_1, \, df_2}}, \; \frac{s_1^2}{s_2^2} \cdot \frac{1}{F_{\alpha/2, \, df_1, \, df_2}} \right]",
        "confidence_interval_note": "Si el intervalo de confianza para el cociente σ₁²/σ₂² contiene al 1.0, no existe evidencia estadística de diferencia en las varianzas al nivel (1 - α).",
        "decision_rule": "Si el valor p < α, se rechaza H₀ y se concluye que las varianzas poblacionales son significativamente desiguales.",
        "example": "Se compara la volatilidad de dos bonos: Bono P (s₁ = 0.0707, n₁ = 10) vs Bono Q (s₂ = 0.0447, n₂ = 12). Con α = 0.10, ¿tienen ambos bonos la misma varianza poblacional?"
    }
}

GENERAL_CONCEPTS = {
    "hypotheses": {
        "title": "Hipótesis Nula (H₀) y Alternativa (H₁)",
        "description": "En cualquier prueba estadística, H₀ representa la afirmación de no efecto, igualdad o estado actual (status quo). H₁ es la hipótesis del investigador o la afirmación de cambio, diferencia o efecto que se desea demostrar con evidencia empírica."
    },
    "alpha": {
        "title": "Nivel de Significancia (α) y Confianza (1 - α)",
        "description": "El nivel de significancia α es la probabilidad máxima aceptada de cometer un Error Tipo I (rechazar H₀ cuando es verdadera). Típicamente se utiliza α = 0.05 (5%), α = 0.01 (1%) o α = 0.10 (10%). El nivel de confianza asociado es 1 - α (ej. 95%, 99% o 90%)."
    },
    "p_value": {
        "title": "Valor p (p-value) y Regla de Decisión",
        "description": "El valor p es la probabilidad de obtener un estadístico de prueba tan o más extremo que el observado, asumiendo que H₀ es cierta. Regla universal: Si p-value < α, se RECHAZA H₀ (evidencia estadísticamente significativa). Si p-value ≥ α, NO se rechaza H₀."
    },
    "tails": {
        "title": "Colas de la Prueba (Bilateral vs Unilateral)",
        "description": "• Bilateral / Dos colas (≠): Se detectan desviaciones en ambas direcciones; el nivel α se divide en α/2 en cada cola.\n• Cola Izquierda (<): Se detecta si el parámetro es menor al teórico; toda el área α se ubica a la izquierda.\n• Cola Derecha (>): Se detecta si el parámetro es mayor al teórico; toda el área α se ubica a la derecha."
    },
    "errors": {
        "title": "Error Tipo I (α) y Error Tipo II (β)",
        "description": "• Error Tipo I (Falso Positivo): Rechazar H₀ cuando en realidad es verdadera. Su probabilidad está acotada por α.\n• Error Tipo II (Falso Negativo): No rechazar H₀ cuando en realidad es falsa. Su probabilidad es β. La potencia de la prueba es 1 - β (capacidad de detectar un efecto real)."
    },
    "ci": {
        "title": "Intervalos de Confianza (CI)",
        "description": "Un intervalo de confianza del (1 - α)% proporciona un rango estimado de valores plausibles para el parámetro poblacional. En pruebas bilaterales, si el valor hipotético nulo (μ₀, p₀, etc.) se encuentra fuera del intervalo de confianza, la prueba correspondiente rechazará H₀ con ese mismo nivel α."
    }
}
