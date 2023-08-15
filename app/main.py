from fastapi import FastAPI


app = FastAPI()




@app.get("/forecasts")
def get_forecasts(city: str):
    pass

