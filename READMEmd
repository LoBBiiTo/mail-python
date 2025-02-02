**Requisitos del Programa**

1. Subir comprobantes de pago en formato PDF : El usuario debe poder cargar archivos PDF.
2. Extraer el número de cliente del PDF : Detectar el número de cliente dentro del contenido del PDF.
3. Asociar el número de cliente con una empresa : Usar una base de datos o un diccionario para mapear números de cliente a empresas.
4. Enviar correos electrónicos : Enviar un correo electrónico a la dirección asociada al cliente, adjuntando el PDF correspondiente.

**Herramientas Necesarias**

1. PyPDF2 o pdfplumber : Para extraer texto de archivos PDF.
2. re (expresiones regulares) : Para detectar el número de cliente en el texto extraído.
3. sqlite3 o un diccionario: Para almacenar la relación entre números de cliente y empresas.
4. smtplib : Para enviar correos electrónicos.
5. email.mime : Para construir el correo con adjuntos.

**Explicación del Código**

1. Extracción del Número de Cliente:
- Usamos pdfplumber para leer el contenido del PDF.
- Aplicamos una expresión regular (re.search) para encontrar el número de cliente en el texto extraído.
2. Búsqueda de Datos del Cliente :
- Usamos un diccionario como base de datos temporal. Si usas una base de datos SQL, puedes reemplazar esta parte con consultas.
3. Envío de Correos Electrónicos :
- Construimos un mensaje MIME con un archivo adjunto usando email.mime.
- Enviamos el correo a través de un servidor SMTP configurado.
4. Interacción con el Usuario :
- El programa solicita la ruta del archivo PDF y verifica si existe antes de procesarlo.

**Consideraciones Adicionales**

1. Formato del PDF:
- Asegúrate de que el número de cliente esté en un formato consistente en todos los PDF. Si no es así, ajusta la expresión regular.

2. Seguridad:
- No expongas tus credenciales de correo en el código. Usa variables de entorno o un archivo de configuración seguro.

3. Escalabilidad:
- Si tienes muchos archivos PDF, considera usar un bucle para procesarlos en lote.

4. Formato Imgaen:
- Si son imágenes, necesitarás usar OCR (por ejemplo, con pytesseract).

**Servidor SMTP**

*¿Qué es SMTP?*
- SMTP (Simple Mail Transfer Protocol) es un protocolo utilizado para enviar correos electrónicos. Cuando envías un correo desde tu programa, necesitas conectarte a un servidor SMTP que se encargue de entregar el mensaje al destinatario.

*¿Para qué sirve?*
- En el programa, el servidor SMTP se utiliza para enviar los correos electrónicos con los comprobantes de pago adjuntos. Necesitas configurar un servidor SMTP que permita enviar correos desde tu cuenta de Gmail.

*Configuración para Gmail*
- Gmail proporciona un servidor SMTP que puedes usar. Aquí están los detalles:

- **Servidor SMTP** : smtp.gmail.com
- **Puerto** : 587 (para TLS)
- **Correo electrónico** : Tu dirección de Gmail
- **Contraseña** : Tu contraseña de Gmail o una contraseña de aplicación (ver más abajo).

**Pasos para configurar Gmail**

*Habilitar el acceso a aplicaciones menos seguras:*
- Ve a la página de seguridad de tu cuenta de Google: https://myaccount.google.com/security .
- Activa la opción "Acceso de aplicaciones menos seguras". Esto permite que tu programa se conecte a Gmail.

- Usar una contraseña de aplicación (opcional pero recomendado) :
- Si tienes la autenticación de dos factores habilitada, no podrás usar tu contraseña normal. En su lugar, debes generar una "contraseña de aplicación".
- Ve a la página de contraseñas de aplicación: https://myaccount.google.com/apppasswords .
- Genera una contraseña para **"Correo"** y úsala en lugar de tu contraseña normal.

**Actualiza el código:**
- Reemplaza las variables de configuración SMTP en tu código con los valores de Gmail:

**Formato de carpetas**

tu_carpeta/
│
├── main.py          # El archivo Python con el código que compartí
├── comprobantes/    # Carpeta donde colocaste los PDFs con números de cliente.
│   ├── archivo1.pdf
│   ├── archivo2.pdf
│   └── ...
└── otros_archivos/  # Opcional: otros archivos o carpetas que puedas tener

**EJECUTAR EL PROGRAMA**

*Una vez que estés en la carpeta correcta, ejecuta el programa con el siguiente comando:*
Bash: python main.py

Si usamos Python3
Bash: python3 main.py


