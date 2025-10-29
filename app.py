from flask import Flask
import os
import psycopg2

app = Flask(__name__)

# Get the database URL from environment variable or hardcode it for testing
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:mfOdWoKCBfCQscLionSzHTCxjdStyYWl@mainline.proxy.rlwy.net:10754/railway")

@app.route('/')
def home():
    # Try connecting to the database
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        message = f"✅ Connected to PostgreSQL Database successfully!<br>📦 Database URL: {DATABASE_URL}<br>🧠 PostgreSQL Version: {db_version[0]}"
    except Exception as e:
        message = f"❌ Failed to connect to database.<br>Error: {e}<br>Database URL: {DATABASE_URL}"

    # Return simple HTML page
    return f"""
    <html>
    <head>
        <title>Flask + PostgreSQL (Railway)</title>
        <style>
            body {{ font-family: Arial; background-color: #f0f0f0; padding: 50px; }}
            div {{ background-color: white; padding: 20px; border-radius: 10px; }}
        </style>
    </head>
    <body>
        <div>
            <h2>🚀 Flask Connected to Railway PostgreSQL!</h2>
            <p>{message}</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
