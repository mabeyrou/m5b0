from os import getenv
import requests
from loguru import logger

API_URL = getenv('API_URL')

def health():
    try:
        response = requests.get(url=f'{API_URL}/health', timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        logger.error(f"API health check failed: {error}")
        return {"is_running": False, "status": "offline"}
    
def calcul(form_data: int):
    try:
        response = requests.post(url=f'{API_URL}/calcul', json=form_data, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        logger.error(f"Error while calculating: {error}")
        return {"success": False, "message": "Something went wrong while calculating"}
