import requests
from datetime import datetime
# Set your API details
subscription_key = "3BGu3mcrOfns6mtwrEVgbXe20NhMeVYSn74ALrPsFHOrRY6OoYagJQQJ99ALACYeBjFXJ3w3AAAFACOGSJxI"  # Replace with your actual vision key
endpoint = "https://seproj.cognitiveservices.azure.com"  # Replace with your actual endpoint URL

# Specify the API endpoint
url = f"{endpoint}/computervision/imageanalysis:segment?api-version=2023-02-01-preview&mode=backgroundRemoval"

# Headers for binary data
headers = {
    "Ocp-Apim-Subscription-Key": subscription_key,
    "Content-Type": "application/octet-stream",  # For binary data
}
index = 0
def sendRequest(imagePath):
    now = datetime.now()
    time_string = now.strftime("%H:%M:%S")
    #save the image
    print(output_path)
    with open(imagePath, "rb") as image_file:
        image_data = image_file.read()

    # Make the API request
    response = requests.post(url, headers=headers, data=image_data)

    # Handle the response
    if response.status_code == 200:
        print("Background removed successfully!")
        # Save the returned image (assuming it is in binary format)
      
        output_path = f"image_{time_string}.png"  # Specify the path to save the image
        with open(output_path, "wb") as output_file:
            output_file.write(response.content)
        print(f"Image saved to {output_path}")
        index = index + 1
    else:
        print("Error:")
        print(response.status_code, response.text)


import os

# Get the directory containing the script
current_directory = os.path.dirname(os.path.abspath(__file__))
script_name = os.path.basename(__file__)  # Get the script's filename

# List all files in the directory except the script
files = [
    file for file in os.listdir(current_directory)
    if os.path.isfile(os.path.join(current_directory, file)) and file != script_name
]

print("Files in the directory (excluding the script):")
print(files)

for file in files:
    # Process each image file
    image_path = os.path.join(current_directory, file)
    print(f"Processing image: {image_path}")
    sendRequest(image_path)
    print("--------------------------------------------------")

