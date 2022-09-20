import numpy as np
import tensorflow as tf
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, validator, root_validator

# loads in pretrained ml model
model = tf.keras.models.load_model('artifacts')

app = FastAPI(debug=True)


# validates data types
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

    # checks if values are 0 or empty
    @validator("Cylinders", "Displacement", "Horsepower", "Weight", "Acceleration", "Model_Year", always=True)
    def validate_mechanical_fields(cls, value):
        if value == 0 or None:
            raise ValueError("Field with mechanical car features can not be empty or 0")
        return value

    # checks that only one country is selected (by typing 1 and 0 at other fields)
    @root_validator()
    def validate_origin_field(cls, values):
        origin_sum = list(map(values.get, ['Europe', 'Japan', 'USA']))
        if sum(origin_sum) > 1:
            raise ValueError("Please Choose only one country")

        if sum(origin_sum) == 0:
            raise ValueError("Please choose at least one country")
        return values


@app.get("/")
async def root():
    return {"message": "Welcome to MPG Prediction Tool"}


@app.post("/predict/")
async def predict_mpg(UserInput: UserInput):
    prediciton = model.predict(
        [UserInput.Cylinders, UserInput.Displacement, UserInput.Horsepower, UserInput.Weight, UserInput.Acceleration,
         UserInput.Model_Year, UserInput.Europe, UserInput.Japan, UserInput.USA]).ravel()

    prediction_rounded = np.round(prediciton[0], 2)

    return {

        "Predicted mpg for your car is {}".format(prediction_rounded)
    }
