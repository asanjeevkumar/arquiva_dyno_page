from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from app.models.string_model import StringUpdate
from app.controllers.string_controller import StringController
import os

app = FastAPI(title="Dynamic String Service")
templates = Jinja2Templates(directory="app/templates")

# Only mount static files if the directory exists
static_dir = "app/static"
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

string_controller = StringController()

@app.get("/", response_class=HTMLResponse)
async def get_page(request: Request):
    current_string = string_controller.get_current_string()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "dynamic_string": current_string}
    )

@app.post("/update-string")
async def update_string(string_update: StringUpdate):
    return string_controller.update_string(string_update.new_string) 