import psycopg2
import os

def connect_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS historico (
            id SERIAL PRIMARY KEY,
            cidade TEXT,
            temperatura REAL,
            umidade REAL,
            vento REAL,
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def salvar_consulta(cidade, temperatura, umidade, vento):
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO historico (cidade, temperatura, umidade, vento)
            VALUES (%s, %s, %s, %s)
        """, (cidade, temperatura, umidade, vento))
        conn.commit()
        cur.close()
        conn.close()
        print("[INFO] Consulta salva no banco com sucesso.")
    except Exception as e:
        print(f"[ERRO] Falha ao salvar no banco: {e}")

def obter_historico():
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT cidade, temperatura, umidade, vento, data FROM historico ORDER BY data DESC")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except Exception as e:
        print(f"[ERRO] Falha ao obter histórico: {e}")
        return []