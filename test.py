import requests     

# URL of your Flask server
url = 'http://52.55.175.185'

# url = 'http://127.0.0.1:5000'                    
# Path to the image file you want to send

url = 'http://54.224.236.204'

image_path = r'C:\Users\krish\OneDrive\Documents\spring24\Cloud Computing\Assignment1\face_images_1000\test_964.jpg'
                    

# Open the image file in binary mode

with open(image_path, 'rb') as file:
    # Create a dictionary with the file data
    
    files = {'inputFile': file}    
    # Send the POST request with the file data

    response = requests.post(url, files=files) 

# Print the response from the server

print(response.text)