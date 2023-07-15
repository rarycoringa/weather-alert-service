import logging

from typing import NoReturn

def callback(ch, method, properties, body) -> NoReturn:
    logging.info(
        "Received message on queue _"
        f"\nch: {ch}"
        f"\nmethod: {method}"
        f"\nproperties: {properties}"
        f"\nbody: {body.decode()}"
    )