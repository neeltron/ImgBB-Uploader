import requests

url = "https://api.imgbb.com/1/upload"
payload = {
"key": "lalalala",
"image": base64.b64encode(file.read()),
}
res = requests.post(url, payload)
dict = res.json()
url = dict['data']['url']
print(url)
