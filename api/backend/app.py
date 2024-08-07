# STL
import logging

# PDM
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

LOG = logging.getLogger(__name__)

app = FastAPI(title="api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/_next/static", StaticFiles(directory="dist/_next/static"), name="static")


@app.get("/")
def read_root():
    return FileResponse("dist/index.html")


@app.get("/api/endpoint")
async def test_endpoint():
    return "Hello World!"
