import streamlit as st
from loguru import logger
import requests

from api_client import calcul

logger.remove()
logger.add("./logs/dev_frontend.log",
          rotation="10 MB",
          retention="7 days",
          compression="zip",
          level="TRACE",
          enqueue=True,
          format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")

def render_form():
    with st.form(key='square', clear_on_submit=True):
        integer = st.number_input(label='Integer', step=1, value=1)
        submitted = st.form_submit_button(label='Calulate')
        if submitted:
            form_data = { 'integer': integer }
            try:
                result = calcul(form_data)
                if result:
                    square = result.get('result')
                    st.write(f'The square value of {integer} is: {square}')
            except requests.exceptions.RequestException as error:
                st.error(f"Erreur lors de la prédiction : {error}")

def main():
    st.set_page_config(page_title="Calculate square value")
    render_form()

if __name__ == "__main__":
    main()