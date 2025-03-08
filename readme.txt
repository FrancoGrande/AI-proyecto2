# Resumidor de Artículos

Este programa resume artículos o informes de varias fuentes (URLs, archivos PDF, DOCX o texto plano) utilizando el modelo Gemini 1.5 Pro y traduce el resumen a español (Argentina).

## Instalación

1.  **Clonar el repositorio:** (Si corresponde)
2.  **Instalar Python:** Asegúrate de tener Python 3.6 o superior instalado.
3.  **Crear un entorno virtual:**
    ```bash
    python -m venv .venv
    ```
4.  **Activar el entorno virtual:**
    *   En Windows:
        ```bash
        .venv\\Scripts\\activate
        ```
    *   En macOS y Linux:
        ```bash
        source .venv/bin/activate
        ```
5.  **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
6.  **Configurar la clave de la API de Gemini:**
    *   Crear un archivo `secrets.toml` en el mismo directorio que `app.py`.
    *   Agregar el siguiente contenido a `secrets.toml`, reemplazando `"YOUR_API_KEY"` con tu clave de API de Gemini real:
        ```toml
        [gemini]
        api_key = "YOUR_API_KEY"
        ```
7.  **Ejecutar la aplicación Streamlit:**
    ```bash
    streamlit run app.py
    ```

## Uso

1.  Abrir la aplicación Streamlit en tu navegador (generalmente en `http://localhost:8501`).
2.  Seleccionar el tipo de entrada (URL, PDF, DOCX o Texto).
3.  Ingresar los datos de entrada (URL, ruta de archivo o texto).
4.  La aplicación resumirá el contenido y traducirá el resumen a español (Argentina).

## Notas

*   Asegúrate de tener una clave de API de Gemini válida y de que esté configurada correctamente en el archivo `secrets.toml`.
*   El programa utiliza la biblioteca `deep-translator` para la traducción, que puede tener algunas limitaciones.
*   El programa requiere una conexión a Internet para acceder a la API de Gemini y realizar la traducción.