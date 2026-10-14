import math
from core_math import (
    norm_cdf, t_cdf, chi2_cdf, f_cdf,
    norm_ppf, t_ppf, chi2_ppf, f_ppf
)

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
    
    # Intervalo de Confianza
    z_crit = norm_ppf(1 - alpha/2)
    me = z_crit * math.sqrt(p_hat * (1 - p_hat) / n)
    
    steps = [
        fr"Paso 1: Proporción muestral: \(\hat{{p}} = \frac{{{x}}}{{{n}}} = {p_hat:.4f}\)",
        fr"Paso 2: Calcular estadístico Z: \(Z = \frac{{\hat{{p}} - p_0}}{{\sqrt{{p_0(1-p_0)/n}}}} = {z:.4f}\)",
        fr"Paso 3: Intervalo de Confianza ({(1-alpha)*100:.0f}%): \(Z_{{crit}} = {z_crit:.4f}\)",
        fr"\(CI = \hat{{p}} \pm Z_{{crit}} \sqrt{{\frac{{\hat{{p}}(1-\hat{{p}})}}{{n}}}} = [{p_hat - me:.4f}, {p_hat + me:.4f}]\)"
    ]
    
    return {
        "title": "Una Proporción",
        "inputs": {"x": x, "n": n, "p₀": p0, "Alfa": alpha},
        "steps": steps,
        "statistic_name": "Z",
        "statistic_value": z,
        "p_value": p_val,
        "ci_name": f"Intervalo de Confianza ({(1-alpha)*100:.0f}%)",
        "ci_value": f"[{p_hat - me:.4f}, {p_hat + me:.4f}]",
        "conclusion": get_conclusion(p_val, alpha)
    }

def test_two_proportions(x1, n1, x2, n2, alpha, tail):
    p_hat1 = x1 / n1
    p_hat2 = x2 / n2
    p_c = (x1 + x2) / (n1 + n2)
    se = math.sqrt(p_c * (1 - p_c) * (1/n1 + 1/n2))
    z = (p_hat1 - p_hat2) / se
    p_val = calculate_p_value(norm_cdf(z), tail)
    
    # Intervalo de Confianza para diferencia de proporciones
    z_crit = norm_ppf(1 - alpha/2)
    me = z_crit * math.sqrt((p_hat1*(1-p_hat1)/n1) + (p_hat2*(1-p_hat2)/n2))
    diff = p_hat1 - p_hat2
    
    steps = [
        fr"Paso 1: Proporciones: \(\hat{{p}}_1 = {p_hat1:.4f}, \hat{{p}}_2 = {p_hat2:.4f}\)",
        fr"Paso 2: Estadístico Z: \(Z = \frac{{\hat{{p}}_1 - \hat{{p}}_2}}{{SE}} = {z:.4f}\)",
        fr"Paso 3: Intervalo de Confianza ({(1-alpha)*100:.0f}%): \(Z_{{crit}} = {z_crit:.4f}\)",
        fr"\(CI = (\hat{{p}}_1 - \hat{{p}}_2) \pm Z_{{crit}} \times SE_{{diff}} = [{diff - me:.4f}, {diff + me:.4f}]\)"
    ]
    
    return {
        "title": "Dos Proporciones",
        "inputs": {"x₁": x1, "n₁": n1, "x₂": x2, "n₂": n2, "Alfa": alpha},
        "steps": steps,
        "statistic_name": "Z",
        "statistic_value": z,
        "p_value": p_val,
        "ci_name": f"Intervalo de Confianza ({(1-alpha)*100:.0f}%)",
        "ci_value": f"[{diff - me:.4f}, {diff + me:.4f}]",
        "conclusion": get_conclusion(p_val, alpha)
    }

def test_one_mean(x_bar, s, n, mu0, alpha, tail):
    se = s / math.sqrt(n)
    t = (x_bar - mu0) / se
    df = n - 1
    p_val = calculate_p_value(t_cdf(t, df), tail)
    
    # Intervalo de Confianza
    t_crit = t_ppf(1 - alpha/2, df)
    me = t_crit * se
    
    steps = [
        fr"Paso 1: Grados de libertad: \(df = {df}\)",
        fr"Paso 2: Estadístico T: \(T = \frac{{{x_bar} - {mu0}}}{{{se:.4f}}} = {t:.4f}\)",
        fr"Paso 3: Intervalo de Confianza ({(1-alpha)*100:.0f}%): \(t_{{crit}} = {t_crit:.4f}\)",
        fr"\(CI = \bar{{x}} \pm t_{{crit}} \frac{{s}}{{\sqrt{{n}}}} = [{x_bar - me:.4f}, {x_bar + me:.4f}]\)"
    ]
    
    return {
        "title": "Una Media",
        "inputs": {"Media (x̄)": x_bar, "Desv. Est. (s)": s, "Muestra (n)": n, "μ₀": mu0, "Alfa": alpha},
        "steps": steps,
        "statistic_name": f"T (df={df})",
        "statistic_value": t,
        "p_value": p_val,
        "ci_name": f"Intervalo de Confianza ({(1-alpha)*100:.0f}%)",
        "ci_value": f"[{x_bar - me:.4f}, {x_bar + me:.4f}]",
        "conclusion": get_conclusion(p_val, alpha)
    }

