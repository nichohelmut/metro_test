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
    return {"message": "Welcome to MPG Prediction FastAPI"}


@app.post("/predict/")
async def predict_mpg(UserInput: UserInput):
    prediciton = model.predict(
        [UserInput.Cylinders, UserInput.Displacement, UserInput.Horsepower, UserInput.Weight, UserInput.Acceleration,
         UserInput.Model_Year, UserInput.Europe, UserInput.Japan, UserInput.USA]).ravel()

    prediction_rounded = np.round(prediciton[0], 2)

    return {

        "Predicted mpg for your car is {}".format(prediction_rounded)
    }


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host='0.0.0.0')
