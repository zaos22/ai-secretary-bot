# cerebro.py
import os
import json
from datetime import datetime
from google import genai # Librería nueva
from dotenv import load_dotenv

load_dotenv()

# Configuramos el cliente nuevo
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analizar_email(cuerpo, fecha_envio):
    hoy = datetime.now().strftime("%Y-%m-%d")
    
    prompt = f"""
    Analyze this email. Today's date: {hoy}. Email sent date: {fecha_envio}.
    
    Task: Extract event details ONLY if it requires attendance (meeting, call, birthday, appointment).
    
    Rules:
    1. If the event is for TODAY ({hoy}), return "es_valido": false.
    2. If the event is for the same date the email was sent ({fecha_envio}), return "es_valido": false.
    3. The event MUST be in the future.
    4. Only appointments, ignore newsletters or general info.

    EMAIL: "{cuerpo}"

    RETURN ONLY JSON:
    {{
        "es_valido": boolean,
        "titulo": "string",
        "inicio": "YYYY-MM-DDTHH:MM:SS",
        "lugar": "string",
        "resumen": "string"
    }}
    """
    
    try:
        # Usamos el modelo que apareció en tu test
        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=prompt
        )
        
        # La nueva librería devuelve el texto de forma más limpia
        text = response.text.strip()
        
        # Limpieza de seguridad por si incluye markdown
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0]
        elif "```" in text:
            text = text.split("```")[1].split("```")[0]
            
        return json.loads(text.strip())
        
    except Exception as e:
        print(f"Error con Gemini 2.5: {str(e)}")
        return {"es_valido": False}