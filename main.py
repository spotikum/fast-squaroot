from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Inisialisasi templates
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def show_form(request: Request):
    return templates.TemplateResponse("input_form.html", {"request": request})


@app.post("/hitung-akar-kuadrat")
async def hitung_akar_kuadrat(request: Request, angka: float = Form(...)):
    if angka < 0:
        return {"error": "Angka harus positif"}

    akar = angka**0.5
    return templates.TemplateResponse(
        "output_result.html", {"request": request, "hasil": akar}
    )
