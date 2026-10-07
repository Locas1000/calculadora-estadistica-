import math
from core_math import norm_cdf, t_cdf, chi2_cdf, f_cdf

def calculate_p_value(cdf_value, tail):
    if tail == 'left':
        return cdf_value
    elif tail == 'right':
        return 1 - cdf_value
    else:
        return 2 * min(cdf_value, 1 - cdf_value)

def format_tail(tail):
    if tail == 'left': return "Cola izquierda (<)"
    if tail == 'right': return "Cola derecha (>)"
    return "Dos colas (≠)"

def get_conclusion(p_val, alpha):
    if p_val < alpha:
        return f"Como el valor p ({p_val:.5f}) es MENOR que el nivel de significancia alfa ({alpha}), <strong>RECHAZAMOS la hipótesis nula ($H_0$)</strong>. Hay evidencia estadística suficiente."
    else:
        return f"Como el valor p ({p_val:.5f}) es MAYOR O IGUAL que el nivel de significancia alfa ({alpha}), <strong>NO RECHAZAMOS la hipótesis nula ($H_0$)</strong>. No hay evidencia estadística suficiente."

def test_one_proportion(x, n, p0, alpha, tail):
    p_hat = x / n
    se = math.sqrt(p0 * (1 - p0) / n)
    z = (p_hat - p0) / se
    p_val = calculate_p_value(norm_cdf(z), tail)
    
    steps = [
        fr"Paso 1: Calcular la proporción muestral: \(\hat{{p}} = \frac{{x}}{{n}} = \frac{{{x}}}{{{n}}} = {p_hat:.4f}\)",
        fr"Paso 2: Calcular el error estándar (SE): \(SE = \sqrt{{\frac{{p_0(1-p_0)}}{{n}}}} = \sqrt{{\frac{{{p0}(1-{p0})}}{{{n}}}}} = {se:.4f}\)",
        fr"Paso 3: Calcular el estadístico Z: \(Z = \frac{{\hat{{p}} - p_0}}{{SE}} = \frac{{{p_hat:.4f} - {p0}}}{{{se:.4f}}} = {z:.4f}\)"
    ]
    
    return {
        "title": "Prueba de Hipótesis para Una Proporción",
        "inputs": {"Éxitos (x)": x, "Muestra (n)": n, "p₀": p0, "Alfa (α)": alpha, "Tipo de prueba": format_tail(tail)},
        "steps": steps,
        "statistic_name": "Z",
        "statistic_value": z,
        "p_value": p_val,
        "conclusion": get_conclusion(p_val, alpha)
    }

def test_two_proportions(x1, n1, x2, n2, alpha, tail):
    p_hat1 = x1 / n1
    p_hat2 = x2 / n2
    p_c = (x1 + x2) / (n1 + n2)
    se = math.sqrt(p_c * (1 - p_c) * (1/n1 + 1/n2))
    z = (p_hat1 - p_hat2) / se
    p_val = calculate_p_value(norm_cdf(z), tail)
    
    steps = [
        fr"Paso 1: Proporciones muestrales: \(\hat{{p}}_1 = {p_hat1:.4f}\), \(\hat{{p}}_2 = {p_hat2:.4f}\)",
        fr"Paso 2: Proporción conjunta (\(p_c\)): \(p_c = \frac{{x_1 + x_2}}{{n_1 + n_2}} = \frac{{{x1} + {x2}}}{{{n1} + {n2}}} = {p_c:.4f}\)",
        fr"Paso 3: Calcular el SE: \(SE = \sqrt{{p_c(1-p_c)(\frac{{1}}{{n_1}} + \frac{{1}}{{n_2}})}} = {se:.4f}\)",
        fr"Paso 4: Calcular el estadístico Z: \(Z = \frac{{\hat{{p}}_1 - \hat{{p}}_2}}{{SE}} = \frac{{{p_hat1:.4f} - {p_hat2:.4f}}}{{{se:.4f}}} = {z:.4f}\)"
    ]
    
    return {
        "title": "Prueba de Hipótesis para Dos Proporciones",
        "inputs": {"x₁": x1, "n₁": n1, "x₂": x2, "n₂": n2, "Alfa (α)": alpha, "Tipo": format_tail(tail)},
        "steps": steps,
        "statistic_name": "Z",
        "statistic_value": z,
        "p_value": p_val,
        "conclusion": get_conclusion(p_val, alpha)
    }

