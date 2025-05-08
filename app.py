import streamlit as st
import requests
import os
from dotenv import load_dotenv
from db import create_table, salvar_consulta, obter_historico

# Carrega variáveis do .env
load_dotenv()

# Cria a tabela se ainda não existir
create_table()
    
# Função para obter dados da API
def get_weather(city):
    api_key = os.getenv("API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pt_br"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Interface do app
st.title("🌤️ Consulta de Clima por Cidade")

city = st.text_input("Digite o nome da cidade:")

if city:
    data = get_weather(city)
    if data:
        temp = data['main']['temp']
        umidade = data['main']['humidity']
        vento = data['wind']['speed']
        nome_cidade = data['name']
        pais = data['sys']['country']

        st.subheader(f"Clima em {nome_cidade} ({pais})")
        st.metric("🌡️ Temperatura", f"{temp} °C")
        st.metric("💧 Umidade", f"{umidade}%")
        st.metric("💨 Vento", f"{vento} m/s")

        try:
            salvar_consulta(nome_cidade, temp, umidade, vento)
            st.success("Consulta salva no histórico!")
        except Exception as e:
            st.error(f"Erro ao salvar no banco: {e}")
    else:
        st.warning("Cidade não encontrada ou erro na API.")

# Histórico na barra lateral
with st.sidebar:
    st.subheader("📜 Histórico de Consultas")

    historico = obter_historico()

    if historico:
        for cidade, temp, umidade, vento, data in historico:
            st.markdown(f"**{cidade}** - {data.strftime('%d/%m/%Y %H:%M')}")
            st.write(f"🌡️ Temperatura: {temp} °C")
            st.write(f"💧 Umidade: {umidade}%")
            st.write(f"💨 Vento: {vento} m/s")
            st.markdown("---")
    else:
        st.info("Nenhuma consulta registrada ainda.")