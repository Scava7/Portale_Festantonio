import pandas as pd
import sqlite3

# Carica l'Excel
df = pd.read_excel("DB_Esportato2.xlsx")
print(df.head())

# Connessione al database
conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

# Opzionale: visualizza colonne per controllo
print("Colonne trovate:", df.columns)

# Inserimento manuale delle righe
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO app_iscrizioni_iscrizione (
            first_name,
            last_name,
            data_di_nascita,
            phone,
            timestamp,
            torneo,
            squadra,
            codice_fiscale,
            note,
            email,
            pagato
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        row["NOME"],
        row["COGNOME"],
        pd.to_datetime(row["DATA DI NASCITA"], errors="coerce").date() if not pd.isna(row["DATA DI NASCITA"]) else None,
        str(row["RECAPITO TELEFONICO"]).strip() if not pd.isna(row["RECAPITO TELEFONICO"]) else None,
        pd.to_datetime(row["DATA INSERIMENTO"], errors="coerce").date() if not pd.isna(row["DATA INSERIMENTO"]) else None,
        row["TORNEI"] if not pd.isna(row["TORNEI"]) else None,
        row["SQUADRE"] if not pd.isna(row["SQUADRE"]) else None,
        row["CODICE FISCALE"] if not pd.isna(row["CODICE FISCALE"]) else None,
        row["TAGLIA MAGLIA"] if not pd.isna(row["TAGLIA MAGLIA"]) else None,
        row["MAIL"] if not pd.isna(row["MAIL"]) else None,
        int(row["ATTIVO"]) if not pd.isna(row["ATTIVO"]) else 0,  # <-- campo pagato
    ))

# Salva e chiudi
conn.commit()
conn.close()

print("Importazione completata.")