import logging
import datetime

# Beispiel für eine einfache Funktion, die lokal aufgerufen wird
def example_function():
    # Berechnungen
    a = 5
    b = 10
    result = a + b
    
    # Logging der Berechnung
    logging.info(f"Demo Calculation: {a} + {b} = {result}")
    
    # Logging der aktuellen Zeit
    logging.info("Current time: %s", str(datetime.datetime.now()))
    
    # Erfolgreiche Ausführung
    logging.info("Successfully executed.")
    logging.info("Die example_function wurde ausgeführt.")
    
    return "Hello from example_function!"


# Hauptfunktion, die bei einem Timer-Trigger in Azure aufgerufen wird
def main():
    # Simuliertes Timestamp
    utc_timestamp = datetime.datetime.utcnow()
    logging.info(f"Timer trigger executed at {utc_timestamp}")

    # Rufe die example_function auf
    result = example_function()
    logging.info(f"example_function hat folgendes zurückgegeben: {result}")


if __name__ == "__main__":
    # Führe die Funktion lokal aus
    logging.basicConfig(level=logging.INFO)
    main()
