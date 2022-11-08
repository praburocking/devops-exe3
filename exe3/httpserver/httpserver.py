from typing import Union

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
def read_root():
	f = open("/usr/data/temp_file.txt", "r")
	return str(f.read())


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
    
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
    