def test_one_mean(x_bar, s, n, mu0, alpha, tail):
    se = s / math.sqrt(n)
    t = (x_bar - mu0) / se
    df = n - 1
    p_val = calculate_p_value(t_cdf(t, df), tail)
    
    steps = [
        fr"Paso 1: Grados de libertad: \(df = n - 1 = {n} - 1 = {df}\)",
        fr"Paso 2: Calcular el SE: \(SE = \frac{{s}}{{\sqrt{{n}}}} = \frac{{{s}}}{{\sqrt{{{n}}}}} = {se:.4f}\)",
        fr"Paso 3: Calcular el estadístico T: \(T = \frac{{\bar{{x}} - \mu_0}}{{SE}} = \frac{{{x_bar} - {mu0}}}{{{se:.4f}}} = {t:.4f}\)"
    ]
    
    return {
        "title": "Prueba de Hipótesis para Una Media",
        "inputs": {"Media (x̄)": x_bar, "Desv. Est. (s)": s, "Muestra (n)": n, "μ₀": mu0, "Alfa (α)": alpha, "Tipo": format_tail(tail)},
        "steps": steps,
        "statistic_name": f"T (df={df})",
        "statistic_value": t,
        "p_value": p_val,
        "conclusion": get_conclusion(p_val, alpha)
    }

def test_two_means(x_bar1, s1, n1, x_bar2, s2, n2, alpha, tail):
    se = math.sqrt((s1**2 / n1) + (s2**2 / n2))
    t = (x_bar1 - x_bar2) / se
    
    num_df = ((s1**2 / n1) + (s2**2 / n2))**2
    den_df = ((s1**2 / n1)**2 / (n1 - 1)) + ((s2**2 / n2)**2 / (n2 - 1))
    df = num_df / den_df
    
    p_val = calculate_p_value(t_cdf(t, df), tail)
    
    steps = [
        fr"Paso 1: Error estándar (Welch): \(SE = \sqrt{{\frac{{s_1^2}}{{n_1}} + \frac{{s_2^2}}{{n_2}}}} = {se:.4f}\)",
        fr"Paso 2: Calcular el estadístico T: \(T = \frac{{\bar{{x}}_1 - \bar{{x}}_2}}{{SE}} = {t:.4f}\)",
        fr"Paso 3: Grados de libertad (Welch-Satterthwaite): \(df = {df:.4f}\)"
    ]
    
    return {
        "title": "Prueba de Hipótesis para Dos Medias (Independientes, Var. Desiguales)",
        "inputs": {"x̄₁": x_bar1, "s₁": s1, "n₁": n1, "x̄₂": x_bar2, "s₂": s2, "n₂": n2, "Alfa (α)": alpha, "Tipo": format_tail(tail)},
        "steps": steps,
        "statistic_name": f"T (df={df:.2f})",
        "statistic_value": t,
        "p_value": p_val,
        "conclusion": get_conclusion(p_val, alpha)
    }

def test_one_variance(s, n, sigma0_sq, alpha, tail):
    df = n - 1
    chi2 = (df) * (s**2) / sigma0_sq
    p_val = calculate_p_value(chi2_cdf(chi2, df), tail)
    
    steps = [
        fr"Paso 1: Grados de libertad: \(df = n - 1 = {n} - 1 = {df}\)",
        fr"Paso 2: Calcular \(\chi^2 = \frac{{(n-1)s^2}}{{\sigma_0^2}} = \frac{{{df}({s}^2)}}{{{sigma0_sq}}} = {chi2:.4f}\)"
    ]
    
    return {
        "title": "Prueba de Hipótesis para Una Varianza",
        "inputs": {"s": s, "n": n, "σ₀²": sigma0_sq, "Alfa (α)": alpha, "Tipo": format_tail(tail)},
        "steps": steps,
        "statistic_name": f"χ² (df={df})",
        "statistic_value": chi2,
        "p_value": p_val,
        "conclusion": get_conclusion(p_val, alpha)
    }

def test_two_variances(s1, n1, s2, n2, alpha, tail):
    f_stat = (s1**2) / (s2**2)
    df1 = n1 - 1
    df2 = n2 - 1
    p_val = calculate_p_value(f_cdf(f_stat, df1, df2), tail)
    
    steps = [
        fr"Paso 1: Grados de libertad: \(df_1 = {n1} - 1 = {df1}\),  \(df_2 = {n2} - 1 = {df2}\)",
        fr"Paso 2: Calcular estadístico F: \(F = \frac{{s_1^2}}{{s_2^2}} = \frac{{{s1}^2}}{{{s2}^2}} = {f_stat:.4f}\)"
    ]
    
    return {
        "title": "Prueba de Hipótesis para Dos Varianzas",
        "inputs": {"s₁": s1, "n₁": n1, "s₂": s2, "n₂": n2, "Alfa (α)": alpha, "Tipo": format_tail(tail)},
        "steps": steps,
        "statistic_name": f"F (df1={df1}, df2={df2})",
        "statistic_value": f_stat,
        "p_value": p_val,
        "conclusion": get_conclusion(p_val, alpha)
    }