def test_two_means(x_bar1, s1, n1, x_bar2, s2, n2, alpha, tail):
    se = math.sqrt((s1**2 / n1) + (s2**2 / n2))
    t = (x_bar1 - x_bar2) / se
    
    num_df = ((s1**2 / n1) + (s2**2 / n2))**2
    den_df = ((s1**2 / n1)**2 / (n1 - 1)) + ((s2**2 / n2)**2 / (n2 - 1))
    df = num_df / den_df
    
    p_val = calculate_p_value(t_cdf(t, df), tail)
    
    # Intervalo de Confianza
    t_crit = t_ppf(1 - alpha/2, df)
    me = t_crit * se
    diff = x_bar1 - x_bar2
    
    steps = [
        fr"Paso 1: Error estándar (Welch): \(SE = {se:.4f}\)",
        fr"Paso 2: Estadístico T: \(T = \frac{{\bar{{x}}_1 - \bar{{x}}_2}}{{SE}} = {t:.4f}\)",
        fr"Paso 3: Grados de libertad (Welch): \(df = {df:.4f}\)",
        fr"Paso 4: Intervalo de Confianza: \(t_{{crit}} = {t_crit:.4f}\)",
        fr"\(CI = (\bar{{x}}_1 - \bar{{x}}_2) \pm t_{{crit}} \times SE = [{diff - me:.4f}, {diff + me:.4f}]\)"
    ]
    
    return {
        "title": "Dos Medias (Independientes)",
        "inputs": {"x̄₁": x_bar1, "s₁": s1, "n₁": n1, "x̄₂": x_bar2, "s₂": s2, "n₂": n2, "Alfa": alpha},
        "steps": steps,
        "statistic_name": f"T (df={df:.2f})",
        "statistic_value": t,
        "p_value": p_val,
        "ci_name": f"Intervalo de Confianza ({(1-alpha)*100:.0f}%)",
        "ci_value": f"[{diff - me:.4f}, {diff + me:.4f}]",
        "conclusion": get_conclusion(p_val, alpha)
    }

def test_one_variance(s, n, sigma0_sq, alpha, tail):
    df = n - 1
    chi2 = (df) * (s**2) / sigma0_sq
    p_val = calculate_p_value(chi2_cdf(chi2, df), tail)
    
    # Intervalo de Confianza
    chi2_lower_crit = chi2_ppf(alpha/2, df)
    chi2_upper_crit = chi2_ppf(1 - alpha/2, df)
    num = df * (s**2)
    
    ci_lower = num / chi2_upper_crit
    ci_upper = num / chi2_lower_crit
    
    steps = [
        fr"Paso 1: Grados de libertad: \(df = {df}\)",
        fr"Paso 2: Estadístico \(\chi^2 = \frac{{(n-1)s^2}}{{\sigma_0^2}} = {chi2:.4f}\)",
        fr"Paso 3: Intervalo de Confianza ({(1-alpha)*100:.0f}%): \(\chi^2_{{inf}} = {chi2_lower_crit:.4f}, \chi^2_{{sup}} = {chi2_upper_crit:.4f}\)",
        fr"\(CI = \left[ \frac{{(n-1)s^2}}{{\chi^2_{{sup}}}}, \frac{{(n-1)s^2}}{{\chi^2_{{inf}}}} \right] = [{ci_lower:.4f}, {ci_upper:.4f}]\)"
    ]
    
    return {
        "title": "Una Varianza",
        "inputs": {"s": s, "n": n, "σ₀²": sigma0_sq, "Alfa": alpha},
        "steps": steps,
        "statistic_name": f"χ² (df={df})",
        "statistic_value": chi2,
        "p_value": p_val,
        "ci_name": f"Intervalo de Confianza ({(1-alpha)*100:.0f}%)",
        "ci_value": f"[{ci_lower:.4f}, {ci_upper:.4f}]",
        "conclusion": get_conclusion(p_val, alpha)
    }

def test_two_variances(s1, n1, s2, n2, alpha, tail):
    f_stat = (s1**2) / (s2**2)
    df1 = n1 - 1
    df2 = n2 - 1
    p_val = calculate_p_value(f_cdf(f_stat, df1, df2), tail)
    
    # Intervalo de Confianza (Cociente de varianzas)
    f_lower_crit = f_ppf(alpha/2, df1, df2)
    f_upper_crit = f_ppf(1 - alpha/2, df1, df2)
    ratio = (s1**2) / (s2**2)
    
    ci_lower = ratio / f_upper_crit
    ci_upper = ratio / f_lower_crit
    
    steps = [
        fr"Paso 1: Grados de libertad: \(df_1 = {df1}, df_2 = {df2}\)",
        fr"Paso 2: Estadístico F: \(F = \frac{{s_1^2}}{{s_2^2}} = {f_stat:.4f}\)",
        fr"Paso 3: Intervalo de Confianza ({(1-alpha)*100:.0f}%): \(F_{{inf}} = {f_lower_crit:.4f}, F_{{sup}} = {f_upper_crit:.4f}\)",
        fr"\(CI = \left[ \frac{{s_1^2}}{{s_2^2}}\frac{{1}}{{F_{{sup}}}}, \frac{{s_1^2}}{{s_2^2}}\frac{{1}}{{F_{{inf}}}} \right] = [{ci_lower:.4f}, {ci_upper:.4f}]\)"
    ]
    
    return {
        "title": "Dos Varianzas (Cociente)",
        "inputs": {"s₁": s1, "n₁": n1, "s₂": s2, "n₂": n2, "Alfa": alpha},
        "steps": steps,
        "statistic_name": f"F (df1={df1}, df2={df2})",
        "statistic_value": f_stat,
        "p_value": p_val,
        "ci_name": f"Intervalo de Confianza para Cociente ({(1-alpha)*100:.0f}%)",
        "ci_value": f"[{ci_lower:.4f}, {ci_upper:.4f}]",
        "conclusion": get_conclusion(p_val, alpha)
    }
