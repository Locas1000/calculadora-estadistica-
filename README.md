# Calculadora Estadística y de Pruebas de Hipótesis

Esta es una aplicación web full-stack y de escritorio para realizar pruebas de hipótesis estadísticas e intervalos de confianza, construida desde cero con Python puro sin utilizar librerías estadísticas pesadas externas (como SciPy, NumPy o Pandas).

Cuenta además con un **Diccionario de Teoría Estadística interactivo** integrado directamente en la interfaz, con formulaciones matemáticas en LaTeX (MathJax), buscador en tiempo real, supuestos, hipótesis y ejemplos prácticos.

---

## Características

- **Implementación matemática nativa:**
  - Distribuciones implementadas desde cero: Normal Estándar ($Z$), $t$-Student, Chi-Cuadrada ($\chi^2$) y $F$ de Fisher-Snedecor.
  - Integración numérica por la **Regla de Simpson 1/3** para calcular probabilidades acumuladas (CDFs) y valores $p$ (*p-values*).
  - Búsqueda de raíces numéricas por el método de **Bisección** para determinar valores críticos inversos (PPF) e intervalos de confianza.
- **Pruebas de hipótesis e intervalos de confianza incluidos:**
  1. Una Proporción ($Z$)
  2. Dos Proporciones ($Z$)
  3. Una Media ($t$-Student)
  4. Dos Medias Independientes (Prueba $t$ de Welch ante varianzas desiguales)
  5. Una Varianza ($\chi^2$)
  6. Dos Varianzas / Cociente de Varianzas ($F$ de Fisher)
- **Diccionario de Teoría Estadística Integrado:**
  - Pestaña interactiva con buscador y filtros por distribución ($Z$, $t$, $\chi^2$, $F$, conceptos clave).
  - Formulación matemática renderizada con MathJax.
  - Objetivos, supuestos, hipótesis bilaterales/unilaterales, errores estándar, intervalos de confianza, reglas de decisión y ejemplos prácticos.
  - Botón de enlace directo para cargar cualquier método inmediatamente en la calculadora.
- **Herramientas & Conversiones auxiliares:**
  - Conversión instantánea de varianza muestral ($s^2$) a desviación estándar ($s$).
  - Cálculo automático de tamaño ($n$), media ($\bar{x}$), varianza ($s^2$) y desviación ($s$) a partir de listas de datos crudos.

---

## Requisitos

- Python 3.10 o superior
- Dependencias indicadas en `requirements.txt`:
  - Flask 3.0.0
  - Werkzeug 3.0.0
  - PyInstaller (para compilar ejecutables)

---

## Instrucciones de Instalación y Ejecución (Modo Desarrollo)

1. **Abre una terminal** en la carpeta del proyecto:
   ```bash
   cd /home/lucas/Documents/estadistica
   ```

2. **Crea y activa un entorno virtual (recomendado):**
   - En Linux / macOS (Bash / Zsh):
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - En Linux (Fish shell):
     ```fish
     python3 -m venv venv
     source venv/bin/activate.fish
     ```
   - En Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\venv\Scripts\activate
     ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecuta el servidor:**
   ```bash
   python app.py
   ```

5. **Accede a la aplicación:**
   El programa abrirá tu navegador automáticamente en:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📦 Empaquetado y Creación de Ejecutables (Linux y Windows)

Para distribuir la aplicación a usuarios finales sin obligarlos a instalar Python ni dependencias manualmente, se compila con **PyInstaller**.

---

### 🐧 1. Compilación Nativa en Linux (Binario ejecutable ELF, sin `.exe`)

En sistemas basados en Linux (Ubuntu, Debian, Fedora, Arch Linux, Linux Mint, etc.), los ejecutables no utilizan la extensión `.exe`, sino que son binarios nativos en formato ELF que funcionan mediante permisos de ejecución (`+x`).

#### Opción A: Crear un único archivo autónomo portable (Recomendado para Linux)
Genera un solo archivo independiente (~14 MB) que contiene el intérprete de Python, Flask, las hojas de estilo y las plantillas HTML empaquetadas:

