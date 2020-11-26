from typing import Optional

from fastapi import FastAPI

from app import is_alive_host

app = FastAPI()

@app.get("/healthz")
def read_item(hostname: Optional[str]):
    data = {}
    if is_alive_host(hostname):
        data['status'] = 'up'
    else:
        data['status'] = 'down'
    data['hostname'] = hostname
    return  data
