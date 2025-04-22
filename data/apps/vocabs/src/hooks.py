import logging


def trigger_workers(crud:str, app: str, prof: str, nr:str, user:str) -> None:
    logging.debug((f"record[{nr}] called!"))


