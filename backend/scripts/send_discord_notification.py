
import requests
from os import getenv
from dotenv import load_dotenv

load_dotenv()

DISCORD_WEBHOOK_URL = getenv('DISCORD_WEBHOOK_URL')

def send_discord_embed(message):
    """Envoyer un message à un canal Discord via un Webhook."""
    data = {"embeds": [{
                "title": "Envoie de notification via script",
                "description": message,
                "color": 5814783,
                "fields": [{
                        "name": "Status",
                        "value": "Succès",
                        "inline": True
                    }]}]}
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    if response.status_code != 204:
        print(f"Erreur lors de l'envoi de l'embed : {response.status_code}")
    else:
        print("Embed envoyé avec succès !")

send_discord_embed("Test de notification par script.")