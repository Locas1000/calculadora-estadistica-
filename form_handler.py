from hypothesis_tests import (
    test_one_proportion,
    test_two_proportions,
    test_one_mean,
    test_two_means,
    test_one_variance,
    test_two_variances
)

def get_float(form_data, field_name):
    """
    Busca en todos los campos con el mismo nombre y devuelve el primero que no esté vacío.
    Esto evita que los campos ocultos del HTML choquen con los visibles.
    """
    valores = form_data.getlist(field_name)
    for val in valores:
        if val is not None and val.strip() != "":
            return float(val)
    raise ValueError(f"Faltan datos requeridos en el formulario.")

def process_test_request(form_data):
    """
    Parsea los datos del formulario (request.form) y ejecuta la prueba correspondiente.
    """
    test_type = form_data.get('test_type')
    alpha = get_float(form_data, 'alpha')
    tail = form_data.get('tail', 'two-sided')

    if test_type == '1_prop':
        return test_one_proportion(
            get_float(form_data, 'x1'),
            get_float(form_data, 'n1'),
            get_float(form_data, 'p0'),
            alpha, tail
        )
        
    elif test_type == '2_prop':
        return test_two_proportions(
            get_float(form_data, 'x1'),
            get_float(form_data, 'n1'),
            get_float(form_data, 'x2'),
            get_float(form_data, 'n2'),
            alpha, tail
        )
        
    elif test_type == '1_mean':
        return test_one_mean(
            get_float(form_data, 'x_bar1'),
            get_float(form_data, 's1'),
            get_float(form_data, 'n1'),
            get_float(form_data, 'mu0'),
            alpha, tail
        )
        
    elif test_type == '2_mean':
        return test_two_means(
            get_float(form_data, 'x_bar1'),
            get_float(form_data, 's1'),
            get_float(form_data, 'n1'),
            get_float(form_data, 'x_bar2'),
            get_float(form_data, 's2'),
            get_float(form_data, 'n2'),
            alpha, tail
        )
        
    elif test_type == '1_var':
        return test_one_variance(
            get_float(form_data, 's1'),
            get_float(form_data, 'n1'),
            get_float(form_data, 'sigma0_sq'),
            alpha, tail
        )
        
    elif test_type == '2_var':
        return test_two_variances(
            get_float(form_data, 's1'),
            get_float(form_data, 'n1'),
            get_float(form_data, 's2'),
            get_float(form_data, 'n2'),
            alpha, tail
        )
        
    else:
        raise ValueError("Tipo de prueba inválida o no seleccionada.")
