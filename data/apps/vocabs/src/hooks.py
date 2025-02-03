import logging
from saxonche import PyXdmNode

def create_record_pre(crud:str, app: str, prof: str, nr:str, user:str, rec:PyXdmNode) -> tuple[PyXdmNode, str]:
    #inspect/modify rec
    return rec, "this message will be ignored"
    #return None, "Create record not allowed!"

def create_record_post(crud:str, app: str, prof: str, nr:str, user:str) -> None:
    logging.debug((f"record[{nr}] created!"))
    count(crud,app,prof,nr,user)

stats = {}
def count(crud:str, app: str, prof: str, nr:str, user:str, rec:PyXdmNode | None=None):
    global stats
    if crud in stats:
       stats[crud] = stats[crud] + 1
    else:
       stats[crud] = 1
    logging.debug((f"{stats}]"))
