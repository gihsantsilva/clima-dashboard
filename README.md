Não consegui acessar diretamente o seu repositório pelo link, mas posso corrigir o README com base nas mudanças que você descreveu — substituindo **SQLite** por **PostgreSQL** e ajustando as instruções para o banco correto.

Segue a versão revisada:

---

# 🌤️ Clima Dashboard com Streamlit e PostgreSQL

Este projeto é uma aplicação web simples desenvolvida em Python com **Streamlit**, que permite consultar dados climáticos de cidades usando a API da OpenWeather. As informações obtidas são armazenadas em um banco de dados **PostgreSQL** e podem ser visualizadas na barra lateral como histórico de consultas.

---

## 📑 Índice

* [Descrição do Projeto](#descrição-do-projeto)
* [Pré-requisitos](#pré-requisitos)
* [Configuração do Banco de Dados](#configuração-do-banco-de-dados)
* [Como Executar o Projeto](#como-executar-o-projeto)
* [Funcionalidades](#funcionalidades)
* [Capturas de Tela](#capturas-de-tela)
* [Licença](#licença)
* [Contribuidores](#contribuidores)

---

## 🧾 Descrição do Projeto

A aplicação permite:

* Consultar o clima atual de qualquer cidade.
* Armazenar as informações (temperatura, umidade, vento) no banco de dados PostgreSQL.
* Exibir o histórico de pesquisas na **sidebar**.

Ideal para fins educacionais e demonstrações de integração entre Streamlit, APIs REST e banco de dados relacional.

---

## ✅ Pré-requisitos

* Python 3.8 ou superior
* PostgreSQL instalado e em execução
* Conta gratuita na [OpenWeatherMap](https://openweathermap.org/api) para gerar uma chave de API

---

## 🛠️ Configuração do Banco de Dados

1. Crie um banco de dados no PostgreSQL:

   ```sql
   CREATE DATABASE clima_dashboard;
   ```

2. Crie a tabela necessária:

   ```sql
   CREATE TABLE IF NOT EXISTS clima (
       id SERIAL PRIMARY KEY,
       cidade VARCHAR(100),
       temperatura NUMERIC,
       umidade NUMERIC,
       vento NUMERIC,
       data_consulta TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

3. Crie um usuário e conceda permissões (opcional):

   ```sql
   CREATE USER clima_user WITH PASSWORD 'sua_senha';
   GRANT ALL PRIVILEGES ON DATABASE clima_dashboard TO clima_user;
   ```

4. Configure o arquivo `.env`:

   ```
   API_KEY=sua_chave_aqui
   DB_HOST=localhost
   DB_NAME=clima_dashboard
   DB_USER=clima_user
   DB_PASSWORD=sua_senha
   DB_PORT=5432
   ```

---

## ▶️ Como Executar o Projeto

1. Clone o repositório:

   ```bash
   git clone https://github.com/gihsantsilva/clima-dashboard
   cd clima-dashboard
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute a aplicação:

   ```bash
   streamlit run app.py
   ```

---

## 🎯 Funcionalidades

* 🔍 Consultar clima atual por cidade.
* 💾 Armazenar resultados no PostgreSQL.
* 📜 Visualizar histórico de pesquisas na **sidebar**.
* ⚠️ Mensagens de erro tratadas para conexões mal sucedidas ou cidades inexistentes.

---

## 🖼️ Capturas de Tela

#### Tela principal:

![Captura de tela 2025-05-27 143159](https://github.com/user-attachments/assets/2c7a90cb-f994-40a6-a8af-764884a4488e)

#### Exemplos de Uso:

![Captura de tela 2025-05-27 143205](https://github.com/user-attachments/assets/92660b4e-5b68-439d-992d-4761459dff3c)

---

## 📝 Licença

Este projeto é de uso educacional e pode ser livremente utilizado e modificado.

---

## 🙋 Contribuidores

* [Giovanna Silva](https://github.com/gihsantsilva) – Responsável pelo desenvolvimento completo da aplicação, incluindo a integração com a API de clima, interface com Streamlit e persistência de dados via PostgreSQL.
