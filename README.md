# Calculadora Estadística y de Pruebas de Hipótesis

Esta es una calculadora web full-stack que realiza pruebas de hipótesis estadísticas, construida desde cero con Python puro sin utilizar librerías matemáticas o estadísticas externas (como SciPy, NumPy o Pandas).

## Características

- Implementación desde cero de las distribuciones: Normal Estándar, T-Student, Chi-Cuadrada y F de Fisher.
- Integración numérica programada de forma nativa en Python (Regla de Simpson 1/3) para calcular los valores de probabilidad (p-values) de las distribuciones complejas.
- Pruebas incluidas:
  - Una Proporción
  - Dos Proporciones
  - Una Media
  - Dos Medias (Independientes, Varianzas desiguales)
  - Una Varianza
  - Dos Varianzas
- Renderizado de fórmulas paso a paso en la interfaz (usando MathJax).

## Requisitos

- Python 3.x
- Flask

## Instrucciones de Instalación y Ejecución

1. **Abre una terminal** en el directorio del proyecto (`/home/lucas/Documents/estadistica`).

2. **Crea y activa un entorno virtual (opcional pero recomendado):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instala las dependencias (Flask):**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecuta el servidor backend:**
   ```bash
   python3 app.py
   ```

5. **Accede a la aplicación:**
   Abre tu navegador web y visita la siguiente dirección:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Estructura del Código

- `app.py`: Archivo principal del servidor (controlador). Se encarga de recibir las peticiones web y enviar las respuestas.
- `math_logic.py`: **El núcleo matemático.** Contiene todas las aproximaciones a las funciones de distribución (PDFs, CDFs) e integrales realizadas con matemáticas puras a través de la librería estándar de Python (`math`).
- `templates/`: Plantillas HTML5.
- `static/`: Archivos CSS3.
