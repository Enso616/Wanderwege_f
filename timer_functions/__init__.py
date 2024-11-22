import logging
import azure.functions as func

def main(timer: func.TimerRequest) -> None:
    try:
        # Prüfen, ob der Timer-Trigger korrekt initialisiert wurde
        if timer.schedule_status:
            utc_timestamp = timer.schedule_status.last
            logging.info(f"Timer trigger executed at {utc_timestamp}")
        else:
            logging.warning("Timer schedule_status is None.")
        
    except Exception as e:
        logging.error(f"An error occurred in the timer function: {str(e)}")


        


"""
# Beispiel für die function, die im Azure Function Timer-Trigger ausgeführt wird
def example_function():
    try:
        # Deine Berechnungen
        a = 5
        b = 10
        result = a + b
        logging.info(f"Demo Calculation: {a} + {b} = {result}")
        return "Hello from example_function!"
    except Exception as e:
        logging.error(f"Error in example_function: {str(e)}")
        return "Error"

# Hauptfunktion, die bei einem Timer-Trigger von Azure aufgerufen wird
def main(timer: func.TimerRequest) -> None:
    """
    Diese Funktion wird durch den Timer-Trigger von Azure aufgerufen.
    """
    utc_timestamp = timer.schedule_status.last
    logging.info(f"Timer trigger executed at {utc_timestamp}")

    # Aufruf der example_function
    result = example_function()
    logging.info(f"example_function hat folgendes zurückgegeben: {result}")
    
"""