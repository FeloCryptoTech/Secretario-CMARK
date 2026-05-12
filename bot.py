import telebot
import time
from flask import Flask
from threading import Thread

# --- EL ENGAÑO PARA RENDER ---
app = Flask('')
@app.route('/')
def home(): return "Bunker Activo"

def run(): app.run(host='0.0.0.0', port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()

# --- CONFIGURACIÓN ---
TOKEN = '8665833044:AAF2Zs1CG8B4fl69-nLABXwbOn3XZ4StIL0'
bot = telebot.TeleBot(TOKEN)
ID_DEL_GRUPO = -1001234567890 # <--- ¡IMPORTANTE! REEMPLAZA ESTO

# --- FUNCIÓN DEL RELOJ (CADA 1 HORA) ---
def recordatorio_seguridad():
    while True:
        try:
            # Aquí pones el ID de tu grupo para que el bot hable solo
            mensaje = "🚨 **¡BÚNKER ACTIVO!**\n\nRecuerden que para comprar seguro deben ir al soporte privado: https://t.me/+Tzo4C3jek_QxNGUx\n\n⚠️ No acepten tratos por fuera. Eviten a los fachos y las estafas. ¡Aquí mandamos nosotros!"
            bot.send_message(ID_DEL_GRUPO, mensaje, parse_mode="Markdown")
        except Exception as e:
            print(f"Error en reloj: {e}")
        
        time.sleep(3600) # Espera 3600 segundos (1 hora)

# --- RESPUESTAS POR PALABRAS CLAVE ---
@bot.message_handler(func=lambda message: True)
def responder(message):
    texto = message.text.lower()
    if any(p in texto for p in ["duda", "ayuda", "luzia", "precio", "comprar", "mlc"]):
        bot.reply_to(message, "¡Oye asere! 🎓 Para dudas o negocios, entra al Búnker Privado: https://t.me/+Tzo4C3jek_QxNGUx")
    elif any(p in texto for p in ["estafa", "denuncia", "manuel", "facho"]):
        bot.reply_to(message, "¡🚨 ALERTA! Reporta al facho o la estafa aquí: @SoporteGlobal_bot")

if __name__ == "__main__":
    keep_alive()
    # Iniciamos el reloj en un hilo separado para que no trabe al bot
    Thread(target=recordatorio_seguridad).start()
    bot.polling()
