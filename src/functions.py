import re

def extract_sql_statement(output):
    """
    Extracts an SQL statement from a given string that begins with "SELECT" and ends with a semicolon.

    This function searches the input string `output` for an SQL statement that starts with the keyword "SELECT"
    and ends with a semicolon (`;`). The search is case-insensitive and spans multiple lines if needed.

    Parameters:
    output (str): A string potentially containing an SQL statement.

    Returns:
    str: The extracted SQL statement without leading or trailing whitespace if found,
         or "No SQL statement found." if no matching SQL statement is present.
    """
    match = re.search(r"(SELECT.*?;)", output, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()  # Gibt das gefundene SQL-Statement zurück, ohne zusätzliche Leerzeichen
    else:
        return "No SQL statement found."



import pandas as pd  # Für das Lesen der CSV-Datei und DataFrame-Funktionalität
import sqlite3       # Für die Verbindung zur SQLite-Datenbank

def import_csv_to_sqlite(csv_file, table_name, db_name=':memory:'):
    """
    Imports data from a CSV file into a specified SQLite database table.

    Parameters:
    csv_file (str): The path to the CSV file to import.
    table_name (str): The name of the table in the SQLite database where the data will be imported.
    db_name (str): The name of the SQLite database file (default is ':memory:' for an in-memory database).

    Returns:
    None
    """
    # Verbindung zur SQLite-Datenbank herstellen (Standard ist eine in-memory-Datenbank)
    conn = sqlite3.connect(db_name)
    try:
        df = pd.read_csv(csv_file)  # CSV-Datei einlesen
        df.to_sql(table_name, conn, if_exists='replace', index=False)  # Daten in die SQLite-Tabelle importieren
    finally:
        conn.close()  # Datenbankverbindung schließen



import random
from datetime import datetime, timedelta
# Funktion, um zufällige Datumswerte zu erzeugen
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))
