# 🌤️ Clima Dashboard com Streamlit e SQLite

Este projeto é uma aplicação web simples desenvolvida em Python com **Streamlit**, que permite consultar dados climáticos de cidades usando a API da OpenWeather. As informações obtidas são armazenadas em um banco de dados **SQLite** local e podem ser visualizadas na barra lateral como histórico de consultas.

---

## 📑 Índice

* [Descrição do Projeto](#descrição-do-projeto)
* [Pré-requisitos](#pré-requisitos)
* [Configuração do Banco de Dados](#configuração-do-banco-de-dados)
* [Como Executar o Projeto](#como-executar-o-projeto)
* [Funcionalidades](#funcionalidades)
* [Licença](#licença)
* [Contribuidores](#contribuidores)

---

## 🧾 Descrição do Projeto

A aplicação permite:

* Consultar o clima atual de qualquer cidade.
* Armazenar as informações (temperatura, umidade, vento) no banco de dados.
* Exibir o histórico de pesquisas na **sidebar**.

Ideal para fins educacionais e demonstrações de integração entre Streamlit, APIs REST e banco de dados local.

---

## ✅ Pré-requisitos

* Python 3.8 ou superior
* Conta gratuita na [OpenWeatherMap](https://openweathermap.org/api) para gerar uma chave de API

---

## 🛠️ Configuração do Banco de Dados

O banco de dados **SQLite** é criado automaticamente com a tabela `clima` ao rodar o sistema. Não é necessário criar manualmente.

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

4. Crie um arquivo `.env` com sua chave da API:

   ```
   API_KEY=sua_chave_aqui
   ```

5. Execute a aplicação:

   ```bash
   streamlit run app.py
   ```

---

## 🎯 Funcionalidades

* 🔍 Consultar clima atual por cidade.
* 💾 Armazenar resultados no banco de dados.
* 📜 Visualizar histórico de pesquisas na **sidebar**.
* ⚠️ Mensagens de erro tratadas para conexões mal sucedidas ou cidades inexistentes.

---

## 🧪 Dicas de Desenvolvimento

* Para apagar entradas de teste do banco, acesse `clima.db` via DBeaver, DB Browser ou script Python de limpeza.
* Utilize extensões como Python e SQLite Viewer no VS Code para melhor experiência de desenvolvimento.

---

## 📝 Licença

Este projeto é de uso educacional e pode ser livremente utilizado e modificado.

---

## 🙋 Contribuidores

* [Giovanna Silva](https://github.com/gihsantsilva) – Responsável pelo desenvolvimento completo da aplicação, incluindo a integração com a API de clima, interface com Streamlit e persistência de dados via PostgreSQL.
* [João Nogueira](https://github.com/nogueirahyper) - Responsável pela configuração e publicação da aplicação em ambiente de nuvem, garantindo seu acesso remoto e funcionamento online.
