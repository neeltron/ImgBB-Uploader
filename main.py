import requests
import base64
import os

image = input("Enter the path to your image: ")

with open(image, "rb") as file:
  url = "https://api.imgbb.com/1/upload"
  payload = {
  "key": os.environ['imgbb'],
  "image": base64.b64encode(file.read()),
  }
  res = requests.post(url, payload)
  dict = res.json()
  url = dict['data']['url']
  print("The URL of your image is: ", url)
