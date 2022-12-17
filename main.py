from modeling.sales_demand_forecasting import TimeSeriesModeling
from modeling.content_filtering import ContentRecommender
from fastapi import FastAPI
from fastapi.param_functions import Depends
from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
app = FastAPI()

class CustomForm(BaseModel):
    janr: str
    nesriyyat: str
    cild: str
    muellif: str
    sehife_sayi: int
    dil: str
    ad: str
    qiymet: float
    kolleksiya: str

@app.post("/predictions")
async def addbook(form_data: CustomForm = Depends()):
    try:
        new_row = [form_data.janr, form_data.nesriyyat,form_data.cild,form_data.muellif,form_data.sehife_sayi,
                   form_data.dil,form_data.ad,form_data.qiymet,form_data.kolleksiya]
        add = ContentRecommender(new_row)
        print(add)
        result = TimeSeriesModeling(book_names=add.recommend()).result()
        return result

    except Exception as e:
        return e

