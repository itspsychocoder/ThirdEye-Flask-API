from flask import Flask, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing import image
from PIL import Image
import io

app = Flask(__name__)

# Load the Keras model
MODEL_PATH = "note_classifier_model.keras"
model = load_model(MODEL_PATH)
class_labels = ["fifty", "five-hundred", "five-thousand", "hundred", "ten", "thousand", "twenty"]
def preprocess_image(image, target_size):
    """Preprocess the image to fit the model's expected input."""
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image / 255.0  # Normalize the image
    return image

@app.route("/predict", methods=["POST"])
def predict():
    """API endpoint to predict the currency value from an image."""
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded."}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No file selected."}), 400
    
    print(f"Received image: {file}")
    try:
        image = Image.open(io.BytesIO(file.read()))
        processed_image = preprocess_image(image, target_size=(150, 150))  # Match training size
        prediction = model.predict(processed_image)
        predicted_class_index = np.argmax(prediction, axis=1)[0]
        print(f"Predicted class index: {predicted_class_index}")
        predicted_label = class_labels[predicted_class_index]

        print(f"Predicted currency value: {predicted_label}")

        return jsonify({"currency_value": predicted_label})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

app.run(debug=True)