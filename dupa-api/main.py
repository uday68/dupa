from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


origin = []
@app.get("/")
async def health_check():
    print("Fastapi server working")
    return  {"<h2>message</h2>":"hello world"}

