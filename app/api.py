import numpy as np
import tensorflow as tf
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

model = tf.keras.models.load_model('artifacts')

app = FastAPI(debug=True)


class UserInput(BaseModel):
    Cylinders: int
    Displacement: float
    Horsepower: float
    Weight: float
    Acceleration: float
    Model_Year: int
    Europe: int
    Japan: int
    USA: int


@app.get("/")
async def root():
    return {"message": "Welcome to Your Sentiment Classification FastAPI"}


@app.post("/predict/")
async def predict_mpg(UserInput: UserInput):
    prediciton = model.predict(
        [UserInput.Cylinders, UserInput.Displacement, UserInput.Horsepower, UserInput.Weight, UserInput.Acceleration,
         UserInput.Model_Year, UserInput.Europe, UserInput.Japan, UserInput.USA]).ravel()

    return {

        "Predicted mpg for your car is {}".format(np.round(prediciton[0], 2))
    }


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host='0.0.0.0')

# docker build -t mpg-prediction-app -f app/Dockerfile app/
# docker run -p 80:80 mpg-prediction-app:latest

# curl -X 'POST' \
#   'http://0.0.0.0/predict/' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "Cylinders": 5,
#   "Displacement": 100,
#   "Horsepower": 100,
#   "Weight": 2500,
#   "Acceleration": 15,
#   "Model_Year": 77,
#   "Europe": 1,
#   "Japan": 0,
#   "USA": 0
# }'
