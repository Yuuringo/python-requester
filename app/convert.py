import requests

url = "https://meigen.doodlenote.net/"
response = requests.get(url)

response.encoding = response.apparent_encoding

name = "download.txt"

with open(name, mode="w") as file:
    file.write(response.text)
