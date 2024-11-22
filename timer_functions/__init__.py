import logging

def main(mytimer: func.TimerRequest) -> None:
    logging.info("Timer function executed.")
    run_my_script()

def run_my_script():
    print("This is your scheduled Python script.")
