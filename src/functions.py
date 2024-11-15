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



import os
import sqlite3
import pandas as pd

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
    # Verbindung zur SQLite-Datenbank herstellen
    conn = sqlite3.connect(db_name)
    try:
        df = pd.read_csv(csv_file)  # CSV-Datei einlesen
        df.to_sql(table_name, conn, if_exists='replace', index=False)  # Daten in die SQLite-Tabelle importieren
        print(f"Importiert: {table_name}")
    finally:
        conn.close()  # Datenbankverbindung schließen

def import_all_csv_to_sqlite(folder_path, db_name=':memory:'):
    """
    Imports all CSV files from a specified folder into a SQLite database, using the file name as the table name.

    Parameters:
    folder_path (str): The path to the folder containing CSV files.
    db_name (str): The name of the SQLite database file (default is ':memory:' for an in-memory database).

    Returns:
    None
    """
    # Für jede CSV-Datei im Ordner
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):  # Nur CSV-Dateien
            csv_file_path = os.path.join(folder_path, file_name)
            table_name = os.path.splitext(file_name)[0]  # Tabellenname ohne Dateiendung
            import_csv_to_sqlite(csv_file_path, table_name, db_name)
            print(f"Tabelle '{table_name}' wurde aus '{file_name}' importiert.")


import random
from datetime import datetime, timedelta
# Funktion, um zufällige Datumswerte zu erzeugen
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))




import sqlite3

def create_tables(db_name='university_database.db'):
    """
    Creates the required tables in the specified SQLite database.

    Parameters:
    db_name (str): The name of the SQLite database file. Default is 'university_database.db'.
    """
    # Verbindung zur SQLite-Datenbank herstellen (oder erstellen, falls sie noch nicht existiert)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # SQL-Befehle zum Erstellen der Tabellen basierend auf dem Schema in variables.py

    # 1. Tabelle: STUDENT_DIMENSION
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS STUDENT_DIMENSION (
            Student_ID INTEGER PRIMARY KEY,
            First_Name TEXT NOT NULL,
            Last_Name TEXT NOT NULL,
            Date_of_Birth DATE,
            Enrollment_Date DATE,
            Email TEXT UNIQUE
        );
    """)

    # 2. Tabelle: COURSE_DIMENSION
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS COURSE_DIMENSION (
            Course_ID INTEGER PRIMARY KEY,
            Course_Name TEXT NOT NULL,
            Credits INTEGER,
            Department_ID INTEGER,
            FOREIGN KEY (Department_ID) REFERENCES DEPARTMENT_DIMENSION(Department_ID)
        );
    """)

    # 3. Tabelle: PROFESSOR_DIMENSION
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS PROFESSOR_DIMENSION (
            Professor_ID INTEGER PRIMARY KEY,
            First_Name TEXT NOT NULL,
            Last_Name TEXT NOT NULL,
            Email TEXT UNIQUE
        );
    """)

    # 4. Tabelle: DEPARTMENT_DIMENSION
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS DEPARTMENT_DIMENSION (
            Department_ID INTEGER PRIMARY KEY,
            Department_Name TEXT NOT NULL
        );
    """)

    # 5. Tabelle: ENROLLMENT_FACTS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ENROLLMENT_FACTS (
            Enrollment_ID INTEGER PRIMARY KEY,
            Student_ID INTEGER,
            Course_ID INTEGER,
            Professor_ID INTEGER,
            Enrollment_Date DATE,
            Grade TEXT CHECK(Grade IN ('A', 'B', 'C', 'D', 'F')),
            FOREIGN KEY (Student_ID) REFERENCES STUDENT_DIMENSION(Student_ID),
            FOREIGN KEY (Course_ID) REFERENCES COURSE_DIMENSION(Course_ID),
            FOREIGN KEY (Professor_ID) REFERENCES PROFESSOR_DIMENSION(Professor_ID)
        );
    """)

    # Änderungen bestätigen und Verbindung schließen
    conn.commit()
    conn.close()
    
    print("Tabellen wurden erfolgreich erstellt.")
