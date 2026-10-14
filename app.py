import os
import sys
import threading
import webbrowser
from flask import Flask, render_template, request
from form_handler import process_test_request
from theory_data import THEORY_DICTIONARY, GENERAL_CONCEPTS

def create_app():
    """Fábrica de la aplicación Flask."""
    # Manejo de rutas para cuando la app está compilada con PyInstaller
    if getattr(sys, 'frozen', False):
        template_folder = os.path.join(sys._MEIPASS, 'templates')
        static_folder = os.path.join(sys._MEIPASS, 'static')
        app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
    else:
        app = Flask(__name__)
    return app

app = create_app()

@app.route('/')
def index():
    return render_template(
        'index.html',
        theory_methods=THEORY_DICTIONARY,
        theory_concepts=GENERAL_CONCEPTS,
        initial_tab=request.args.get('tab', 'hipotesis'),
        selected_method=request.args.get('method', '')
    )

@app.route('/teoria')
def teoria():
    return render_template(
        'index.html',
        theory_methods=THEORY_DICTIONARY,
        theory_concepts=GENERAL_CONCEPTS,
        initial_tab='teoria',
        selected_method=request.args.get('method', '')
    )

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Delegamos la extracción de variables y la ejecución lógica al handler
        result = process_test_request(request.form)
    except Exception as e:
        result = {"error": str(e)}

    return render_template('result.html', result=result)

def open_browser():
    """Abre el navegador por defecto automáticamente."""
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == '__main__':
    # Ejecuta open_browser después de 1 segundo (dando tiempo a que Flask arranque)
    threading.Timer(1.0, open_browser).start()
    
    # Debug=False es importante para el ejecutable final
    app.run(port=5000, debug=False)