1. **Abre la terminal** en la carpeta del proyecto y activa el entorno virtual:
   - Si usas **Bash / Zsh**:
     ```bash
     source .venv/bin/activate
     ```
   - Si usas **Fish shell**:
     ```fish
     source .venv/bin/activate.fish
     ```
2. **Ejecuta la compilación:**
   ```bash
   pyinstaller --clean --noconfirm --onefile --name calculadora_estadistica --add-data "templates:templates" --add-data "static:static" app.py
   ```
   *(Nota: en Linux el separador del argumento `--add-data` son dos puntos `:`).*

3. **Ejecutar el programa:**
   El binario se generará en `dist/calculadora_estadistica`. Otórgale permisos de ejecución (si no los tiene) y ejecútalo:
   ```bash
   chmod +x dist/calculadora_estadistica
   ./dist/calculadora_estadistica
   ```
   *(También puedes hacerle doble clic directamente desde el explorador de archivos gráfico).*

#### Opción B: Compilación rápida en modo carpeta con `app.spec`
1. Ejecuta:
   ```bash
   pyinstaller --clean --noconfirm app.spec
   ```
2. El ejecutable se encontrará en `dist/app/app`.
3. Ejecútalo con:
   ```bash
   chmod +x dist/app/app
   ./dist/app/app
   ```

#### 💡 Acceso directo en el menú de aplicaciones de Linux (.desktop)
Si deseas que la aplicación aparezca en tu menú de programas (GNOME, KDE, XFCE):
1. Crea un archivo lanzador en `~/.local/share/applications/calculadora.desktop`:
   ```ini
   [Desktop Entry]
   Name=Calculadora Estadística
   Comment=Pruebas de Hipótesis e Intervalos de Confianza
   Exec=/home/lucas/Documents/estadistica/dist/calculadora_estadistica
   Terminal=false
   Type=Application
   Categories=Education;Science;Math;
   ```
2. Otórgale permisos:
   ```bash
   chmod +x ~/.local/share/applications/calculadora.desktop
   ```
   ¡Ahora podrás buscar "Calculadora Estadística" directamente en el menú de tu sistema operativo!

---

### 🪟 2. Compilación para Windows (Ejecutable `.exe`)

> [!NOTE]
> PyInstaller genera binarios nativos del sistema donde se ejecuta. Por ello, para obtener un archivo `.exe`, se debe compilar desde Windows (o mediante Wine en Linux).

#### Método 1: Compilación en Windows usando `app.spec` (Recomendado)

El proyecto incluye el archivo [`app.spec`](app.spec) previamente configurado para empaquetar automáticamente las plantillas HTML (`templates/`) y las hojas de estilo (`static/`).

1. **Copia o clona la carpeta del proyecto** en una máquina con Windows.
2. **Abre PowerShell o CMD** dentro de la carpeta del proyecto.
3. **Crea y activa un entorno virtual:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
4. **Instala las dependencias del proyecto:**
   ```powershell
   pip install -r requirements.txt
   ```
5. **Ejecuta la compilación con PyInstaller:**
   ```powershell
   pyinstaller --clean --noconfirm app.spec
   ```
   *(El parámetro `--clean` borra cachés temporales y `--noconfirm` evita preguntas de confirmación).*

6. **Resultado y distribución:**
   - La aplicación compilada se generará en la carpeta:
     ```
     dist\app\app.exe
     ```
   - Al haberse compilado en modo directorio (`--onedir`), para compartir el programa con otros usuarios **debes comprimir en un `.zip` toda la carpeta `dist\app`** (la cual contiene el ejecutable `app.exe` junto a su carpeta interna `_internal` con los archivos estáticos y dependencias).

---

### Método 2: Crear un Único Archivo Portable (.exe One-File)

Si prefieres distribuir un **único archivo `.exe` independiente** (sin carpeta exterior ni subdirectorios):

1. En Windows, con el entorno virtual activado, ejecuta el siguiente comando:
   ```powershell
   pyinstaller --clean --noconfirm --onefile --windowed --add-data "templates;templates" --add-data "static;static" app.py
   ```
   *(Nota: en Windows el separador de `--add-data` es punto y coma `;`).*

2. **Resultado:**
   - Encontrarás un único archivo ejecutable en:
     ```
     dist\app.exe
     ```
   - Este archivo puede copiarse a cualquier computadora con Windows sin necesidad de archivos adicionales.

