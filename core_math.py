import math

def integrate(f, a, b, n=2000):
    """Integración numérica usando la Regla de Simpson 1/3"""
    if a == b:
        return 0.0
    if n % 2 != 0:
        n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n, 2):
        s += 4 * f(a + i * h)
    for i in range(2, n, 2):
        s += 2 * f(a + i * h)
    return (s * h) / 3

def norm_cdf(z):
    """CDF de la Distribución Normal Estándar usando la Función de Error"""
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))
def t_pdf(t, df):
    """PDF de la Distribución T-Student (cálculo logarítmico contra overflow)"""
    log_num = math.lgamma((df + 1) / 2)
    log_den = 0.5 * math.log(df * math.pi) + math.lgamma(df / 2)
    log_term = - ((df + 1) / 2) * math.log(1 + (t**2)/df)
    return math.exp(log_num - log_den + log_term)

def t_cdf(t, df):
    """CDF de la Distribución T-Student"""
    if t == 0:
        return 0.5
    area = integrate(lambda x: t_pdf(x, df), 0, abs(t), n=max(2000, int(abs(t)*50)))
    if t > 0:
        return 0.5 + area
    else:
        return 0.5 - area

def chi2_pdf(x, df):
    """PDF de la Distribución Chi-Cuadrada"""
    if x <= 0: return 0
    log_num = ((df/2) - 1) * math.log(x) - (x/2)
    log_den = (df/2) * math.log(2) + math.lgamma(df/2)
    return math.exp(log_num - log_den)

def chi2_cdf(x, df):
    """CDF de la Distribución Chi-Cuadrada"""
    if x <= 0: return 0
    if df == 1:
        return norm_cdf(math.sqrt(x)) - norm_cdf(-math.sqrt(x))
    if df == 2:
        return 1 - math.exp(-x/2)
    return integrate(lambda val: chi2_pdf(val, df), 1e-8, x, n=max(2000, int(x*20)))

def f_pdf(x, df1, df2):
    """PDF de la Distribución F de Fisher"""
    if x <= 0: return 0
    log_num = (df1 / 2) * math.log(df1 * x / df2)
    log_den = math.log(x) + ((df1 + df2) / 2) * math.log(1 + df1 * x / df2)
    log_beta = math.lgamma(df1/2) + math.lgamma(df2/2) - math.lgamma((df1+df2)/2)
    return math.exp(log_num - log_den - log_beta)

def f_cdf(x, df1, df2):
    """CDF de la Distribución F de Fisher"""
    if x <= 0: return 0
    return integrate(lambda val: f_pdf(val, df1, df2), 1e-8, x, n=max(2000, int(x*20)))

# ==========================================
# CÁLCULO DE VALORES CRÍTICOS (INVERSAS / PPF)
# ==========================================

def _bisection(cdf_func, target_prob, low, high):
    """Encuentra la raíz de cdf_func(x) = target_prob (Algoritmo numérico de Bisección)"""
    # Expandir el límite si es necesario para distribuciones que van a infinito
    while cdf_func(high) < target_prob:
        high *= 2.0
    
    for _ in range(80):
        mid = (low + high) / 2.0
        p_mid = cdf_func(mid)
        if abs(p_mid - target_prob) < 1e-5:
            return mid
        if p_mid < target_prob:
            low = mid
        else:
            high = mid
    return (low + high) / 2.0

def norm_ppf(p):
    """Inversa de la CDF Normal (Z)"""
    return _bisection(norm_cdf, p, -10.0, 10.0)

def t_ppf(p, df):
    """Inversa de la CDF T-Student (t crítico)"""
    return _bisection(lambda t: t_cdf(t, df), p, -50.0, 50.0)

def chi2_ppf(p, df):
    """Inversa de la CDF Chi-Cuadrada (Chi2 crítico)"""
    return _bisection(lambda x: chi2_cdf(x, df), p, 1e-5, float(df) * 3.0 + 10.0)

def f_ppf(p, df1, df2):
    """Inversa de la CDF F de Fisher (F crítico)"""
    return _bisection(lambda x: f_cdf(x, df1, df2), p, 1e-5, 10.0)
