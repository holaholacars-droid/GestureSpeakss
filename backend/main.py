from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from crop_recommendation_model import predict_crop, train_model
import uvicorn

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,  # Set to False when using wildcard origins
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

class WeatherData(BaseModel):
    temperature: float
    humidity: float
    rainfall: float
    soil_ph: float = 6.5

@app.options("/predict-crop")
async def options_predict_crop():
    return {"message": "OK"}

@app.post("/predict-crop")
async def get_crop_recommendation(weather_data: WeatherData):
    try:
        prediction = predict_crop(
            temperature=weather_data.temperature,
            humidity=weather_data.humidity,
            rainfall=weather_data.rainfall,
            soil_ph=weather_data.soil_ph
        )
        
        if prediction is None:
            raise HTTPException(status_code=500, detail="Failed to make prediction")
            
        return prediction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/train-model")
async def train_new_model():
    try:
        model, le = train_model()
        return {"message": "Model trained successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 