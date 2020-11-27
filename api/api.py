from typing import Optional

from fastapi import FastAPI

from api.sockets import is_alive_host


app = FastAPI()

@app.get("/")
def info():
   return  {'info': 'You need to specify /healthz?hostname=<place here the hostname you are interested in>'}


@app.get("/healthz")
def read_item(hostname: Optional[str]):
    status = is_alive_host(hostname)
    return  {'status': 'up' if status else 'down'}
