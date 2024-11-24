import datetime
import logging

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    logging.info('HELLO DUDE WAKE UP?????????????')    
    logging.warning('I will find YOU!!!')
    a = 5
    b = 20
    c= a*b
    logging.info(f"Result c: {c}")    

    if mytimer.past_due:
        logging.info('The timer is past due!')
        logging.info('HELLO?????????????')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
