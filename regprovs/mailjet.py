from mailjet_rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

def send_mailjet_email(to_email, name, username, password, link):
    """
    Envía un correo usando Mailjet con plantilla y variables dinámicas.
    
    Args:
        to_email (str): Correo del destinatario.
        name (str): Nombre del usuario.
        username (str): Nombre de usuario.
        password (str): Contraseña.
        link (str): Enlace personalizado.
    """
    api_key = os.environ['MJ_APIKEY_PUBLIC']
    api_secret = os.environ['MJ_APIKEY_PRIVATE']
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')

    data = {
        'Messages': [
            {
                "From": {
                    "Email": "beig.techsolutions@gmail.com",
                    "Name": "Beig Tech Solutions"
                },
                "To": [
                    {
                        "Email": "beig.techsolutions@gmail.com"
                    }
                ],
                "TemplateID": 6993866,
                "TemplateLanguage": True,
                "Variables": {
                    "name": name,
                    "username": username,
                    "password": password,
                    "link": link
                }
            }
        ]
    }

    result = mailjet.send.create(data=data)
    return {
        "status_code": result.status_code,
        "response": result.json()
    }