import os
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import pdfplumber

# Base de datos ficticia (puede ser reemplazada por una base de datos real)
clientes = {
    "12345": {"nombre_empresa": "Empresa A", "correo": "empresa_a@example.com"},
    "67890": {"nombre_empresa": "Empresa B", "correo": "empresa_b@example.com"},
}

# Configuración del servidor SMTP para Gmail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "example@example.com"  # Reemplaza con tu correo
EMAIL_PASSWORD = "tu_contraseña_o_contraseña_de_aplicación"  # Usa una contraseña de aplicación si es necesario

def extraer_numero_cliente(pdf_path):
    """Extrae el número de cliente del PDF."""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                texto = page.extract_text()
                if texto:
                    # Buscar un patrón de número de cliente (ajusta según tu formato)
                    match = re.search(r"Número de Cliente:\s*(\d+)", texto)
                    if match:
                        return match.group(1)
        print(f"No se encontró el número de cliente en el archivo: {pdf_path}")
        return None
    except Exception as e:
        print(f"Error al procesar el archivo PDF ({pdf_path}): {e}")
        return None

def obtener_datos_cliente(numero_cliente):
    """Obtiene los datos del cliente basados en el número de cliente."""
    datos = clientes.get(numero_cliente, None)
    if not datos:
        print(f"No se encontraron datos para el cliente con número: {numero_cliente}")
    return datos

def enviar_correo(destinatario, archivo_adjunto):
    """Envía un correo electrónico con el archivo adjunto."""
    mensaje = MIMEMultipart()
    mensaje["From"] = EMAIL_ADDRESS
    mensaje["To"] = destinatario
    mensaje["Subject"] = "Comprobante de Pago Adjunto"

    cuerpo = "Adjunto encontrarás tu comprobante de pago."
    mensaje.attach(MIMEText(cuerpo, "plain"))

    # Adjuntar el archivo PDF
    try:
        with open(archivo_adjunto, "rb") as adjunto:
            parte = MIMEBase("application", "octet-stream")
            parte.set_payload(adjunto.read())
            encoders.encode_base64(parte)
            parte.add_header(
                "Content-Disposition",
                f"attachment; filename={os.path.basename(archivo_adjunto)}",
            )
            mensaje.attach(parte)
    except Exception as e:
        print(f"Error al adjuntar el archivo ({archivo_adjunto}): {e}")
        return

    # Conectar al servidor SMTP y enviar el correo
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Habilita la conexión segura
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, destinatario, mensaje.as_string())
        server.quit()
        print(f"Correo enviado a {destinatario}")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

def procesar_comprobante(pdf_path):
    """Procesa un comprobante de pago y envía el correo correspondiente."""
    numero_cliente = extraer_numero_cliente(pdf_path)
    if not numero_cliente:
        print(f"No se pudo extraer el número de cliente del archivo: {pdf_path}")
        return

    datos_cliente = obtener_datos_cliente(numero_cliente)
    if not datos_cliente:
        print(f"No se encontraron datos para el cliente con número: {numero_cliente}")
        return

    print(f"Enviando correo a {datos_cliente['nombre_empresa']}...")
    enviar_correo(datos_cliente["correo"], pdf_path)

def procesar_multiples_comprobantes(carpeta_pdf):
    """Procesa todos los archivos PDF en una carpeta."""
    if not os.path.isdir(carpeta_pdf):
        print("La carpeta no existe.")
        return

    for nombre_archivo in os.listdir(carpeta_pdf):
        if nombre_archivo.lower().endswith(".pdf"):
            pdf_path = os.path.join(carpeta_pdf, nombre_archivo)
            try:
                print(f"Procesando archivo: {pdf_path}")
                procesar_comprobante(pdf_path)
            except Exception as e:
                print(f"Error al procesar {pdf_path}: {e}")

if __name__ == "__main__":
    # Ruta de la carpeta que contiene los PDFs
    carpeta_pdf = input("Ingresa la ruta de la carpeta con los PDFs: ").strip()
    procesar_multiples_comprobantes(carpeta_pdf)