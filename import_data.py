import pandas as pd
import sqlite3
from django.utils.text import slugify
import unidecode
import uuid

# Carica l'Excel
df = pd.read_excel("DB_Esportato2.xlsx")
print(df.head())

# Connessione al database
conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

print("Colonne trovate:", df.columns)

for _, row in df.iterrows():
    # Prendi campi base
    first_name = row["NOME"] if not pd.isna(row["NOME"]) else ""
    last_name = row["COGNOME"] if not pd.isna(row["COGNOME"]) else ""
    squadra = row["SQUADRE"] if not pd.isna(row["SQUADRE"]) else ""
    torneo = row["TORNEI"] if not pd.isna(row["TORNEI"]) else ""

    # Costruisci slug
    parts = [first_name, last_name, squadra, torneo]
    parts = [str(p) for p in parts if p]

    if parts:
        slug_string = "-".join(parts)
        slug_string = unidecode.unidecode(slug_string)
        final_slug = slugify(slug_string)
    else:
        final_slug = f"senza-nome-{uuid.uuid4().hex[:8]}"

    # Converte timestamp
    timestamp_value = None
    if not pd.isna(row["DATA INSERIMENTO"]):
        ts = pd.to_datetime(row["DATA INSERIMENTO"], errors="coerce")
        if not pd.isna(ts):
            timestamp_value = ts.to_pydatetime()

    cursor.execute("""
        INSERT INTO app_iscrizioni_iscrizione (
            first_name,
            last_name,
            data_di_nascita,
            luogo_di_nascita,
            numero_documento,
            ente_rilasciatore,
            data_rilascio,
            comune_residenza,
            indirizzo,
            phone,
            timestamp,
            torneo,
            squadra,
            codice_fiscale,
            note,
            email,
            pagato,
            slug
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        first_name,
        last_name,
        pd.to_datetime(row["DATA DI NASCITA"], errors="coerce").date() if not pd.isna(row["DATA DI NASCITA"]) else None,
        row["LUOGO DI NASCITA"] if not pd.isna(row["LUOGO DI NASCITA"]) else None,
        row["NUMERO DOCUMENTO"] if not pd.isna(row["NUMERO DOCUMENTO"]) else None,
        row["RILASCIATO DA"] if not pd.isna(row["RILASCIATO DA"]) else None,
        pd.to_datetime(row["DATA DI RILASCIO"], errors="coerce").date() if not pd.isna(row["DATA DI RILASCIO"]) else None,
        row["COMUNE RESIDENZA"] if not pd.isna(row["COMUNE RESIDENZA"]) else None,
        row["INDIRIZZO RESIDENZA"] if not pd.isna(row["INDIRIZZO RESIDENZA"]) else None,
        str(row["RECAPITO TELEFONICO"]).strip() if not pd.isna(row["RECAPITO TELEFONICO"]) else None,
        timestamp_value,
        torneo if torneo else None,
        squadra if squadra else None,
        row["CODICE FISCALE"] if not pd.isna(row["CODICE FISCALE"]) else None,
        row["TAGLIA MAGLIA"] if not pd.isna(row["TAGLIA MAGLIA"]) else None,
        row["MAIL"] if not pd.isna(row["MAIL"]) else None,
        int(row["ATTIVO"]) if not pd.isna(row["ATTIVO"]) else 0,
        final_slug,
    ))

# Salva e chiudi
conn.commit()
conn.close()

print("Importazione completata.")