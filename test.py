import requests
import numpy as np


def classify_image(file_path, endpoint_url="http://127.0.0.1:5000/predict"):
    """
    Sends an image file to the Flask app's classify endpoint.

    Args:
        file_path (str): The local path to the image file.
        endpoint_url (str): The URL of the Flask classify endpoint.

    Returns:
        dict: The response from the Flask app.
    """
    try:
        # Open the file in binary mode for sending
        with open(file_path, 'rb') as img_file:
            files = {'file': img_file}

            # Send the POST request
            response = requests.post(endpoint_url, files=files)

            # Check for HTTP errors
            response.raise_for_status()

            # Return the JSON response
            return response.json()

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


image_path = "test1.jpg"

# Call the classify_image function
result = classify_image(image_path)
# Print the result
print(result)