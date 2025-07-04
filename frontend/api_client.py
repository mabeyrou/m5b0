from os import getenv
from dotenv import load_dotenv
import requests
from loguru import logger

load_dotenv()

API_URL = getenv('API_URL')

def calcul(form_data: int):
    try:
        response = requests.post(url=f'{API_URL}/calcul', json=form_data, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        logger.error(f"Error while calculating: {error}")
        return {"success": False, "message": "Something went wrong while calculating"}
