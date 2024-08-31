import uvicorn

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import io
import numpy as np
from tensorflow.keras.models import load_model  # type: ignore

from tensorflow.keras.preprocessing import image  # type: ignore
from tensorflow.keras.applications.inception_v3 import preprocess_input  # type: ignore

from io import BytesIO

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = load_model("model/plant_disease_model.h5")

classes = [
    "brinjal-athilacna-beetles",
    "brinjal-fruitborer",
    "brinjal-mites",
    "brinjal-tobacco-mosaic-virus",
    "chili-leaf-curl-complex",
    "pumpkin-mosaic-virus",
]


@app.get("/")
def index():
    return "Welcome to fastapi!"


def predict_image(contents, model):
    img = image.load_img(io.BytesIO(contents), target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_processed = np.expand_dims(img_array, axis=0)
    img_processed /= 255.0

    prediction = model.predict(img_processed)
    # prob = prediction[0]
    index = np.argmax(prediction)

    return {
        "prediction": str(classes[index]).title(),
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    result = predict_image(contents, model)
    return result


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
