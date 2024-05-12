import requests
import random

response = requests.get('https://api.thecatapi.com/v1/images/search')
filename = f"./images/image{random.randint(0,100000000)}.jpg"

if response.status_code == 200:
    json_data = response.json()
    image_url = json_data[0]['url']

    # Download the image content
    image_response = requests.get(image_url)

    if image_response.status_code == 200:
        # Open the file in binary write mode and write the content of the image response to it
        with open(filename, "wb") as file:
            file.write(image_response.content)
        print("Image downloaded successfully.")
    else:
        print("Failed to download image:", image_response.status_code)
else:
    print("Failed to fetch image URL:", response.status_code)
