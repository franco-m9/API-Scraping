import requests

response = requests.get("https://randomfox.ca/floof")
fox = response.json()

print("Status code of the API request is:", response.status_code)
print("Text response is:", response.text)
print("JSON response is:", response.json())
print("The image is:", fox['image'])
print("The image is:", fox['link'])
