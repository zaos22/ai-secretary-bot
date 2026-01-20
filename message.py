# notificador.py
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

ID_INSTANCE = os.getenv("GREEN_API_ID")
API_TOKEN = os.getenv("GREEN_API_TOKEN")
WHATSAPP_ID = os.getenv("WHATSAPP_GROUP_ID") # El que acabas de copiar

def enviar_confirmacion_whatsapp(titulo, inicio, lugar):
    url = f"https://api.green-api.com/waInstance{ID_INSTANCE}/sendMessage/{API_TOKEN}"
    
    # LÓGICA DE VALIDACIÓN:
    # Si el ID ya tiene @g.us o @c.us, lo usamos tal cual.
    # Si es solo un número, le añadimos @c.us.
    if "@" in WHATSAPP_ID:
        final_chat_id = WHATSAPP_ID
    else:
        final_chat_id = f"{WHATSAPP_ID}@c.us"

    mensaje = (
        f"🤖 *SECRETARIO AI*\n\n"
        f"✅ Evento Agendado:\n"
        f"📅 *{titulo}*\n"
        f"⏰ {inicio}\n"
        f"📍 {lugar}"
    )

    payload = {
        "chatId": final_chat_id, # Aquí va el ID validado
        "message": mensaje
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"📱 WhatsApp enviado con éxito al ID: {final_chat_id}")
        else:
            print(f"❌ Error de validación de Green-API: {response.text}")
    except Exception as e:
        print(f"❌ Error de conexión: {e}")