---

### Método 3: Compilar un `.exe` de Windows desde Linux (usando Wine)

Si te encuentras en un entorno Linux y requieres compilar un `.exe` para Windows sin reiniciar la máquina:

1. Instala Wine y Python para Windows en Wine:
   ```bash
   # Verificar que Wine esté instalado
   wine --version
   ```
2. Instala las dependencias de Python bajo Wine:
   ```bash
   wine python -m pip install -r requirements.txt
   ```
3. Compila el ejecutable usando el archivo `app.spec`:
   ```bash
   wine pyinstaller --clean --noconfirm app.spec
   ```
4. El `.exe` generado estará listo en `dist/app/app.exe`.

---

### ⚙️ ¿Cómo Funciona el Ejecutable al Abrirse?

1. **Detección de entorno congelado (`sys.frozen`):**  
   En [`app.py`](app.py), el código detecta automáticamente si se está ejecutando desde un archivo empaquetado de PyInstaller:
   ```python
   if getattr(sys, 'frozen', False):
       template_folder = os.path.join(sys._MEIPASS, 'templates')
       static_folder = os.path.join(sys._MEIPASS, 'static')
       app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
   ```
   Esto asegura que Flask localice las plantillas HTML y los archivos CSS sin errores de `TemplateNotFound`.
2. **Arranque del servidor y apertura automática del navegador:**  
   Al hacer doble clic en `app.exe`, un hilo en segundo plano espera 1 segundo a que Flask levante el puerto local 5000 y abre automáticamente la pestaña en el navegador predeterminado:
   ```python
   webbrowser.open_new("http://127.0.0.1:5000")
   ```
3. **Modo sin consola de fondo:**  
   La configuración `console=False` (o `--windowed`) evita que se abra una ventana negra de comandos de terminal, brindando una experiencia limpia de aplicación de escritorio.

---

### 🛠️ Solución de Problemas Frecuentes al Empaquetar

- **Error `jinja2.exceptions.TemplateNotFound`:**  
  Ocurre si no se incluyeron las carpetas `templates/` y `static/` al compilar. Asegúrate de compilar usando `app.spec` o pasando `--add-data "templates;templates" --add-data "static;static"`.
- **Falso positivo de antivirus o Windows Defender:**  
  Los ejecutables generados por PyInstaller sin firma comercial digital pueden ser bloqueados preventivamente por Windows SmartScreen o antivirus. Agrega una excepción a la carpeta o presiona *"Más información" -> "Ejecutar de todas formas"*.
- **Puerto 5000 ya en uso:**  
  Si el programa no abre o muestra error de conexión, verifica que no tengas otra instancia previa de `app.exe` o Flask corriendo en segundo plano. Puedes cerrarla desde el Administrador de Tareas.

---

## Estructura del Código

- [`app.py`](app.py): Controlador principal del servidor Flask y fábrica de la aplicación adaptada para PyInstaller y ejecución web.
- [`theory_data.py`](theory_data.py): **Diccionario de Teoría Estadística.** Contiene la información teórica estructurada, fórmulas en LaTeX, hipótesis, supuestos, reglas de decisión y ejemplos de cada método.
- [`form_handler.py`](form_handler.py): Enrutador y procesador de formularios que valida las entradas del usuario y delega el cálculo al método correspondiente.
- [`hypothesis_tests.py`](hypothesis_tests.py): Implementación de las 6 pruebas de hipótesis estadísticas, cálculo de estadísticos, valores $p$, intervalos de confianza y conclusiones interpretativas.
- [`core_math.py`](core_math.py): **El núcleo matemático puro.** Contiene las integrales numéricas (Simpson 1/3), funciones de distribución acumuladas (Normal, $t$, $\chi^2$, $F$) y algoritmo de bisección para valores críticos.
- [`templates/`](templates/): Plantillas HTML5 (`index.html` con calculadora y diccionario de teoría; `result.html` con paso a paso y conclusiones).
- [`static/`](static/): Hojas de estilo CSS (`style.css`).
- [`app.spec`](app.spec): Archivo de configuración oficial de PyInstaller para compilar el ejecutable.
