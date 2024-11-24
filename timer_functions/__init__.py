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