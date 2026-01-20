from auth import obtener_servicios
from brain import analizar_email
from config import TIMEZONE
from message import enviar_confirmacion_whatsapp 

def ejecutar_bot():
    print("🚀 Iniciando escaneo de correos...")
    gmail, calendar = obtener_servicios()
    
    results = gmail.users().messages().list(userId='me', q='is:unread').execute()
    mensajes = results.get('messages', [])

    if not mensajes:
        print("📭 No hay correos nuevos.")
        return

    for m in mensajes:
        msg = gmail.users().messages().get(userId='me', id=m['id']).execute()
        snippet = msg['snippet']
        headers = msg['payload']['headers']
        f_envio = next(h['value'] for h in headers if h['name'] == 'Date')

        data = analizar_email(snippet, f_envio)

        if data.get("es_valido"):
            # 1. Crear el evento en Calendar
            evento = {
                'summary': data['titulo'],
                'location': data['lugar'],
                'description': data['resumen'],
                'start': {'dateTime': data['inicio'], 'timeZone': TIMEZONE},
                'end': {'dateTime': data['inicio'], 'timeZone': TIMEZONE},
            }
            
            calendar.events().insert(calendarId='primary', body=evento).execute()
            print(f"✅ Evento creado en Calendar: {data['titulo']}")
            
            # 2. ENVIAR WHATSAPP
            enviar_confirmacion_whatsapp(data['titulo'], data['inicio'], data['lugar'])
            
            # 3. Marcar como leído
            gmail.users().messages().batchModify(
                userId='me', 
                body={'removeLabelIds': ['UNREAD'], 'ids': [m['id']]}
            ).execute()
        else:
            print("⏭️ Correo descartado.")

if __name__ == "__main__":
    ejecutar_bot()