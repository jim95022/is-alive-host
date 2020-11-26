from typing import Optional

from fastapi import FastAPI

from api.app import is_alive_host

app = FastAPI()

@app.get("/healthz")
def read_item(hostname: Optional[str]):
    data = {}
    status, host = is_alive_host(hostname)
    if status:
        data['status'] = 'up'
    else:
        data['status'] = 'down'
    data['hostname'] = host
    return  data
