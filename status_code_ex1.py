import requests

url = "https://www.youtube.com"

r = requests.get(url)
status_code = r.status_code

# print(status_code)

print(r.text)