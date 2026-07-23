from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import json

import os

BASE_DIR = os.path.dirname(__file__)

MODEL_PATH = os.path.join(BASE_DIR, "saved_models", "palm_model.keras")

model = load_model(MODEL_PATH)

def predict_palm(image_path):

    img = Image.open(image_path).convert("RGB")
    img = img.resize((128,128))

    img = np.array(img).astype("float32")/255.0
    img = np.expand_dims(img,axis=0)

    prediction = model.predict(img)[0]

    result = {
        "fate": {
            "present": bool(prediction[0] > 0.5),
            "confidence": round(float(prediction[0]),2)
        },
        "head": {
            "present": bool(prediction[1] > 0.5),
            "confidence": round(float(prediction[1]),2)
        },
        "heart": {
            "present": bool(prediction[2] > 0.5),
            "confidence": round(float(prediction[2]),2)
        },
        "life": {
            "present": bool(prediction[3] > 0.5),
            "confidence": round(float(prediction[3]),2)
        },
        "palm_width": {
            "present": bool(prediction[4] > 0.5),
            "confidence": round(float(prediction[4]),2)
        },
        "line_density": {
            "present": bool(prediction[5] > 0.5),
            "confidence": round(float(prediction[5]),2)
        }
    }

    return result

if __name__ == "__main__":
    IMAGE_PATH = r"C:\Infosys\inosys\Palmistry_Tarot\ai\dataset\test\15_image_palm_jpeg_jpg.rf.d6bc896702835495f21760fcf736dd5c.jpg"
    result = predict_palm(IMAGE_PATH)
    print(json.dumps(result, indent=4))