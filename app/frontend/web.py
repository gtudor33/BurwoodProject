from fastapi import Request, FastAPI

from fastapi.templating import Jinja2Templates

web_app = FastAPI()


ENDPOINTS = {"fizzbuzz_number": "/fizzbuzz", "most_common": "/most_common"}
templates = Jinja2Templates(directory="templates")


@web_app.get("/")
async def index(request: Request):
    # Simple frontend landing page to show the fizzbizz app
    return templates.TemplateResponse("index.html", {"request": request})
